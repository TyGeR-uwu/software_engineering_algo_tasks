from tasks.data_stuctures.stack_max.solution import solution

def test():
    stack = StackMax()
    assert stack.get_max() == "None"
    assert stack.pop() == "error"

    stack.push(7)
    assert stack.get_max() == 7

    stack.push(1)
    stack.push(3)
    assert stack.get_max() == 7

    stack.pop()
    stack.pop()
    assert stack.get_max() == 7

    stack.pop()
    assert stack.get_max() == "None"

test()
