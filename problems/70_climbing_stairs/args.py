from argparse import ArgumentParser

def get_args():
    parser = ArgumentParser(description='Input for count_stairs')
    parser.add_argument('--stairs', '-n', default=0, type=int, help='the number of stairs to climb')
    return parser.parse_args()