hour = int(input())
minutes = int(input())

total = (hour * 60) + minutes + 15
mins = total % 60
h = total // 60


if mins > 59:
   h = h + 1
   mins = mins - 60
if h >= 24:
   h = h % 24
if mins < 10:
   print('{}:0{}'.format(h, mins))
else:
    print('{}:{}'.format(h, mins))