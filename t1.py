import random
import time
import matplotlib.pyplot as plt


def bubble_sort(array):
  n = len(array)
  for i in range(n):
    for j in range(0, n - i - 1):
      if array[j] > array[j + 1]:
        array[j], array[j + 1] = array[j + 1], array[j]

  return array


def selection_sort(array):
  n = len(array)
  for i in range(n):
    minimum_index = i
    for j in range(i + 1, n):
      if array[j] < array[minimum_index]:
        minimum_index = j

    array[i], array[minimum_index] = array[minimum_index], array[i]
  return array


def insertion_sort(array):
  n = len(array)
  for i in range(1, n):
    key = array[i]
    j = i - 1

    while j >= 0 and key < array[j]:
      array[j + 1] = array[j]
      j -= 1
    array[j + 1] = key
  return array


def measure_algorithm_time_in_seconds(algorithm, array):
  start_time = time.time()
  algorithm(array)
  return time.time() - start_time

sizes = list(range(2000, 50001, 2000))

bubble_times = []
selection_times = []
insertion_times = []

for size in sizes:
  print(f'Iniciando para o tamanho: {size}')
  arr = [random.randint(1, 10000) for _ in range(size)]

  bubble_times.append(measure_algorithm_time_in_seconds(bubble_sort, arr.copy()))
  print(f'Bubble sorteado para o tamanho: {size}')
  selection_times.append(measure_algorithm_time_in_seconds(selection_sort, arr.copy()))
  print(f'Selection sorteado para o tamanho: {size}')
  insertion_times.append(measure_algorithm_time_in_seconds(insertion_sort, arr.copy()))
  print(f'Insertion sorteado para o tamanho :{size}')

plt.figure(figsize=(10, 6))
plt.plot(sizes, bubble_times, label="Bubble Sort", color='r')
plt.plot(sizes, selection_times, label="Selection Sort", color='g')
plt.plot(sizes, insertion_times, label="Insertion Sort", color='b')

plt.xlabel("Tamanho da array")
plt.ylabel("Tempo (em segundos)")
plt.title("Comparação dos algoritmos")
plt.legend()
plt.grid(True)
plt.show()
