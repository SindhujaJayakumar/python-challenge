import csv
import os

csvpath = os.path.join("C:/Bootclassactivities/SMUDAL201905DATA5/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv")


#Variables for month and revenue data
months = []
revenue = []

#Read csv and parse data into lists
#Revenue list will be list of integers
with open(csvpath, 'r') as csvfile:
	csvread = csv.reader(csvfile)
	next(csvread)

	for row in csvread:
		months.append(row[0])
		revenue.append(int(row[1]))

#Find total months
total_months = len(months)

#Create greatest increase, decrease variabl;es and set them equal to the first revenue entry
#Set total revenue = 0
max_inc = revenue[0]
max_dec = revenue[0]
total_revenue = 0

#Loop through revenue indices and compare number to find greatest inc/dec
#Also add each revenue to total revenue
for r in range(len(revenue)):
	if revenue[r] >= max_inc:
		max_inc = revenue[r]
		max_inc_month = months[r]
	elif revenue[r] <= max_dec:
		max_dec = revenue[r]
		max_dec_month = months[r]
	total_revenue += revenue[r]

#Calculate average change in revenue
average_delta = round(total_revenue/total_months, 2)


#Set path for output file
output_path = os.path.join("C:/Bootclassactivities/GitExperiments/python-challenge/Outputpybank.txt")

#Opens the output destination in write mode and prints the summary
with open(output_path, 'w') as writefile:
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Total Months: ' + str(total_months) + '\n')
    writefile.writelines('Total Revenue: $' + str(total_revenue) + '\n')
    writefile.writelines('Average Revenue Change: $' + str(average_delta) + '\n')
    writefile.writelines('Greatest Increase in Revenue: ' + max_inc_month + ' ($' + str(max_inc) + ')'+ '\n')
    writefile.writelines('Greatest Decrease in Revenue: ' + max_dec_month + ' ($' + str(max_dec) + ')')

#Opens the output file in r mode and prints to Terminal
with open(output_path, 'r') as readfile:
	print(readfile.read())