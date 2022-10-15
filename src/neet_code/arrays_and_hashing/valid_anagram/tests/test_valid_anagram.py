from hypothesis import given, strategies as st


def test_valid_anagram_solution_1_true():
    from valid_anagram_solution_1 import valid_anagram

    assert valid_anagram("anagram", "nagaram") == True


def test_valid_anagram_solution_1_false():
    from valid_anagram_solution_1 import valid_anagram

    assert valid_anagram("rat", "car") == False


@given(st.tuples(st.text(), st.text()))
def test_valid_anagram_solution_1_invariant(test_case):
    from valid_anagram_solution_1 import valid_anagram

    s, t = test_case
    valid_anagram(s, t)


@given(st.text())
def test_valid_anagram_solution_1_invariant_equal(test_case):
    from valid_anagram_solution_1 import valid_anagram

    valid_anagram(test_case, test_case)


def test_valid_anagram_solution_2_true():
    from valid_anagram_solution_2 import valid_anagram

    assert valid_anagram("anagram", "nagaram") == True


def test_valid_anagram_solution_2_false():
    from valid_anagram_solution_2 import valid_anagram

    assert valid_anagram("rat", "car") == False


@given(st.tuples(st.text(), st.text()))
def test_valid_anagram_solution_2_invariant(test_case):
    from valid_anagram_solution_2 import valid_anagram

    s, t = test_case
    valid_anagram(s, t)


@given(st.text())
def test_valid_anagram_solution_2_invariant_equal(test_case):
    from valid_anagram_solution_2 import valid_anagram

    valid_anagram(test_case, test_case)
