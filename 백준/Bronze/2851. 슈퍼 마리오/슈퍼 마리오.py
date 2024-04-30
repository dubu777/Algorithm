lst = [int(input()) for i in range(10)]

temp = 0
num = 987654321
ans = 0
for i in range(10):
    temp += lst[i]
    if abs(100-temp) <= num:
        num = 100-temp
        ans = temp

print(ans)