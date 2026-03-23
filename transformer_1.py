import matplotlib.pyplot as plt
import numpy as np

# Длина аудио (в секундах)
audio_length = np.array([1, 5, 10, 20, 30, 60, 120, 180, 300, 600])

# WER с chunking
cnn_wer = np.array([25, 15, 12, 10, 10, 12, 12, 13, 13, 14])
rnn_wer_chunked = np.array([30, 18, 12, 10, 12, 15, 18, 20, 22, 25])
transformer_wer_chunked = np.array([28, 15, 8, 5, 5, 6, 7, 8, 9, 10])

# Создаем график
plt.figure(figsize=(12,6))
plt.plot(audio_length, cnn_wer, marker='o', label='RNN')
plt.plot(audio_length, rnn_wer_chunked, marker='s', linestyle='-', label='CNN')
plt.plot(audio_length, transformer_wer_chunked, marker='^', linestyle='-', label='Transformer')

plt.title('График зависимости WER от длины аудио')
plt.xlabel('Длина аудио (секунды)')
plt.ylabel('WER (%)')

# Логарифмическая шкала для пропорций графика
plt.xscale('log')

# Кастомные подписи по оси X (секунды)
plt.xticks(audio_length, labels=[str(x) for x in audio_length])

plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.show()
