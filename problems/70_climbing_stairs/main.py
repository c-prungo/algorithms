from argparse import ArgumentParser


def get_args():
    parser = ArgumentParser(description='Input for count_stairs')
    parser.add_argument('--stairs', '-n', default=0, type=int, help='the number of stairs to climb')
    return parser.parse_args()


def main():
    args = get_args()

    memo = [None for _ in range(args.stairs)]
    def climb_stairs(n):

        # initial base cases
        if n < 0: return 0
        if n == 0: return 1

        # initialise key
        key = n-1

        # dynamic return
        if memo[key] != None: return memo[key]

        # recursive call
        memo[key] = climb_stairs(n-1) + climb_stairs(n-2)

        return memo[key]

    print(climb_stairs(args.stairs))


if __name__ == "__main__":
    main()