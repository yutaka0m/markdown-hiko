from unittest import TestCase

from src.service.markdown_file_service import MarkdownFileService


class TestOpenMarkDown(TestCase):
    def test_open_mark_down(self):
        markdown = """\
        ![](./image/file/path)
        ![](./image/file/path)
        ![test](./image/file/path)""".replace(" ", "")

        markdown_file_service = MarkdownFileService("./test.md")

        opened_markdown = markdown_file_service.open_markdown()
        self.assertEqual(opened_markdown, markdown)

    def test_not_found(self):
        with self.assertRaises(FileNotFoundError):
            markdown_file_service = MarkdownFileService("./not_found_file.md")
            markdown_file_service.open_markdown()
