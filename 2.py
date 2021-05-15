import pandas as pd
import statistics
import csv

df = pd.read_csv("height-weight.csv")
heightList = df["Height(Inches)"].tolist()
median = statistics.median(heightList)
mode = statistics.mode(heightList)
standardDeviation = statistics.stdev(heightList)
mean = statistics.mean(heightList)
firstStart, firstEnd, secondStart, secondEnd, thirdStart, thirdEnd = mean-standardDeviation, mean+standardDeviation, mean-2*standardDeviation, mean+2*standardDeviation, mean-3*standardDeviation, mean+3*standardDeviation
firstList=[result for result in heightList if result > firstStart and result<firstEnd]
secondList=[result for result in heightList if result > secondStart and result<secondEnd]
thirdList = [result for result in heightList if result > thirdStart and result<thirdEnd]
firstPercentage = len(firstList)*100/len(heightList)
secondPercentage = len(secondList)*100/len(heightList)
thirdPercentage = len(thirdList)*100/len(heightList)

print(firstPercentage)
print(secondPercentage)
print(thirdPercentage)

