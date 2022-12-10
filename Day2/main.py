strategy = open("input").read().split("\n")
while "" in strategy:
    strategy.remove("")
score = 0
for match in strategy:
    score += (ord(match[2].upper()) - 87)
    if ord(match[0]) + 23 == ord(match[2]):
        score += 3  # draw
    elif ord(match[0]) + 24 == ord(match[2]) or ord(match[0]) + 21 == ord(match[2]):
        score += 6  # win

print(f"Score: {score}")

score2 = 0
definitions = [1, 2, 3]
definitions2 = {"A": 0, "B": 1, "C": 2}
for match in strategy:
    score2 += (ord(match[2].upper()) - 88) * 3  # 0 on loss (X), 3 on draw (Y), 6 on win (Z)
    score2 += definitions[(definitions2[match[0]] + ord(match[2].upper()) - 89) % 3]
    # look up index of first letter, add -1 to 1, mod 3, look up answer in possible points
print(f"Score2: {score2}")
