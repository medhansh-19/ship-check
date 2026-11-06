#!/usr/bin/env python3
"""Convert an explicit ISO deadline to IST and UTC without guessing its zone."""

import argparse
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

IST = timezone(timedelta(hours=5, minutes=30), "IST")


def convert_deadline(value, zone=None):
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is not None:
        if zone:
            raise ValueError("Use either an ISO offset or --zone, not both")
    else:
        if not zone:
            raise ValueError("Deadline needs an explicit UTC offset or --zone IANA name")
        tz = ZoneInfo(zone)
        candidates = []
        for fold in (0, 1):
            candidate = parsed.replace(tzinfo=tz, fold=fold)
            roundtrip = candidate.astimezone(timezone.utc).astimezone(tz)
            if roundtrip.replace(tzinfo=None) == parsed:
                candidates.append(candidate)
        if not candidates:
            raise ValueError("Nonexistent local time during DST transition")
        if len({candidate.utcoffset() for candidate in candidates}) > 1:
            raise ValueError("Ambiguous local time; provide the source's explicit UTC offset")
        parsed = candidates[0]
    return {"IST": parsed.astimezone(IST), "UTC": parsed.astimezone(timezone.utc)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("deadline", help='Example: "2026-11-07T23:59:00+05:30"')
    parser.add_argument("--zone", help="IANA name for a deadline without an offset, e.g. Asia/Kolkata")
    args = parser.parse_args()
    try:
        for name, value in convert_deadline(args.deadline, args.zone).items():
            print(f"{name}: {value.isoformat()}")
    except (ValueError, ZoneInfoNotFoundError) as error:
        parser.exit(1, f"tz: {error}\n")


if __name__ == "__main__":
    main()
