from unittest import TestCase
from .question import FileManagement, Terminology, support_lookup


class TestQuestions(TestCase):
    def test_terminology(self):
        q = Terminology("Mac", "menu bar")
        self.assertEqual(support_lookup["Mac"] + " menu bar", q.search_query())

    def test_file_management(self):
        q = FileManagement("Mac", "folder", 'copy')
        self.assertEqual(support_lookup["Mac"] + " copy folder", q.search_query())

