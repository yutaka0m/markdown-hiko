import os

from src.model.file_path import FilePath
from src.model.directory_path import DirectoryPath


class ImagePathService:
    def __init__(
            self, image_path: FilePath,
            project_root_path: DirectoryPath,
            markdown_file_directory_path: DirectoryPath):
        self.__image_path = image_path
        self.__project_root_path = project_root_path
        self.__markdown_file_directory_path = markdown_file_directory_path

    def get_absolute_path(self) -> FilePath:
        if self.__image_path.is_absolute_path():
            return FilePath(self.__project_root_path.value + self.__image_path.value)
        return FilePath(os.path.abspath(self.__markdown_file_directory_path.value + "/" + self.__image_path.value))
