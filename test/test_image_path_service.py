from unittest import TestCase

from src.model.directory_path import DirectoryPath
from src.model.file_path import FilePath
from src.service.image_path_service import ImagePathService


class TestImagePathService(TestCase):
    def test_get_absolute_path_relative_image_file_path(self):
        image_path_service = ImagePathService(
            image_path=FilePath("./image.jpg"),
            project_root_path=DirectoryPath("/usr/project"),
            markdown_file_directory_path=DirectoryPath("/usr/test"),
        )
        self.assertEqual("/usr/test/image.jpg", image_path_service.get_absolute_path().value)

    def test_get_absolute_path_absolute_image_file_path(self):
        image_path_service = ImagePathService(
            image_path=FilePath("/hoge/image.jpg"),
            project_root_path=DirectoryPath(""),
            markdown_file_directory_path=DirectoryPath("/usr/project"),
        )
        self.assertEqual("/hoge/image.jpg", image_path_service.get_absolute_path().value)

    def test_get_absolute_path_absolute_image_file_path_project_root(self):
        image_path_service = ImagePathService(
            image_path=FilePath("/hoge/image.jpg"),
            project_root_path=DirectoryPath("/usr/project"),
            markdown_file_directory_path=DirectoryPath("/usr/project"),
        )
        self.assertEqual("/usr/project/hoge/image.jpg", image_path_service.get_absolute_path().value)
