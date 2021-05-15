import random
import plotly.figure_factory as ff
import statistics
diceResult = []
for i in range (0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceResult.append(dice1 + dice2)
mean = sum(diceResult)/len(diceResult)
median  = statistics.median(diceResult)
mode = statistics.mode(diceResult)
standardDeviation = statistics.stdev(diceResult)
fig = ff.create_distplot([diceResult],["Result"], show_hist = False)
print(mean)
print(mode)
print(median)
print(standardDeviation)
fig.show()
