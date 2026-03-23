import matplotlib.pyplot as plt
import numpy as np

# Архитектуры
models = ['CNN', 'RNN (LSTM/GRU)', 'Transformer/Conformer']

# Примерные требования к VRAM (ГБ)
vram = [4, 6, 12]  # CNN ~4GB, RNN ~6GB, Transformer ~12GB

# Примерное использование GPU (%) (средняя интенсивность)
gpu_usage = [40, 60, 90]  # условные проценты

# Примерное время обучения (часы)
training_time = [5, 24, 72]  # условные значения для среднего датасета

# Примерные FLOPS (TFLOPS) для инференса / обучения
flops = [1, 5, 20]  # условные значения, Transformer самый требовательный

x = np.arange(len(models))  # позиции для баров
width = 0.2  # ширина баров

fig, ax = plt.subplots(figsize=(12,6))

# Столбцы для каждой метрики
rects1 = ax.bar(x - 1.5*width, vram, width, label='VRAM (GB)')
rects2 = ax.bar(x - 0.5*width, gpu_usage, width, label='Использование GPU (%)')
rects3 = ax.bar(x + 0.5*width, training_time, width, label='Время обучения (ч)')
rects4 = ax.bar(x + 1.5*width, flops, width, label=' TFLOPS')

# Подписи и стиль
ax.set_ylabel('Ресурсы')
ax.set_title('Требования к вычислительным ресурсам для транскрибации аудио')
ax.set_xticks(x)
ax.set_xticklabels(models)
ax.grid(axis='y', linestyle='--', alpha=0.5)
ax.legend()

# Добавим подписи сверху баров
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0,3),
                    textcoords="offset points",
                    ha='center', va='bottom')

add_labels(rects1)
add_labels(rects2)
add_labels(rects3)
add_labels(rects4)

plt.show()
