import random

overbooked = []
for x in range(26):
    overbooked.append(random.randint(1,15))
print(overbooked)
overbookedCount = overbooked.count(15)
print(overbookedCount)
