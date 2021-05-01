# iport the stuff I need to do this
import os
import csv


#This calls the path from where I am currently at to get the cvs file after that I set all the variables I would need later
election_data_csv = os.path.join ("Resources","election_data.csv")
total_votes = 0
khan = 0
correy = 0
li = 0 
otooley = 0
winner = str

#This part defines the percentage function I will use later
def percentage(part,whole):
    percentage = 100 * int(part)/int(whole)
    return str(percentage) + "%"

#This opens the csv_file and seperates from the delimter selected in this case a comma
with open(election_data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")


    csv_header = next(csv_reader)
    #print(f"Header {csv_header}")

#I start the for loop here and go through each one using the variables I set earlier
    for row in csv_reader:
        total_votes +=1
        if "Khan" in row:
            khan +=  1
        if 'Correy' in row:
            correy +=  1
        if 'Li' in row: 
            li +=  1
        if "O'Tooley" in row:
            otooley += 1
        
    # This just lets me set something to the variable winner
    if khan > li and otooley and correy:
        winner= "Khan"
    if li > khan and otooley and correy:
        winner = "Li"
    if otooley > khan and li and correy:
        winner = "O'Tooley"
    if correy > khan and otooley and li:
        winner = "Correy"
    
    #Print that good stuff whole thing took me close to 6 hours, I do not know why looking back at it now it is easy
    print("Election Results")
    print("-----------------------")
    print(f"Total votes - {total_votes}")
    print("-----------------------")
    print(f"Khan - {percentage(khan,total_votes)}, {khan}")
    print(f"Correy - {percentage(correy,total_votes)}, {correy}")
    print(f"Li - {percentage(li,total_votes)}, {li}")
    print(f"O'Tooley - {percentage(otooley,total_votes)}, {otooley}")
    print("-----------------------")
    print(f"The winner is {winner} with {khan} votes and a percentage of {percentage(khan,total_votes)} get out of here O'tooley")
election_file = os.path.join("Analysis", "election_data.txt")
with open (election_file, "w") as outfile:
    outfile.write("Election Results('/n')")
    outfile.write("-----------------------/n")
    outfile.write(f"Total votes - {total_votes}/n")
    outfile.write("-----------------------/n")
    outfile.write(f"Khan - {percentage(khan,total_votes)}, {khan}/n")
    outfile.write(f"Correy - {percentage(correy,total_votes)}, {correy}/n")
    outfile.write(f"Li - {percentage(li,total_votes)}, {li}/n")
    outfile.write(f"O'Tooley - {percentage(otooley,total_votes)}, {otooley}/n")
    outfile.write("-----------------------/n")
    outfile.write(f"The winner is {winner} with {khan} votes and a percentage of {percentage(khan,total_votes)} get out of here O'tooley/n")



