class DoubleConnectedNode:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


def solution(head: DoubleConnectedNode) -> DoubleConnectedNode:
    current = head
    new_head = None

    # Проходим по списку
    while current is not None:
        # Меняем указатели местами
        current.prev, current.next = current.next, current.prev

        # Сохраняем нового head (последний посещённый узел)
        new_head = current

        # Переходим дальше (в "старом" списке это был next → теперь prev)
        current = current.prev

    return new_head
