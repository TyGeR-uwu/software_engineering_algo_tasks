def bubble_sort(arr: list[int]) -> list[list[int]]:
    """
    Возвращает снимки массива после каждого прохода,
    в котором были выполнены обмены.
    Если обменов не было ни разу, возвращает один снимок исходного массива.
    """
    n = len(arr)
    a = arr[:]  # работаем с копией, исходный массив не меняем
    snapshots = []
    any_swaps = False

    for i in range(n):
        swapped = False

        # проходим от 0 до n - i - 2
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True

        if swapped:
            snapshots.append(a[:])  # фиксируем снимок после прохода
            any_swaps = True
        else:
            break

    if not any_swaps:
        snapshots.append(a[:])  # массив уже был отсортирован

    return snapshots
