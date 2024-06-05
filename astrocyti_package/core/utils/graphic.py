def graphic_save_and_show(max_intensities_in_area, z):
    import numpy as np
    import matplotlib.pyplot as plt
    time_intervals = np.linspace(0, len(max_intensities_in_area) / 2, 300)
    plt.figure(figsize=(8.27, 3.69), dpi=300)
    plt.plot(time_intervals, max_intensities_in_area, color='#00C78B', linewidth=1.5, label='Максимум интенсивности')
    plt.xlabel('Время (секунд)')
    plt.ylabel('Максимум интенсивности')
    plt.title('График максимумов интенсивности в зависимости от времени')
    plt.legend()
    plt.xlim(time_intervals[0], time_intervals[-1])
    plt.ylim(0, max(max_intensities_in_area) * 1.1)
    plt.grid()
    plt.savefig(f'intensity_max_plot{z}.png', bbox_inches='tight')
    plt.savefig(f'intensity_max_plot{z}.svg', bbox_inches='tight')
    plt.show()