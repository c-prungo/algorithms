from typing import List, Union
import heapq


def calc_perf(
    speed: List[int],
    efficiency: int
):
    return sum(speed) * efficiency


def get_team_performance(
    sample: int,
    speed: List[int],
    efficiency: List[int]
) -> int:

    # sort both lists with respect to each other
    engineers = []
    for eff, spd in zip(efficiency, speed):
        engineers.append([eff, spd])
    engineers.sort(reverse=True)

    speed, perf = 0, 0
    spd_heap = []
    for eff, spd in engineers:

        # pop smallest speed from the running total
        if len(spd_heap) == sample:
            speed -= heapq.heappop(spd_heap)

        # add new speed to the running total
        speed += spd
        heapq.heappush(spd_heap, spd)

        # recalculate running perf
        perf = max(perf, calc_perf(spd_heap, eff))

    return perf % (1e9 + 7)