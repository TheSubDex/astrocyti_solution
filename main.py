from folders import folders_init
from image_processing import read_images_from_folders, max_intensity_matrix_for_pixels, find_largest_white_area, find_largest_white_area_from_all_images, max_intensities_in_biggest_area_from_all_images
from graphing import graphic_save_and_show

def final_func():   
    for Num in range(1, 7):
        folders = folders_init(Num) 
        df = read_images_from_folders(folders)
        print(f"Матрица максимальной интенсивности пикселей :{max_intensity_matrix_for_pixels(df)}\n")
        pixel_coordinates_all_images = find_largest_white_area_from_all_images(df)
        max_intensities_in_area = max_intensities_in_biggest_area_from_all_images(pixel_coordinates_all_images, df)
        graphic_save_and_show(max_intensities_in_area, Num)

if __name__ == "__main__":
    final_func()

# main_module.py
"""
def final_func():

    Выполняет всю обработку изображений используя все остальные модули

"""
