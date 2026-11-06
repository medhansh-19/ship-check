import unittest
from app import TASKS, summarize


class TaskSummaryTests(unittest.TestCase):
    def test_counts_only_completed_tasks(self):
        self.assertEqual(summarize(TASKS), {"total": 3, "completed": 1, "open": 2})

    def test_empty_task_list(self):
        self.assertEqual(summarize([]), {"total": 0, "completed": 0, "open": 0})


if __name__ == "__main__":
    unittest.main()
