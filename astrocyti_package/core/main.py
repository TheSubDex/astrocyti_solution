import FolderUtils
import ImageProcessing
import DataCreatingAndSaving

def final_func(main_folder_path):
    subfolders_list = FolderUtils.read_subfolders(main_folder_path)
    x = 0

    for folder_path in subfolders_list:
        new_folder_path = FolderUtils.create_new_folder(folder_path)

        images_df = ImageProcessing.read_images_from_folders(folder_path)
        max_intensity_matrix = ImageProcessing.max_intensity_matrix_for_pixels(images_df)
        DataCreatingAndSaving.create_and_save_intensity_image(max_intensity_matrix, x, new_folder_path)

        pixel_coordinates_all_images = ImageProcessing.find_largest_white_area_from_all_images(images_df)
        max_intensities = ImageProcessing.max_intensities_in_biggest_area_from_all_images(pixel_coordinates_all_images, images_df)
        time_intervals = DataCreatingAndSaving.graphic_create_and_save(max_intensities, x, new_folder_path)
        DataCreatingAndSaving.save_data_max_intensity_to_table(time_intervals, max_intensities, x, new_folder_path)
        x += 1

main_folder_path = r"D:\Python\last\main_folder"
final_func(main_folder_path)