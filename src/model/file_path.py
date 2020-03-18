import dataclasses
import os

from src.model.directory_path import DirectoryPath


@dataclasses.dataclass(frozen=True)
class FilePath:
    """value is /xxx/xxx/xxx.jpg
    [relative file path] or [absolute file path] or [relative file path form project root]
    """

    value: str

    def __hash__(self):
        return hash(self.value)

    def is_absolute_path(self) -> bool:
        """
        :return: True if FilePath is absolute path
        """
        return os.path.isabs(self.value)

    def get_directory_path(self) -> DirectoryPath:
        """
        :return: Directory path from FilePath
        """
        return DirectoryPath(os.path.dirname(self.value))

    def get_file_name(self) -> str:
        """
        :return: File name from FilePath
        """
        return os.path.basename(self.value)
