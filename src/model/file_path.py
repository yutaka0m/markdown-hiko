import dataclasses
import os

from src.model.directory_path import DirectoryPath


@dataclasses.dataclass(frozen=True)
class FilePath:
    # ex: /xxx/xxx/xxx.jpg ([relative path] or [absolute path] or [relative path form project root])
    value: str

    def __hash__(self):
        return hash(self.value)

    def is_absolute_path(self) -> bool:
        return os.path.isabs(self.value)

    def get_directory_path(self) -> DirectoryPath:
        return DirectoryPath(os.path.dirname(self.value))

    def get_base_name(self) -> str:
        return os.path.basename(self.value)
