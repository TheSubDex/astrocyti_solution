def folders_init(Num):
    if Num == 1:
        folders = [
            r'D:\Python\Dataset\last\31_08_2020_tser1\images',
            r'D:\Python\Dataset\last\31_08_2020_tser1\events'
        ]
        return folders
    elif Num == 2:
        folders = [
            r'D:\Python\Dataset\last\31_08_2020_tser2\images',
            r'D:\Python\Dataset\last\31_08_2020_tser2\events'
        ]
        return folders
    elif Num == 3:
        folders = [
            r'D:\Python\Dataset\last\31_08_2020_tser3\images',
            r'D:\Python\Dataset\last\31_08_2020_tser3\events'
        ]
        return folders
    elif Num == 4:
        folders = [
            r'D:\Python\Dataset\last\31_08_2020_tser4\images',
            r'D:\Python\Dataset\last\31_08_2020_tser4\events'
        ]
        return folders
    elif Num == 5:
        folders = [
            r'D:\Python\Dataset\last\2016-05-18_fileNo11_BM3D_z-max\images',
            r'D:\Python\Dataset\last\2016-05-18_fileNo11_BM3D_z-max\events'
        ]
        return folders
    elif Num == 6:
        folders= [
            r'D:\Python\Dataset\last\2016-05-26_fileNo32_BM3D_z-max\images',
            r'D:\Python\Dataset\last\2016-05-26_fileNo32_BM3D_z-max\events'
        ]
        return folders
    else:
        return None

def folders_init(Num):
    """
    Инициализирует папки на основе предоставленного числа.

    Аргументы:
        Num (int): Число, представляющее конфигурацию папок.

    Возвращает:
        list: Список путей к папкам.
    """
