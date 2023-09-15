import os
import csv

#set path for file
budget_data_csv = os.path.join("Resources" , "budget_data.csv")
#set the output of the text file
text_path = os.path.join("analysis" , "output.txt")

#Set variables
total_months = 0
total_revenue = 0
revenue = []
previous_revenue = 0
month_of_change = []
revenue_change = 0
greatest_decrease = ["", 9999999]
greatest_increase = ["", 0]
revenue_change_list = []
revenue_average = 0


#open the csv file
with open(budget_data_csv,"r") as csvfile:  
    csvreader = csv.reader(csvfile,delimiter=",") 
    header = next(csvreader)

    #Loop through to find total months
    for row in csvreader:

        #Count the total of months
        total_months += 1 
        #Calculate the total revenue over the entire period
        total_revenue = int(total_revenue )+ int(row[1])
        
        #Calculate the average change in revenue between months over the entire period
        revenue_change = float(row[1])- previous_revenue 
 
        #print("Revenue Change:", revenue_change)
        previous_revenue = float(row[1])
        #print("Previous Revenue:", previous_revenue)
        revenue_change_list = revenue_change_list + [revenue_change]
        #print("Revenue Change List:", revenue_change_list)
        month_of_change = [month_of_change] + [row[0]]
        #print("Month of Change", month_of_change)
       

        #The greatest increase in revenue (date and amount) over the entire period
        if revenue_change>greatest_increase[1]:
            greatest_increase[1]= revenue_change
            greatest_increase[0] = row[0]

        #The greatest decrease in revenue (date and amount) over the entire period
        if revenue_change<greatest_decrease[1]:
            greatest_decrease[1]= revenue_change
            greatest_decrease[0] = row[0]
    revenue_average = sum(revenue_change_list)/len(revenue_change_list)

msg_output = "Financial Analysis\n"  
msg_output +=  "---------------------\n"
msg_output += "Total Months: %d\n" % total_months 
msg_output += "Total Revenue: $%d\n" % total_revenue 
msg_output +=  "Average Revenue Change $%d\n" % revenue_average 
msg_output += "Greatest Increase in Revenue: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1])
msg_output += "Greatest Decrease in Revenue: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]) 
print (msg_output)  


#write changes to csv
with open(text_path, 'w') as file:
    file.write (msg_output) 
    
    