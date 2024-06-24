import os

def read_subfolders(path):
    """
    Находит все подпапки в указанной директории.

    Аргументы:
    path (str): Путь к директории.

    Возвращает:
    list: Список подпапок в указанной директории.
    """
    subfolders_list = []
    for folders in os.scandir(path):
        if folders.is_dir():
            subfolders_list.append(folders.path)
    return subfolders_list

def create_new_folder(folder_path):
    """
    Создает новые папки для "Выхода".

    Аргументы:
    folder_path (str): Путь к основной папке.

    Возвращает:
    str: Путь к новой папке.
    """
    folder_name = folder_path.split("\\")[-1]
    new_folder_path = os.path.join('D:\Python\last\output', folder_name)
    os.makedirs(new_folder_path, exist_ok=True)
    return new_folder_path