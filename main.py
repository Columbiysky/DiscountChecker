import subprocess


def main():
    proc = subprocess.Popen(
        'python ./parsers/market.yandex.ru.py https://market.yandex.ru/product--smartfon-apple-iphone-14-pro-max/1768738052?nid=34512430&show-uid=16674637884255687426716002&context=search&sku=101813096786&cpc=MOlNcyBeyLWoxloy9IIwypb6a2qqgagMHJwGzr94D2sBvfYBB9FZAqdBHy6w7BWZ8wkocwsnApZ5k0EMRTPmouu-8K621QNNUhVmLQdipVczq3R2uulSLU0eqKdmv9D62jAN6qNypNhkuL1BN0AJN3kUsMkweoBQ7-wRTi57fhy4GCDdbpqfRyHy7lucwaSHawiBv6Q9wG0%2C&do-waremd5=S5dF40uVhOVXQZxkHL9R7A&sponsored=1',
        stdout=subprocess.PIPE,
        shell=True)
    for line in proc.stdout:
        print(line.decode("utf-8"))


if __name__ == '__main__':
    main()
