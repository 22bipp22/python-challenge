#PyBank Homework
import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")

budget_date = []
profit_loss = []
great_inc_date = str
greatest_increase = 0
great_dec_date = str 
greatest_decrease = 0
profit_change_total = 0
budget_total = 0
profit_change = 0

#initialize "previous row" with the first profit/loss value
first_row = "yes"


with open(csvpath) as csvfile:

    budget_list = csv.reader(csvfile, delimiter = ",")
    
    csv_header = next(budget_list)

    print(f"CSV Header: {csv_header}")

    for row in budget_list:
        budget_date.append(row[0])
        profit_loss.append(row[1])

        #running total of all of the profit/losses
        budget_total = budget_total + int(row[1])

        #current row profit/loss amount
        budget_amount = int(row[1])
        
        #If this is the first row, save the profit/loss amount to the previous row field
        if first_row == "yes":
            
            previous_row = budget_amount
            first_row = "no"

        #Subtract the previous profit/loss value from the current p/l value to get the profit change amount and add it to the total change
        else:

            profit_change = int(budget_amount) - int(previous_row)
            profit_change_total += profit_change
                
            previous_row = budget_amount

        #Looking for the date with the greatest p/l increase
        if profit_change > greatest_increase:
            greatest_increase = profit_change
            great_inc_date = row[0]

        #Looking for the date with the greatest p/l decrease
        if profit_change < greatest_decrease:
            greatest_decrease = profit_change
            great_dec_date = row[0]
   
    
    #final calculations for display    
    total_months = len(budget_date)
    average_change = round(profit_change_total/(total_months - 1),2)
    
#Display results in terminal
print("Financial Analysis")
print("-------------------------------")
print(f"Total Months: {total_months}")   
print(f"Total: ${budget_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {great_inc_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {great_dec_date} (${greatest_decrease})")
        
#Print results to a text file
output_file = os.path.join("Analysis","Financial_Summary.txt")

with open(output_file, 'w') as textfile:
    textfile.writelines(f'Financial Analysis \n-------------------------- \nTotal Months: {total_months} \nTotal: ${budget_total} \nAverage Change: ${average_change} \nGreatest Increase in Profits: {great_inc_date} (${greatest_increase}) \nGreatest Decrease in Profits: {great_dec_date} (${greatest_decrease})') 
   
   

    
    

    
    