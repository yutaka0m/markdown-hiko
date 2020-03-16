from unittest import TestCase

from src.service.markdown_text_service import MarkdownTextService


class TestMarkdownService(TestCase):
    def test_find_image_file_path(self):
        markdown = """¥
        # Test case
        ![](./image/file/path)
        ![](./image/file/path)
        ![test](./image/file/path)
        """

        markdown_service = MarkdownTextService(markdown)
        image_file_path_list = markdown_service.find_markdown_image_list()
        self.assertEqual(len(image_file_path_list), 3)

    def test_not_found_file_path(self):
        markdown = "# Test"
        with self.assertRaises(Exception):
            MarkdownTextService(markdown)

    def test_ind_uniq_markdown_image_list(self):
        markdown = """¥
        # Test case
        ![](./image/file/path0)
        ![](./image/file/path1)
        ![test](./image/file/path1)
        """

        markdown_service = MarkdownTextService(markdown)
        image_file_path_list = markdown_service.find_uniq_markdown_image_list()
        self.assertEqual(2, len(image_file_path_list))

    def test_replace_markdown_image_file_path(self):
        markdown = """¥
        # Test case
        ![](./image/file/path1.jpg)
        ![test](./image/file/path2.png)
        """

        expected = """¥
        # Test case
        ![](https://aws.amazon/com/image/path1.jpg)
        ![test](https://aws.amazon/com/image/path2.png)
        """

        markdown_service = MarkdownTextService(markdown)
        result = markdown_service.replace_markdown_image_file_path("https://aws.amazon/com/image/")
        self.assertEqual(expected, result)
