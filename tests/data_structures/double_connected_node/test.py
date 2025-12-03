from tasks.data_stuctures.double_connected_node.solution import solution

def test_reverse_doubly_linked_list():
    # ---------- Тест 1: один элемент ----------
    n1 = DoubleConnectedNode(1)
    head = solution(n1)
    assert head.value == 1
    assert head.next is None
    assert head.prev is None

    # ---------- Тест 2: два элемента ----------
    n1 = DoubleConnectedNode(1)
    n2 = DoubleConnectedNode(2, prev=n1)
    n1.next = n2

    head = solution(n1)
    assert head.value == 2
    assert head.next.value == 1
    assert head.prev is None
    assert head.next.next is None
    assert head.next.prev.value == 2

    # ---------- Тест 3: три элемента ----------
    n1 = DoubleConnectedNode(1)
    n2 = DoubleConnectedNode(2, prev=n1)
    n3 = DoubleConnectedNode(3, prev=n2)
    n1.next = n2
    n2.next = n3

    head = solution(n1)
    assert head.value == 3
    assert head.next.value == 2
    assert head.next.next.value == 1
    assert head.next.next.next is None

    # ---------- Тест 4: повторяющиеся значения ----------
    n1 = DoubleConnectedNode(5)
    n2 = DoubleConnectedNode(5, prev=n1)
    n3 = DoubleConnectedNode(5, prev=n2)
    n1.next = n2
    n2.next = n3

    head = solution(n1)
    assert [head.value, head.next.value, head.next.next.value] == [5, 5, 5]

    # ---------- Тест 5: стресс-тест 1000 элементов ----------
    nodes = [DoubleConnectedNode(i) for i in range(1000)]
    for i in range(999):
        nodes[i].next = nodes[i+1]
        nodes[i+1].prev = nodes[i]

    head = solution(nodes[0])

    for i in range(1000):
        assert head.value == 999 - i
        head = head.next



test_reverse_doubly_linked_list()
