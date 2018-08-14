n = int(input())

width = n * 5

for i in range(1, 2):
    print("." * n + "_" * (width - (2 * n)) + "." * n)
for i in range(2, 3):
    print("." * n + "|" + "*" * ((width - 2) - (2 * n)) + "|" + "." * n)
for i in range(3, 4):
    print("." * n + "\\" + "-" * ((width - 2) - (2 * n)) + "/" + "." * n)
for i in range(4, 7):
    print("." * ((n + i) - 3) + "\\" + "-" * (width - (2 * (n + i) - 4)) + "/" + "." * ((n + i) - 3))
for i in range(7, 8):
    number = (width - (2 * ((n + i) - 3)))
    print("." * ((n + i) - 3) + "|" + "*" * (number // 3) + "1" + "*" * (number // 3) + "|" + "." * ((n + i) - 3))
for i in range(8, 11):
    print("." * (n + 1) + "~" * (width - (2 * (n + 1))) + "." * (n + 1))
