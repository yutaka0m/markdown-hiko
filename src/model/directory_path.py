import dataclasses


@dataclasses.dataclass(frozen=True)
class DirectoryPath:
    """value is /xxx/xxx/xxx
    [relative path] or [absolute path] or [relative path form project root]
    """

    __value: str

    @property
    def value(self) -> str:
        """Custom getter
        :return: If the path ends with "/", trim "/"
        """
        if self.__value.endswith("/"):
            return self.__value[:-1]
        return self.__value
