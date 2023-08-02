import contextlib
import os


def createFileFolder(file_path):
    file_name = file_path.split("/")[-1]
    os.makedirs(f'{file_path.split(f"/{file_name}")[0]}/', exist_ok=True)
    return True


def renameFile(source_file_path, target_file_path):
    assert not os.path.exists(target_file_path)

    while os.path.exists(source_file_path):
        with contextlib.suppress(Exception):
            os.rename(source_file_path, target_file_path)
    return True


def removeFile(file_path):
    while os.path.exists(file_path):
        try:
            os.remove(file_path)
        except Exception:
            continue
    return True
