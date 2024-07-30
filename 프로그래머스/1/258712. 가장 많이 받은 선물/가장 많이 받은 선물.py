def solution(friends, gifts):

    l = len(friends)
    lst = [[0] * l for _ in range(l)]
    friend_dict = {name: index for index, name in enumerate(friends)}
    gift_cnt = [0] * l
    for gift in gifts:
        p, t = gift.split(" ")
        lst[friend_dict[p]][friend_dict[t]] += 1

    p = [0] * l
    for i in range(l):
        p[i] = sum(lst[i]) - sum([k[i] for k in lst])

    for i in range(l):
        for j in range(l):
            if i == j:
                continue
            if lst[i][j] > lst[j][i]:
                gift_cnt[i] += 1
            elif lst[i][j] == lst[j][i]:
                if p[i] > p[j]:
                    gift_cnt[i] += 1


    return max(gift_cnt)

