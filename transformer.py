import matplotlib.pyplot as plt

architectures = ["CNN", "RNN", "Transformer"]
wer = [20, 15, 5]  # примерные значения WER (%)

plt.figure()
plt.bar(architectures, wer)

plt.xlabel("Архитектура")
plt.ylabel("WER (%)")
plt.title("Сравнение точности моделей для транскрибации аудио")

plt.show()
