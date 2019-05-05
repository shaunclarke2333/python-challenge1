import csv
import os
votes = 0
voter_id = []
country_id = []
candidate_id = []
candidate_votes = {}
total_votes = 0
names = 0
percentages = 0
vote = 0

csv_path = os.path.join("Resources/election_data.csv")

with open(csv_path, newline="") as csvfile:

    read_csv = csv.reader(csvfile, delimiter =",")
    csv_header = next(csvfile)
    for row in read_csv:
        v_id = row[0]
        country = row[1]
        candidate = row[2]
        voter_id.append(v_id)
        country_id.append(country)
        candidate_id.append(candidate)
        total_votes += 1

    # populate dictionry with total votes for each candidate
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
#print(candidate_votes)
print("Election Results")
print ("-------------------------------")
print("Total Votes:"+" "+str(total_votes))
print ("-------------------------------")
print("Percentages Won & Total Votes") 
print ("-------------------------------")    
working_list = zip(candidate_votes.values(), candidate_votes.keys())
for percent in working_list:
    names = (percent[1])
    percentages = (format((percent[0] /total_votes) * 100, '.3f'))
    vote = int(percent[0]) 
    print (f"{names} {percentages} ({vote})")
    #print(percentages)
    #print(str(percent[1])+":"+" "+str((percent[0] /total_votes) * 100)+" "+"(" +str(percent[0])+")")


new_list = (max(zip(candidate_votes.values(), candidate_votes.keys())))

print ("-------------------------------")    
print ("Winner: "+ new_list[1]) 

# write to txt file


txt = open("Election_Results.txt", "a")
print("Election Results", file=txt)
print ("-------------------------------", file=txt)
print("Total Votes:"+" "+str(total_votes), file=txt)
print ("-------------------------------", file=txt)
print("Percentages Won & Total Votes", file=txt) 
print ("-------------------------------", file=txt)    
print (f"{names} {percentages} ({vote})", file=txt)
print ("-------------------------------", file=txt)    
print ("Winner: "+ new_list[1], file=txt) 