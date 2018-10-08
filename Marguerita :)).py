n = int(input())
wight = 8 * n + 2
print("'&$" + "'"*(wight-3))
for i in range(1, n):
    print("'"*(i+1) + "\\" + "'"*(wight - (i+2)))
print("^*"*(4*n)+ "^'")
for i in range(0, n-1):
    a = i + 2 + n + 1 + 2 + (i + 1)
    print("'"*i+"\\\\" + " "*n + "\\" + " "*(wight-a) + "//" + "'"*(i+1))
for i in range(1, n+1):
    a = ((n - 2) + i) + 1 + 1 + (((n - 2) + i) + 1)
    if i == 1:
        print("'" * ((n - 2) + i) + "\\" + "~" * (wight - a) + "/" + "'" * (((n - 2) + i) + 1))
    elif i == n:
        print("'" * ((n - 2) + i) + "\\" + "_" * (wight - a) + "/" + "'" * (((n - 2) + i) + 1))
    else:
        print("'" * ((n - 2) + i) + "\\" + " " * (wight - a) + "/" + "'" * (((n - 2) + i) + 1))
for i in range(1, (n*2)+1):
    a = ((((n * 2) - 1) - 1) + i) + 1 + 1 + (((n * 2) - 1) + i)
    if i == 1:
        print("'" * ((((n * 2) - 1) - 1) + i) + "\\" + "." * (wight - a) + "/" + "'" * (((n * 2) - 1) + i))
    elif i == n*2:
        print("'" * ((((n * 2) - 1) - 1) + i) + "\\" + "_" * (wight - a) + "/" + "'" * (((n * 2) - 1) + i))
    else:
        print("'" * ((((n * 2) - 1) - 1) + i) + "\\" + " " * (wight - a) + "/" + "'" * (((n * 2) - 1) + i))

for i in range(1, (n*2)+2):
    number = (n*4)-1
    print("'" * number + "|||" + "'" * (number+1))
print("_"*(wight-1) + "'")
print("'" + "-"*(wight-3) + "''")