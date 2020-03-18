import argparse
import os

from src.model.directory_path import DirectoryPath
from src.model.file_path import FilePath
from src.service.image_path_service import ImagePathService
from src.service.markdown_file_service import MarkdownFileService
from src.service.markdown_text_service import MarkdownTextService
from src.service.s3_service import S3Service


def main():
    """ markdown-hiko
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", "-f", help="path to Markdown file", required=True)
    parser.add_argument("--url", "-u", help="S2 or CloudFront domain name", required=True)
    parser.add_argument("--bucket", "-b", help="S3 bucket name", required=True)
    parser.add_argument("--root", "-r", help="Project root path", default="", required=False)
    args = parser.parse_args()

    markdown_file_absolute_path = FilePath(os.path.abspath(args.file))
    project_root_absolute_path = DirectoryPath(os.path.abspath(args.root))
    args_aws_domain_name = args.url
    bucket = args.bucket

    markdown_file_directory_path: DirectoryPath = markdown_file_absolute_path.get_directory_path()

    markdown_file_service = MarkdownFileService(markdown_file_absolute_path)
    try:
        markdown_string: str = markdown_file_service.open_markdown()
        markdown_text_service: MarkdownTextService = MarkdownTextService(markdown_string)
    except FileNotFoundError:
        raise Exception("Markdown file is not fount")

    # Upload to S3
    s3_service = S3Service(bucket)
    for file in markdown_text_service.markdown_image_file_list:
        image_path_service = ImagePathService(
            image_path=file,
            project_root_path=project_root_absolute_path,
            markdown_file_directory_path=markdown_file_directory_path,
        )
        s3_service.upload_file(image_path_service.get_absolute_path())

    # Replace Markdown image file path
    replaced_string: str = markdown_text_service.replace_markdown_image_file_path(args_aws_domain_name)
    markdown_file_service.save_markdown(replaced_string)


if __name__ == "__main__":
    main()
