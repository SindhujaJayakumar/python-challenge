import os
import csv

#csvpath = os.path.join(".", "Resources", "budget_data.csv") # look up file from relative path
csvpath = os.path.join("C:/Bootclassactivities/SMUDAL201905DATA5/02-Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv")

profit = 0
loss = 0
amount = 0
total = 0
months = 0

prev_month = 0
incdec = 0
great_inc = 0
great_dec = 0
sum_incdec = 0
average = 0
index = 0

with open(csvpath, newline="") as csvfile:
   csv_reader = csv.reader(csvfile, delimiter=",")

   csv_header = next(csvfile)

   for row in csv_reader:
       amount = float(row[1])
       
       if amount > 0:
           profit = profit + amount
       else:
           loss = loss + amount

       incdec = amount - prev_month
       if index != 0:
           sum_incdec = sum_incdec + incdec

       if (incdec > 0) and (incdec > great_inc):
           great_inc = incdec
           month_row_inc = row[0]
       elif (incdec < 0) and (incdec < great_dec):
           great_dec = incdec
           month_row_dec = row[0]

       prev_month = amount
       index +=1

   total = profit + loss

   months = len(list(csv.reader(open(csvpath))))
   # Check how many months are in the file not considering the header
   months = months - 1

   # Calculate the average dividing the total of changes by the number of changes
   average = sum_incdec / (months - 1)

   print(f"Financial Analysis")
   print(f"-------------------")
   print(f"Total Months: {months}")
   print(f"Total: $ {total}")
   print(f"Average Change: $ {average}")
   print(f"Greatest Increase in Profits: {month_row_inc} ($ {great_inc})")
   print(f"Greatest Decrease in Profits: {month_row_dec} ($ {great_dec})")

output_path = os.path.join ("Financial_Analysis.csv")

# write mode
with open(output_path, 'w', newline='') as csvfile:

   # Initialize csv.writer
   csvwriter = csv.writer(csvfile)

   # second row


   csvwriter.writerow(["Financial Analysis"])
   csvwriter.writerow(["----------------------------"])
   csvwriter.writerow([f"Total Months: {months}"])
   csvwriter.writerow([f"Total: $ {total}"])
   csvwriter.writerow([f"Average Change: $ {average}"])
   csvwriter.writerow([f"Greatest Increase in Profits: {month_row_inc} ($ {great_inc})"])
   csvwriter.writerow([f"Greatest Decrease in Profits: {month_row_dec} ($ {great_dec})"])
