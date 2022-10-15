from hypothesis import given, strategies as st


def test_contains_duplicate_true():
    from contains_duplicate_solution_1 import contains_duplicate

    assert contains_duplicate([1, 4, 2, 3, 4, 5]) == True


def test_contains_duplicate_false():
    from contains_duplicate_solution_1 import contains_duplicate

    assert contains_duplicate([1, 2, 3, 4, 5]) == False


@given(st.lists(st.integers()))
def test_contains_duplicate_invariant(test_case):
    from contains_duplicate_solution_1 import contains_duplicate

    test_case = list(dict.fromkeys(test_case))
    assert contains_duplicate(test_case) == False
