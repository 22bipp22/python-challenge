import os
import csv

csvpath = os.path.join("Resources","budget_data.csv")

budget_date = []
profit_loss = []
budget_total = 0
greatest_increase = 0
greatest_decrease = 0
change_amount = []



with open(csvpath) as csvfile:

    budget_list = csv.reader(csvfile, delimiter = ",")
    
    csv_header = next(budget_list)

    print(f"CSV Header: {csv_header}")

    for row in budget_list:
        budget_date.append(row[0])
        profit_loss.append(row[1])

        budget_total = budget_total + int(row[1])

        budget_amount = int(row[1])

        if budget_amount > greatest_increase:
            greatest_increase = budget_amount

        if budget_amount < greatest_decrease:
            greatest_decrease = budget_amount

    
    ##???? need to loop through profit_loss and subtract previous from current, then add them all and get the average ????
    for row in profit_loss:
        
    #calculate total months 
    total_months = len(budget_date) 
    print(profit_loss[0])
    
    print(total_months)
    print(budget_total)
    print(greatest_increase)
    print(greatest_decrease)
