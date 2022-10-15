from hypothesis import given, strategies as st


def test_valid_anagram_solution_1_true():
    from two_sum_solution_1 import two_sum

    assert two_sum("anagram", "nagaram") == True


def test_valid_anagram_solution_1_false():
    from two_sum_solution_1 import two_sum

    assert two_sum("rat", "car") == False


@given(st.tuples(st.text(), st.text()))
def test_valid_anagram_solution_1_invariant(test_case):
    from two_sum_solution_1 import two_sum

    s, t = test_case
    two_sum(s, t)


@given(st.text())
def test_valid_anagram_solution_1_invariant_equal(test_case):
    from two_sum_solution_1 import two_sum

    two_sum(test_case, test_case)
