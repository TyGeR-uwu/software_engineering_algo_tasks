from tasks.data_stuctures.bracket_sequence.solution import is_correct_bracket_seq

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
