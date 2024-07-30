def solution(bandage, health, attacks):
    t, x, y = bandage
    start = 0
    hp = health
    for time, power in attacks:
        hp += ((time - start - 1) // t) * y + (time - start - 1) * x
        if hp >= health:
            hp = health
        hp -= power
        if hp <= 0:
            return -1
        start = time
    return hp
