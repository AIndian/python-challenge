import os
import csv

#initiating the lists to be used
months = []
budget = []

#reading and importing file data to lists to be used
datapath = os.path.join('Resources','budget_data.csv')
with open(datapath) as csvfile:
    bankData = csv.reader(csvfile)
    next (bankData)
    for row in bankData:
        months.append(row[0])
        budget.append(int(row[1]))

#calculations for the results
totMonths = len(months)
totBud = sum(budget)
maxLoss = min(budget)
maxProfit = max(budget)
averageChange = sum(budget)/len(budget)
dateLoss = months[budget.index(maxLoss)]
dateProfit = months[budget.index(maxProfit)]

#writing results to file
spacer = "----------------------------"
outputFile = os.path.join('Analysis','budgetResults.txt')
with open(outputFile, 'w', newline = '') as res:
    res.write(f'Financial Analysis\n{spacer}\nTotal Months: {totMonths} \nTotal: ${totBud} \nAverage Change: ${averageChange:.2f} \nGreatest Increase in Profits: {dateProfit} (${maxProfit}) \nGreatest Decrease in Profits: {dateLoss} (${maxLoss})')

#printing results to console
with open(outputFile) as results:
    print(results.read())   