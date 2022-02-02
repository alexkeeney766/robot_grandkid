from unittest import TestCase
from .question import FileManagement, Terminology, support_lookup


class TestQuestions(TestCase):
    def test_terminology(self):
        q = Terminology("Mac", "menu bar")
        self.assertEqual(support_lookup["Mac"] + r"%20menu%20bar", q.search_query())

    def test_file_management(self):
        q = FileManagement("Mac", "folder", 'copy')
        self.assertEqual(support_lookup["Mac"] + r"%20copy%20folder", q.search_query())

