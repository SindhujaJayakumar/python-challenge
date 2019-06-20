import os
import csv

csvpath = os.path.join("C:/Bootclassactivities/SMUDAL201905DATA5/02-Homework/03-Python/Instructions/PyPoll/Resources/election_data.csv")

candidate = []
votes = []
total_votes = 0
count = 0
khan = 0
total_candidates_with_votes = 0
i = 0
votes_candidate = 0
percent = 0
winner_percent = 0

with open(csvpath, newline="") as csvfile:
   csv_reader = csv.reader(csvfile, delimiter=",")

   csv_header = next(csvfile)

   total_votes  = len(list(csv.reader(open(csvpath))))

   for row in csv_reader:
       name = row[2]
       votes.append(name)
       if name in candidate:
           continue
       else:
           candidate.append(name)

   print(f"Election Results")
   print(f"----------------------------")
   print(f"Total Votes: {total_votes}")
   print(f"----------------------------")

   total_candidates_with_votes = len(candidate)

   while i < total_candidates_with_votes:
       name_aux = candidate[i]
       votes_candidate = votes.count(name_aux)
       percent = round((votes_candidate / total_votes * 100),2)
       
       if percent > winner_percent:
           winner_percent = percent
           winner_name = name_aux

       print(f"{name_aux}: {percent}% ({votes_candidate})")
       i = i + 1

   print(f"----------------------------")
   print(f"Winner: {winner_name}")
   print(f"----------------------------")

output_path = os.path.join ("Election_Results.csv")

with open(output_path, 'w', newline='') as csvfile:

   # csvwriter
   csvwriter = csv.writer(csvfile)

   #second row
   

   csvwriter.writerow(["Election Results"])
   csvwriter.writerow(["--------------------------------------"])
   csvwriter.writerow([f"Total Votes: {total_votes}"])
   csvwriter.writerow(["--------------------------------------"])
   
   
   total_candidates_with_votes = len(candidate)

   while i < total_candidates_with_votes:
       name_aux = candidate[i]
       votes_candidate = votes.count(name_aux)
       percent = round((votes_candidate / total_votes * 100),2)
       
       if percent > winner_percent:
           winner_percent = percent
           winner_name = name_aux

       csvwriter.writerow([f"{name_aux}: {percent}% ({votes_candidate})"])
       i = i + 1

   csvwriter.writerow(["--------------------------------------"])
   csvwriter.writerow([f"Winner: {winner_name}"])
   csvwriter.writerow(["--------------------------------------"])   
