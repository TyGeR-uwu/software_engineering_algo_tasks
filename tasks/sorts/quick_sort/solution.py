def quick_sort(arr: list[int]) -> list[int]:
    # Возвращаем новый массив, не изменяя оригинальный
    if len(arr) <= 1:
        return arr[:]

    def sort(a):
        if len(a) <= 1:
            return a

        # выбор пивота: медиана из трёх (приём для улучшения среднего случая)
        first, mid, last = a[0], a[len(a) // 2], a[-1]
        pivot = sorted((first, mid, last))[1]

        left = []
        middle = []
        right = []

        for x in a:
            if x < pivot:
                left.append(x)
            elif x > pivot:
                right.append(x)
            else:
                middle.append(x)

        # рекурсивная сортировка
        return sort(left) + middle + sort(right)

    return sort(arr)
