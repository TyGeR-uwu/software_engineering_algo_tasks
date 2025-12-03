from tasks.data_stuctures.tasks_list.solution import solution

def test():
    assert is_correct_bracket_seq("{[()]}") is True
    assert is_correct_bracket_seq("(]") is False
    assert is_correct_bracket_seq(")(") is False
    assert is_correct_bracket_seq("()") is True
    assert is_correct_bracket_seq("()()") is True
    assert is_correct_bracket_seq("()()()") is True
    assert is_correct_bracket_seq("()()()()") is True
    assert is_correct_bracket_seq("()()()()()") is True
    assert is_correct_bracket_seq("()()()()()()") is True
    assert is_correct_bracket_seq("(asdkjhasdkjasd(dasjkdasjhd)asdjkasd)") is True
    assert is_correct_bracket_seq("[{}()") is False
    assert is_correct_bracket_seq("[(])") is False

test()
