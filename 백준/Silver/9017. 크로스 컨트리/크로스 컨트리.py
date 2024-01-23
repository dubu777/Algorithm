from collections import Counter

t = int(input())
for _ in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    cnt_lst = dict(Counter(lst))
    # print(cnt_lst)
    new_lst = []
    for i in range(1, len(cnt_lst)+1):
        if cnt_lst[i] == 6:
            new_lst.append(i)
    score_lst = [[] for _ in range(len(cnt_lst)+1)]

    res_lst = []
    for i in range(n):
        if lst[i] in new_lst:
            res_lst.append(lst[i])
    # print(res_lst, 'res')

    for i in range(len(res_lst)):
        score_lst[res_lst[i]].append(i+1)
    # print(score_lst, 'sc')

    sublist_sums = [(sum(sublist[:4]), i) for i, sublist in enumerate(score_lst) if len(sublist) > 4]
    min_sum = min(sublist_sums, key=lambda x: x[0])[0]
    min_sublists = [s for s in sublist_sums if s[0] == min_sum]

    # 최소 합이 유일하면 해당 인덱스 반환, 아니면 5번째 인덱스가 가장 작은 서브리스트의 인덱스 반환
    if len(min_sublists) == 1:
        print(min_sublists[0][1])
    else:
        print(min([(score_lst[i][4], i) for _, i in min_sublists], key=lambda x: x[0])[1])
