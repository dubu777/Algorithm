import sys
n = int(sys.stdin.readline())
lst = [int(sys.stdin.readline()) for _ in range(n)]
num_set = list(set(lst))

cnt_lst = []
for sn in num_set:
    temp_lst = []
    for ln in lst:
        if ln != sn:
            temp_lst.append(ln)
    cnt = 1
    max_cnt = 1

    for i in range(1, len(temp_lst)):
        if temp_lst[i-1] == temp_lst[i]:
            cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
        else:
            cnt = 1
            if max_cnt < cnt:
                max_cnt = cnt
    cnt_lst.append(max_cnt)

ans = max(cnt_lst)
print(ans)
