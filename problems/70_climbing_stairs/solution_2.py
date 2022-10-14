from args import get_args

def climb_stairs(n: int) -> int:

    one, two = 1, 1

    for _ in range(n-1):

        # one = one + two & two = one
        # (doing it this way removes need for temp object)
        one, two = one + two, one

    return one


def main():

    args = get_args()
    print(climb_stairs(args.stairs))


if __name__ == "__main__":
    main()