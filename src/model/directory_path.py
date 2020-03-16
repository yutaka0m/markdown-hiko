import dataclasses


@dataclasses.dataclass(frozen=True)
class DirectoryPath:
    __value: str

    @property
    def value(self) -> str:
        if self.__value.endswith("/"):
            return self.__value[:-1]
        return self.__value
