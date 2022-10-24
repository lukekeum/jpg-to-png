import sys


def main():
    if len(sys.argv) < 2:
        raise Exception("Unknown file")
    elif not (sys.argv[1].endswith('.jpg') or sys.argv[1].endswith('.jpeg')):
        raise Exception("Requiring jpg or jpeg file but not found")
    print("[JPNC] Recover Started")


if __name__ == '__main__':
    main()
