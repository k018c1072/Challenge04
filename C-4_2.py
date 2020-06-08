distance = int(input('距離＞ '))
if distance <= 10:
    print('200円')
else:
    fee = 200
    for d in range(distance - 10, 0, -1):
        fee += 20
    print(str(fee) + '円')
