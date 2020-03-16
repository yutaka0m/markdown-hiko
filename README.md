# Markdown-hiko ![](https://github.com/yutaka0m/markdown-hiko/workflows/Python%20CI/badge.svg?branch=master)


Markdownに記述してあるローカルファイルを、s3にアップロードし、MarkdownのURLも書き換えます。

Markdown内に、次のような文章があった場合、

```text
# Testです。
![](../image/test.jpg)
```

画像のURLを探して、S3にアップロードします。

また、Markdownも次のように変換して保存します。

```text
# Testです。
![](https://static.s3image.com/test.jpg)
```

## Install

```bash
pip install --user markdown-hiko 
```

※(`$HOME/.local/bin` にパスを通してください)

## Basic Usage

```bash
markdown-hiko \
    --file "/path/to/markdown.md" \
    --url "https://resource.test.com" \
    --bucket "Bucket name"
```

| 引数   | Notes |
| :---------- | :----------------|
| --file | Markdownのファイルパスを指定します（絶対パス or 相対パス) |
| --url | S3のドメイン名 |
| --bucket | S3のバケット名 |
| --root  | (option) 画像のファイルパスが、プロジェクトルートからのパスとなっている場合は、プロジェクトルートのパスを指定する |

## Develop

- GitHubでリリースを作成すると、自動的にPyPIにアップロードされます（setup.pyのVERSIONを上げることを忘れずに）
