from src.model.file_path import FilePath


class MarkdownFileService:
    def __init__(self, markdown_file_path: FilePath):
        self.markdown_file_path = markdown_file_path

    def open_markdown(self) -> str:
        with open(self.markdown_file_path.value, "r", encoding="utf-8") as file:
            return file.read()

    def save_markdown(self, markdown_string: str) -> None:
        with open(self.markdown_file_path.value, "w", encoding="utf-8") as file:
            file.write(markdown_string)
