from tasks.recursion.binary_search.solution import binary_search

def test_binary_search():
    # 1. Базовый случай — элемент есть в середине
    arr = [1, 3, 5, 7, 9]
    assert binary_search(arr, 5) == 2

    # 2. Граничный случай — элемент в начале массива
    arr = [0, 2, 4, 6, 8]
    assert binary_search(arr, 0) == 0

    # 3. Граничный случай — элемент в конце массива
    arr = [10, 20, 30, 40, 50]
    assert binary_search(arr, 50) == 4

    # 4. Дубликаты — должно вернуть один из корректных индексов
    arr = [1, 2, 2, 2, 3]
    assert binary_search(arr, 2) in (1, 2, 3)

    # 5. Тест на временную сложность — большой массив (до 10^6 элементов)
    #    Проверяем, что работает быстро и возвращает корректный индекс
    arr = list(range(1_000_000))
    assert binary_search(arr, 123456) == 123456

    # Дополнительно: отсутствие элемента
    assert binary_search(arr, 1_000_001) == -1



test_binary_search()
