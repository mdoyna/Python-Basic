num = int(input())

if num <= 100:
    score = 5
elif num >= 1000:
    score = num * 0.1
elif num > 100:
    score = num * 0.2
if num % 10 == 5:
    score += 2
elif num % 2 == 0:
    score += 1

print(score)
print(num + score)

