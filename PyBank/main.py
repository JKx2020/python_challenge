##PyBank

#import CSV module
import csv

#create and open txt file we want to write to
pybankoutput = open("pybanksummary.txt", 'w')

#Print the title of the analysis to git bash and txt file
pybankoutput.write("Financial Analysis\n")
pybankoutput.write("-------------------------------\n")

print("Financial Analysis")
print("-------------------------------")


##1. Count number of months included
#create variables and lists to hold calculations
months = 0
change = 0
profitchange = []
netpl = 0
periods = []

#read through the lines of the CSV and create an object for the data
with open("budget_data.csv","r") as budgetfile:
    budgetreader = csv.reader(budgetfile, delimiter=",")
    
    #read the header row
    header = next(budgetreader) 
    first_row = next(budgetreader)
    
    #create variable for first pl value & add to the profits list
    firstvalue = int(first_row[1])
    firstdate = (first_row[0])

    netpl += firstvalue
    periods.append(firstdate)
    
    #increase months # for first value month
    months += 1
    
    
    #count the rows in the file after the header
    for row in budgetreader:
    
        #calculate total months
        months += 1

        #calculate changes between first and second value and add to list of changes and add the date to the list dates
        secondvalue = int(row[1])
        
        change = float(secondvalue) - float(firstvalue)
        firstvalue = int(row[1])
        
        profitchange.append(change)
        periods.append(row[0])
        
        #calculate total net p&l calculation
        netpl = netpl + int(row[1])
        
        #average changes over the period
        avg_change = sum(profitchange)/len(profitchange)
        avg_change = round(avg_change, 2)
  
#merging two lists into a dictionary so we can reference dates to the changes
keys = periods[1:]
values = profitchange


periods_profitchange = dict(zip(keys, values))

#find max monthly change in profits
max_profitchangedate = max(periods_profitchange, key=periods_profitchange.get)
maxprofit = max(profitchange)
maxprofit = round(maxprofit)

#find min monthly change in profits
min_profitchangedate = min(periods_profitchange, key=periods_profitchange.get)
minprofit = min(profitchange)
minprofit = round(minprofit)
        
        
##print results
#total months
print(f'Total Months: {months}')
pybankoutput.write(f'Total Months: {months}\n')

#total P&L
print(f'Total: ${netpl}')
pybankoutput.write(f'Total: ${netpl}\n')

#Average change over whole period
print(f'Average Change: ${avg_change}')
pybankoutput.write(f'Average Change: {avg_change}\n')

#Greatest profit increase over the entire period
print(f'Greatest Increase in Profits: {max_profitchangedate} (${maxprofit})')
pybankoutput.write(f'Greatest Increase in Profits: {max_profitchangedate} (${maxprofit})\n')

#Least profit increase over the entire period
print(f'Greatest Decrease in Profits: {min_profitchangedate} (${minprofit})')
pybankoutput.write(f'Greatest Decrease in Profits: {min_profitchangedate} (${minprofit})\n')






