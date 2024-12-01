import random
import time
import matplotlib.pyplot as plt


def bubble_sort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]
  return arr


def selection_sort(arr):
  n = len(arr)
  for i in range(n):
    min_idx = i
    for j in range(i + 1, n):
      if arr[j] < arr[min_idx]:
        min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
  return arr


def insertion_sort(arr):
  for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
      arr[j + 1] = arr[j]
      j -= 1
    arr[j + 1] = key
  return arr


def measure_time(algorithm, arr):
  start_time = time.time()
  algorithm(arr)
  return time.time() - start_time

sizes = list(range(2000, 50001, 2000))

bubble_times = []
selection_times = []
insertion_times = []

for size in sizes:
  print(f'Iniciando para o tamanho {size}')
  arr = [random.randint(1, 10000) for _ in range(size)]

  bubble_times.append(measure_time(bubble_sort, arr.copy()))
  print(f'Bubble sorteado para o tamanho {size}')
  selection_times.append(measure_time(selection_sort, arr.copy()))
  print(f'Selection sorteado para o tamanho {size}')
  insertion_times.append(measure_time(insertion_sort, arr.copy()))
  print(f'Insertion sorteado para o tamanho {size}')

plt.figure(figsize=(10, 6))
plt.plot(sizes, bubble_times, label="Bubble Sort", color='r')
plt.plot(sizes, selection_times, label="Selection Sort", color='g')
plt.plot(sizes, insertion_times, label="Insertion Sort", color='b')

plt.xlabel("Tamanho do Vetor")
plt.ylabel("Tempo de Ordenação (em segundos)")
plt.title("Comparação dos Algoritmos de Ordenação")
plt.legend()
plt.grid(True)
plt.show()
