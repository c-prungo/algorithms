from args import get_args

def climb_stairs(n: int) -> int:

    memo = [None for _ in range(n)]
    def _recursive(n: int) -> int:

        # initial base cases
        if n < 0: return 0
        if n == 0: return 1

        # initialise key
        key = n-1

        # dynamic return
        if memo[key] != None: return memo[key]

        # recursive call
        memo[key] = _recursive(n-1) + _recursive(n-2)

        return memo[key]

    return _recursive(n)


def main():

    args = get_args()
    print(climb_stairs(args.stairs))


if __name__ == "__main__":

    main()