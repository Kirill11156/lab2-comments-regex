"""Тесты для лабы 2 (вариант 29)."""

import unittest

from main import is_comment, find_comments, read_file


class TestIsComment(unittest.TestCase):
    def test_hash_comment(self):
        self.assertTrue(is_comment("# просто коментарий"))

    def test_slash_comment(self):
        self.assertTrue(is_comment("// коментарий как в с++"))

    def test_indent(self):
        self.assertTrue(is_comment("   # с отступом"))

    def test_block_comment(self):
        self.assertTrue(is_comment("/* коментарий */"))

    def test_block_two_lines(self):
        self.assertTrue(is_comment("/* начало\nконец */"))

    def test_code_not_comment(self):
        self.assertFalse(is_comment("print(1)"))

    def test_code_with_hash(self):
        self.assertFalse(is_comment("x = 5 # присваивание"))

    def test_url_not_comment(self):
        self.assertFalse(is_comment("https://example.com"))

    def test_unclosed(self):
        self.assertFalse(is_comment("/* незакрытый"))

    def test_empty(self):
        self.assertFalse(is_comment(""))

    def test_spaces(self):
        self.assertFalse(is_comment("    "))


class TestFindComments(unittest.TestCase):
    def test_finds_all(self):
        code = "# шапка\nimport os  # импорт\n\nx = 1\n"
        res = find_comments(code)
        self.assertEqual(len(res), 2)
        self.assertEqual(res[0], ("# шапка", 1))
        self.assertEqual(res[1], ("# импорт", 2))

    def test_multiline(self):
        code = "int a;\n/* много\n   строчный */\nint b; // инлайн\n"
        res = find_comments(code)
        self.assertEqual(len(res), 2)
        self.assertEqual(res[0][0], "/* много\n   строчный */")
        self.assertEqual(res[0][1], 2)
        self.assertEqual(res[1], ("// инлайн", 4))

    def test_no_comments(self):
        self.assertEqual(find_comments("x = 1\ny = 2"), [])

    def test_empty_text(self):
        self.assertEqual(find_comments(""), [])


class TestReadFile(unittest.TestCase):
    def test_missing_file(self):
        self.assertEqual(read_file("takogo_faila_net_123.py"), "")


if __name__ == "__main__":
    unittest.main()
