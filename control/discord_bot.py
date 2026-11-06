"""Optional Discord controls, sharing the dashboard's approval ledger."""
import asyncio
import difflib
import os
import threading


def start(engine):
    import discord
    owner = int(os.environ["DISCORD_OWNER_ID"])
    channel_id = int(os.environ["DISCORD_CHANNEL_ID"])
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    ready = threading.Event()

    @client.event
    async def on_message(message):
        if message.channel.id != channel_id:
            return
        actor = None
        if message.author.id == owner:
            actor = "owner"
        elif message.webhook_id:
            hooks = await message.channel.webhooks()
            trusted = next((hook for hook in hooks if hook.id == message.webhook_id and hook.user and hook.user.id == client.user.id),None)
            if trusted:
                name = message.author.name.lower()
                if "scout" in name: actor="scout"
                elif "auditor" in name: actor="auditor"
        if not actor:
            return
        text = message.content
        for embed in message.embeds:
            if embed.description:
                text += "\n" + embed.description
        for attachment in message.attachments:
            if attachment.filename.endswith((".md",".txt")) and attachment.size < 200000:
                text += "\n" + (await attachment.read()).decode(errors="replace")
        await asyncio.to_thread(engine.workflow.observe,message.id,actor,text,message.created_at.isoformat())

    class Controls(discord.ui.View):
        def __init__(self, run):
            super().__init__(timeout=None)
            for check in run["checks"]:
                fix = check["proposal"]
                if not fix:
                    continue
                button = discord.ui.Button(label="Review " + fix["path"], custom_id=f"shipcheck:{engine.namespace}:{run['id']}:{fix['id']}", style=discord.ButtonStyle.secondary)
                async def review(interaction, proposal=fix, run_id=run["id"]):
                    if interaction.user.id != owner:
                        return await interaction.response.send_message("Only the configured project owner can approve fixes.", ephemeral=True)
                    diff = "\n".join(difflib.unified_diff(proposal["before"].splitlines(), proposal["after"].splitlines(), fromfile="before/" + proposal["path"], tofile="after/" + proposal["path"], lineterm=""))
                    view = discord.ui.View(timeout=300)
                    for decision in ("approved", "rejected"):
                        action = discord.ui.Button(label="Approve exact change" if decision == "approved" else "Reject", style=discord.ButtonStyle.success if decision == "approved" else discord.ButtonStyle.danger)
                        async def decide(event, choice=decision):
                            if event.user.id != owner:
                                return await event.response.send_message("Owner only.", ephemeral=True)
                            try:
                                await asyncio.to_thread(engine.decide, run_id, proposal["id"], choice, "Discord owner")
                                await event.response.edit_message(content=f"{proposal['path']}: {choice}. Create the PR from the local dashboard after reviewing all fixes.", view=None, attachments=[])
                            except ValueError as error:
                                await event.response.send_message(str(error), ephemeral=True)
                        action.callback = decide
                        view.add_item(action)
                    import io
                    await interaction.response.send_message(proposal["summary"], file=discord.File(io.BytesIO(diff.encode()), filename="proposed-change.diff"), view=view, ephemeral=True)
                button.callback = review
                self.add_item(button)
            rerun = discord.ui.Button(label="Run audit", custom_id=f"shipcheck:{engine.namespace}:audit:{run['id']}", style=discord.ButtonStyle.primary)
            async def audit(interaction):
                if interaction.user.id != owner:
                    return await interaction.response.send_message("Owner only.", ephemeral=True)
                await interaction.response.defer(ephemeral=True)
                state = await asyncio.to_thread(engine.audit, "Discord owner requested recheck")
                await publish(state)
                await interaction.followup.send("Fresh evidence posted in this channel.", ephemeral=True)
            rerun.callback = audit
            self.add_item(rerun)
            pr = discord.ui.Button(label="Create approved PR", custom_id=f"shipcheck:{engine.namespace}:pr:{run['id']}", style=discord.ButtonStyle.success)
            async def create_pr(interaction):
                if interaction.user.id != owner:
                    return await interaction.response.send_message("Owner only.", ephemeral=True)
                await interaction.response.defer(ephemeral=True)
                try:
                    result = await asyncio.to_thread(engine.create_pr, run["id"])
                    await interaction.followup.send("Approved changes: " + result["url"], ephemeral=True)
                except Exception as error:
                    await interaction.followup.send("PR was not created: " + (str(error) if isinstance(error, ValueError) else "check local GitHub authentication and logs"), ephemeral=True)
            pr.callback = create_pr
            self.add_item(pr)

    async def publish(state):
        run = state["run"]
        channel = client.get_channel(channel_id) or await client.fetch_channel(channel_id)
        embed = discord.Embed(title="Ship Check · launch readiness", description=f"**{run['repo']}**\n**{run['passed']}/{run['total']} checks passed** · `{run['branch']}` · `{run['commit']}`", color=0x17583F)
        for check in run["checks"][:18]:
            embed.add_field(name=(check["status"].replace('_',' ').upper() + " · " + check["title"])[:160], value=check["evidence"][:100], inline=False)
        if len(run["checks"]) > 18:
            embed.add_field(name="Additional event requirements", value=f"{len(run['checks']) - 18} more checks with source quotes and verification controls are available in the local dashboard.", inline=False)
        if run.get("event_rules"):
            embed.add_field(name="Selected event", value=run["event_rules"]["name"][:256], inline=False)
        embed.set_footer(text=f"Audit {run['id']} · Static checks; event eligibility and playback need human verification.")
        await channel.send(embed=embed, view=Controls(run), allowed_mentions=discord.AllowedMentions.none())

    @client.event
    async def on_ready():
        if ready.is_set():
            return
        ready.set()
        client.add_view(Controls(engine.state()["run"]))
        await publish(engine.state())

    def notify(state):
        if ready.wait(timeout=1):
            future = asyncio.run_coroutine_threadsafe(publish(state), client.loop)
            def done(result):
                if result.exception():
                    engine.event("discord_error", "Discord delivery failed; dashboard retains the audit.")
            future.add_done_callback(done)

    threading.Thread(target=lambda: client.run(os.environ["DISCORD_BOT_TOKEN"], log_handler=None), daemon=True).start()
    return notify
