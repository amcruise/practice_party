import sys

from .pieparty import pieparty


def main(args=None):
    if args is None:
        args = sys.argv[1:]
        pieparty(args)


if __name__ == '__main__':
    sys.exit(main())
