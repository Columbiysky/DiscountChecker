import subprocess
import sys
from urllib.parse import urlparse


def main(link: str):
    domain = urlparse(link).hostname
    proc = subprocess.Popen(
        f'python ./parsers/{domain}.py {link}',
        stdout=subprocess.PIPE,
        shell=True)
    for line in proc.stdout:
        print(line.decode("utf-8"))


if __name__ == '__main__':
    main(sys.argv[1])
