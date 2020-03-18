import os
import re
from typing import List, Set

from src.model.file_path import FilePath


class MarkdownTextService:
    """Service class of Markdown text
    """

    def __init__(self, markdown_text: str):
        self.markdown_text: str = markdown_text
        self.markdown_image_file_list: Set[FilePath] = self.find_uniq_markdown_image_list()

    def find_markdown_image_list(self) -> List[FilePath]:
        """Find Image file path from Markdown text

        :return: List of the FilePath
        """
        pattern = "\!\[.*\]\(.*\)"
        # Find list of ![xxx](yyy/yyy/yyy.jpg)
        file_list: List[str] = re.findall(pattern, self.markdown_text)

        if len(file_list) == 0:
            raise Exception("Not found file path in Markdown")

        image_file_path_list: List[FilePath] = []
        for file in file_list:
            pattern = "(.*)\]\((.*)"
            # Get yyy/yyy/yyy.jpg
            file_path = re.search(pattern, file).group(2)[:-1]

            if "http" in file_path:
                continue

            image_file_path_list.append(FilePath(file_path))

        return image_file_path_list

    def find_uniq_markdown_image_list(self) -> Set[FilePath]:
        """
        :return: Unique image file path from the Markdown text
        """
        image_file_path_list = self.find_markdown_image_list()
        return set(image_file_path_list)

    def replace_markdown_image_file_path(self, s3_url: str) -> str:
        """Replace [../hoge/fuga.jpg] to [${s3_url}/fuga.jpg]

        :param s3_url: S3's Endpoint URL
        :return: Replaced Markdown text
        """
        if s3_url.endswith("/"):
            s3_url = s3_url[:-1]

        replace_markdown_text = self.markdown_text
        for markdown_image in self.markdown_image_file_list:
            basename = os.path.basename(markdown_image.value)
            replace_markdown_text = replace_markdown_text.replace(markdown_image.value, s3_url + "/" + basename)

        return replace_markdown_text
