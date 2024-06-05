def read_images_from_folders(folders):
    import os
    from natsort import natsorted
    import cv2
    import pandas as pd

    data = []

    for folder in folders:
        folder_name = os.path.basename(folder)
        dataset_name = "images" if "images" in folder_name else "events"
        image_names = natsorted(os.listdir(folder)) #правильная сортировка по цифрам в названии

        for image_name in image_names:
            image_path = os.path.join(folder, image_name)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            image_data = {
                'dataset': dataset_name,
                'image_name': image_name,
                'image_path': image_path,
                'image_size': image.shape if image is not None else None
            }
            data.append(image_data)

    images_df = pd.DataFrame(data)
    return images_df

def max_intensity_matrix_for_pixels(df):
    import numpy as np
    import cv2
    max_intensity = None

    for index, row in df[df['dataset'] == 'images'].iterrows():
        image = cv2.imread(row['image_path'], cv2.IMREAD_GRAYSCALE)
        numpy_image = np.array(image)
        max_intensity = numpy_image if max_intensity is None else np.maximum(numpy_image, max_intensity)

    return max_intensity

def find_largest_white_area(image):
    import cv2
    contours, musor = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    largest_area = 0
    largest_area_contour = None

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > largest_area:
            largest_area = area
            largest_area_contour = contour

    pixel_coordinates = []
    if largest_area_contour is not None:

        for pixel in largest_area_contour:
            x, y = pixel[0]
            pixel_coordinates.append((x, y))

    return pixel_coordinates

def find_largest_white_area_from_all_images(df):
    import cv2
    pixel_coordinates_all_images = []

    for image_number, (index, row) in enumerate(df[df['dataset'] == 'events'].iterrows()):
        image = cv2.imread(row['image_path'], cv2.IMREAD_GRAYSCALE)
        pixel_coordinates = find_largest_white_area(image)           
        pixel_coordinates_all_images.append((pixel_coordinates, image_number))

    return pixel_coordinates_all_images

def max_intensities_in_biggest_area_from_all_images(pixel_coordinates_all_images, df):
    import cv2
    max_intensities = []

    for index, row in df[df['dataset'] == 'images'].iterrows():
        image = cv2.imread(row['image_path'], cv2.IMREAD_GRAYSCALE)
        max_intensity = 0

        for coordinates in pixel_coordinates_all_images[index][0]:
            x, y = coordinates
            intensity = image[y, x]
            if intensity > max_intensity:
                max_intensity = intensity

        max_intensities.append(max_intensity)

    return max_intensities

def read_images_from_folders(folders):
    """
    Читает изображения из предоставленных папок и заполняет DataFrame.

    Аргументы:
        folders (list): Список путей к папкам.

    Возвращает:
        pd.DataFrame: DataFrame, содержащий данные об изображениях.
    """

def max_intensity_matrix_for_pixels(df):
    """
    Рассчитывает максимальную матрицу интенсивности для пикселей из DataFrame.

    Аргументы:
        df (pd.DataFrame): DataFrame, содержащий данные об изображениях.

    Возвращает:
        np.array: Максимальная матрица интенсивности для пикселей.
    """

def find_largest_white_area(image):
    """
    Находит самую большую белую область на предоставленном изображении.

    Аргументы:
        image (np.array): Изображение для анализа.

    Возвращает:
        list: Список координат пикселей в самой большой белой области.
    """

def find_largest_white_area_from_all_images(df):
    """
    Находит самую большую белую область на всех изображениях в DataFrame.

    Аргументы:
        df (pd.DataFrame): DataFrame, содержащий данные об изображениях.

    Возвращает:
        list: Список координат пикселей со всех изображений.
    """

def max_intensities_in_biggest_area_from_all_images(pixel_coordinates_all_images, df):
    """
    Рассчитывает максимальную интенсивность в самой большой области со всех изображений.

    Аргументы:
        pixel_coordinates_all_images (list): Список координат пикселей.
        df (pd.DataFrame): DataFrame, содержащий данные об изображениях.

    Возвращает:
        list: Список максимальных интенсивностей на всех изображениях.
    """
