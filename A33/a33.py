import threading
import sys

sys.setrecursionlimit(1500)


def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)


def quicksort_fast(arr, inizio=0, fine=-1):  # Porzione di arr
    if fine == -1:
        fine += len(arr)

    if inizio < fine:  # arr con + elementi
        pivot = arr[fine]  # prendo l'ultimo come riferimento
        iprog = inizio
        j = inizio
        while j < fine:  # considero tutti gli elementi che lo precedono
            if arr[j] <= pivot:  # confronto se sono minori dell' ultimo
                arr[iprog], arr[j] = arr[j], arr[iprog]  # scambio con prog
                iprog += 1  # incremento indice progressivo dei minori
            j += 1

        arr[iprog], arr[fine] = arr[fine], arr[iprog]  # il primo dei maggiori lo scambio con il pivot
        quicksort_fast(arr, inizio, iprog - 1)  # parte dei minori o uguali
        quicksort_fast(arr, iprog + 1, fine)  # parte dei maggiori


# RecursionError: maximum recursion depth exceeded in comparison

def testquicksort_fast():
    abba = [3, 2, 5, 2, 4, 6, 8, 7, 4]

    quicksort_fast(abba)

    print(abba)


testquicksort_fast()
