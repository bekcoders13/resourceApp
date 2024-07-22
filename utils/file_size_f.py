import os


def get_file_size(file_path: str) -> int:
    return os.path.getsize(file_path)
