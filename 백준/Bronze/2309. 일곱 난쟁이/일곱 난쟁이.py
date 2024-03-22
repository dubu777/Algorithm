alst = []
for _ in range(9):
    alst.append(int(input()))
num = sum(alst)-100
for i in range(9):
    for j in range(9):
        if not i == j and alst[i] + alst[j] == num:
            i_idx, j_idx = i, j
            break
alst.remove(alst[i_idx])
alst.remove(alst[j_idx])
alst.sort()
for a in alst:
    print(a)