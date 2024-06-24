import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd

def create_and_save_intensity_image(max_intensity_matrix, x, folder_path):
    """
    Создает изображение с максимальной интенсивностью и сохраняет его.

    Аргументы:
    max_intensity_matrix (numpy.ndarray): Матрица максимальной интенсивности.
    x (int): Номер изображения.
    folder_path (str): Путь к папке назначения.

    Возвращает:
    None
    """
    img = cv2.cvtColor(max_intensity_matrix, cv2.COLOR_GRAY2RGB)
    x_start = int(max_intensity_matrix.shape[1] - max_intensity_matrix.shape[1] * 0.33)
    x_max = int(max_intensity_matrix.shape[1] - max_intensity_matrix.shape[1] * 0.33 + 51)
    y = int(max_intensity_matrix.shape[0] - max_intensity_matrix.shape[0] * 0.075)
    cv2.line(img, (x_start, y), (x_max, y), (255, 255, 255), 5)
    text_x_pos = int(max_intensity_matrix.shape[1] * 0.55)
    text_y_pos = int(max_intensity_matrix.shape[0] * 0.88)
    cv2.putText(img, "10 mkm", (text_x_pos, text_y_pos), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    cv2.imwrite(os.path.join(folder_path, f'intensity_image_{x + 1}.png'), img)

def graphic_create_and_save(max_intensities, x, folder_path):
    """
    Строит график зависимости интенсивности и сохраняет его по переданному пути.

    Аргументы:
    max_intensities (list): Максимальные интенсивности.
    x (int): Номер изображения.
    folder_path (str): Путь к папке назначения.

    Возвращает:
    numpy.ndarray: Временные интервалы.
    """
    time_intervals = np.linspace(0, len(max_intensities) / 2, 300)
    graphic = plt.figure(figsize=(6.7, 3.11), dpi=300)
    plt.plot(time_intervals, max_intensities, color='#00C78B', linewidth=1.5, label='Максимум интенсивности')
    plt.xlabel('Время (секунд)')
    plt.ylabel('Максимум интенсивности')
    plt.title('График максимумов интенсивности в зависимости от времени')
    plt.legend()
    plt.xlim(time_intervals[0], time_intervals[-1])
    plt.ylim(0, max(max_intensities) * 1.1)
    plt.grid()
    plt.savefig(os.path.join(folder_path, f'intensity_max_plot{x + 1}.png'), bbox_inches='tight')
    plt.savefig(os.path.join(folder_path, f'intensity_max_plot{x + 1}.svg'), bbox_inches='tight')
    plt.show()
    return time_intervals

def save_data_max_intensity_to_table(time_intervals, max_intensities, x, folder_path):
    """
    Сохраняет массивы максимальной интенсивности и временные интервалы в эксель таблицу.

    Аргументы:
    time_intervals (numpy.ndarray): Временные интервалы.
    max_intensities (list): Максимальные интенсивности.
    x (int): Номер изображения.
    folder_path (str): Путь к папке назначения.

    Возвращает:
    None
    """
    data = {'Time Interval': time_intervals, 'Max Intensity': max_intensities}
    df = pd.DataFrame(data)
    file_name = os.path.join(folder_path, f'intensity_max_table_{x + 1}.xlsx')
    df.to_excel(file_name, index=False)