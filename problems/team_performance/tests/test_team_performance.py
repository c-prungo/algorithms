

def test_team_performance_calculation_basic():
    from solution_1 import calc_perf

    res = calc_perf(
        speed=[1, 2, 3, 4],
        efficiency=1
    )

    assert res == 10


def test_team_performance_case_one():
    from solution_1 import get_team_performance

    res = get_team_performance(
        sample=2,
        speed=[1, 2, 3, 4],
        efficiency=[4, 3, 2, 1]
    )

    assert res == 10


def test_team_performance_case_two():
    from solution_1 import get_team_performance

    res = get_team_performance(
        sample=2,
        speed=[2, 10, 3, 1, 5, 8],
        efficiency=[5, 4, 3, 9, 7, 2]
    )

    assert res == 60