values = list(map(int, input('入力＞ ').split()))
for v in values:
    for i in range(v):
        print('■', end=' ')
    print()
