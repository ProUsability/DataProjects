# MacbookAir Filepath
#pfile = "//Users//thomas//Desktop//VideoSurveyAll.csv"

# Desktop Filepath
pfile = "C:\\Users\\G1_SNIPA\\Desktop\\DataProjects\\VideoSurveyAll.csv"


import csv

# library for parsing out user_agent data
from user_agents import parse

count = 0
notPC = 0
bots = 0
notPrimary = 0

# Input file
pfile
with open(pfile, 'rb') as csvfile:
    lines = csv.reader(csvfile, delimiter=',', quotechar='"')
    
    
    for line in lines:
        print line
        print len(line)
        
        print count
        count += 1        
        
        # Function for reading in the first two lines of data to determine the questions and answer options.
        if count == 1:
            continue
        elif count == 2:
            continue
        else:
            # user_agent library for deciphering strings
            # user_agent = parse(line[4]) # parses using data from "User Agent" field
            user_agent_ext = parse(line[5]) # parses using data from "User Agent Extended" field
            
            if user_agent_ext.is_bot: # Skips if it's a bot
                bots += 1
                continue
            
            if user_agent_ext.is_pc is False: # Skips if not on desktop
                notPC += 1
                continue

            browserData = user_agent_ext.browser
            
            if browserData.family != line[9]: # Skips if current browser is not primary broser
                notPrimary += 1
                continue                
            
            
            # calculate time spent per user
            
            # count versioning for both browsers
            
            # Find the longest data value per column to make uploading to mysql easier
            
            
            print browserData
            
            
        












    
    
    