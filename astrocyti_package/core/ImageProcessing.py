import os
import pandas as pd
import cv2
from natsort import natsorted
import numpy as np

def read_images_from_folders(main_folder):
    """
    Считывает изображения из папок 'images' и 'events' в основной папке.

    Аргументы:
    main_folder (str): Путь к основной папке.

    Возвращает:
    pandas.DataFrame: DataFrame с информацией об изображениях.
    """
    data = []
    images_folder = os.path.join(main_folder, 'images')
    events_folder = os.path.join(main_folder, 'events')

    for folder in [images_folder, events_folder]:
        dataset_name = "images" if "images" in folder else "events"
        image_names = natsorted(os.listdir(folder))

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

def max_intensity_matrix_for_pixels(images_df):
    """
    Находит матрицу максимальной интенсивности для пикселей изображений.

    Аргументы:
    images_df (pandas.DataFrame): DataFrame с информацией об изображениях.

    Возвращает:
    numpy.ndarray: Матрица максимальной интенсивности.
    """
    max_intensity_matrix = None

    for index, row in images_df[images_df['dataset'] == 'images'].iterrows():
        image = cv2.imread(row['image_path'], cv2.IMREAD_GRAYSCALE)
        numpy_image = np.array(image)
        max_intensity_matrix = numpy_image if max_intensity_matrix is None else np.maximum(numpy_image, max_intensity_matrix)

    return max_intensity_matrix

def find_largest_white_area(image):
    """
    Находит контуры самой большой области активности на изображении.

    Аргументы:
    image (numpy.ndarray): Входное изображение.

    Возвращает:
    list: Координаты пикселей контура.
    """
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
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

def find_largest_white_area_from_all_images(images_df):
    """
    Находит контуры самой большой области активности на всех изображениях.

    Аргументы:
    images_df (pandas.DataFrame): DataFrame с информацией об изображениях.

    Возвращает:
    list: Координаты пикселей контура для каждого изображения.
    """
    pixel_coordinates_all_images = []

    for image_number, row in images_df[images_df['dataset'] == 'events'].iterrows():
        image = cv2.imread(row['image_path'], cv2.IMREAD_GRAYSCALE)
        pixel_coordinates = find_largest_white_area(image)           
        pixel_coordinates_all_images.append((pixel_coordinates, image_number))

    return pixel_coordinates_all_images

def max_intensities_in_biggest_area_from_all_images(pixel_coordinates_all_images, images_df):
    """
    Находит максимальную интенсивность в самой большой области активности на изображениях.

    Аргументы:
    pixel_coordinates_all_images (list): Координаты пикселей контура для каждого изображения.
    images_df (pandas.DataFrame): DataFrame с информацией об изображениях.

    Возвращает:
    list: Максимальные интенсивности.
    """
    max_intensities = []

    for index, row in images_df[images_df['dataset'] == 'images'].iterrows():
        image = cv2.imread(row['image_path'], cv2.IMREAD_GRAYSCALE)
        max_intensity = 0

        if index < len(pixel_coordinates_all_images):
            for coordinates in pixel_coordinates_all_images[index][0]:
                x, y = coordinates
                intensity = image[y, x]
                if intensity > max_intensity:
                    max_intensity = intensity

            max_intensities.append(max_intensity) 

    return max_intensities