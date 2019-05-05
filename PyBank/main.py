import os
import csv 
profit_losses = 0
total = 0
difference = 0
budget = []
tot_months = []
month = 0


csvpath = os.path.join('Resources/budget_data.csv')

with open( csvpath, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    #for row in csv_reader:
        #print(row)
    
    for row in csv_reader:
        budget.append(row)
        
    budget = budget[1:]

# The total number of months included in the dataset

    for row in budget:
        month += 1
    print("Financial Analysis") 
    print("-----------------------------")
    print("-----------------------------")    
    print("Total Months:"+" "+str(month))
    print("-----------------------------")
       


    
# The net total amount of "Profit/Losses" over the entire period
    for row in budget:
        profit_loss = row[1]
        total += int(profit_loss)
        
    print("Total"+" " +str(total))
    print("-----------------------------")



# The average of the changes in "Profit/Losses" over the entire period
    for index in range(month-1):
    
        difference += int(budget[index + 1][1]) - int(budget[index][1])

    average = (difference / (month - 1))




    print("Average Change"+" "+ str(average))
    print("-----------------------------")
        

# The greatest increase and decrease in profits (date and amount) over the entire period
    


       
txt = open("Financial_Analysist.txt", "a")
print("Financial Analysis", file=txt)
print ("-------------------------------", file=txt)
print("Total Months:"+" "+str(month), file=txt)
print ("Total"+" " +str(total), file=txt)
print("Average Change"+" "+ str(average), file=txt)
