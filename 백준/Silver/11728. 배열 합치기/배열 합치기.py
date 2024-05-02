'''
정렬된 두배열을 합쳐서 정렬하기
시작은 같은 인덱스에서 시작
반복문 탈출은 둘중 어떤 배열이든 인덱스 밖으로 나가면
나머지 남은 쪽 배열은 그냥 전부 추가
'''

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))


ai = 0
bi = 0
ans = []
while ai < n and bi < m:
    if a[ai] > b[bi]:
       ans.append(b[bi])
       bi += 1
       # if bi == m:
       #     # ans.extend(a[ai:])
       #     for i in range(ai, n):
       #         ans.append(a[i])
       #     break
    elif a[ai] < b[bi]:
        ans.append(a[ai])
        ai += 1
        # if ai == n:
        #     # ans.extend(b[bi:])
        #     for i in range(bi, m):
        #         ans.append(b[i])
        #     break
    else:
        ans.append(a[ai])
        ans.append(b[bi])
        bi += 1
        ai += 1
if ai < n:
    for i in range(ai, n):
        ans.append(a[i])
elif bi < m:
    for i in range(bi, m):
        ans.append(b[i])


print(*ans)
