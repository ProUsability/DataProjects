# MacbookAir Filepath
#pfile = "//Users//thomas//Desktop//VideoSurveyAll.csv"

# Desktop Filepath
pfile = "C:\\Users\\G1_SNIPA\\Desktop\\DataProjects\\VideoSurveyAll.csv"


import csv

# library for parsing out user_agent data
from user_agents import parse

# Input file
fnamemaster = pfile
fmaster = open(fnamemaster,'r')

# Read in input file
lines = fmaster.readlines()
fmaster.close()

#print lines


length = len(lines)
    
# length of the document    
print "This document has  " +  str(length) + "  lines"


# Function for reading in the first two lines of data to determine the questions and answer options.

# user_agent library for deciphering strings

# Find the longest data value per column to make uploading to mysql easier

# calculate time spent per user

count = 0

for line in lines:
    # print line
    row = line.split(",")
    count += 1
    print row
    print str(len(row))
    
    if count == 0 or count == 1:
        continue
    
    
    
    