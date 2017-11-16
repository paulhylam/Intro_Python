import random
import sys

stake = 10
goal = 40
trials = 1000

bets = 0
wins = 0

for t in range (0, trials):
    # run one experiment
    cash = stake
    while (cash > 0) and (cash < goal):
        bets += 1
        if random.randrange(0,2)==0:
            cash -= 1
        else:
            cash += 1
    if cash == goal:
        wins += 1

win_prob = wins/trials
Avgbets = bets/trials
print(win_prob)
print(Avgbets)


