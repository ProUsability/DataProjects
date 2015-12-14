'''
Extract survey data from a CSV file and uploads it into a local MySQL database for analysis with R.

Written by Thomas Lennig
Started December 7th, 2015
'''

# temporary mac mysql db pw or85ef;irF_%

import MySQLdb
import csv
import datetime
from user_agents import parse

# connects to MySQL database, creates table for data upload
connection = MySQLdb.connect(host='localhost',user='root',passwd='admin',db='test')
cursor = connection.cursor()

command ='''DROP TABLE IF EXISTS testtable1'''
cursor.execute(command)

command ='''CREATE TABLE testtable1(
row int unsigned not null auto_increment,
participant int unsigned not null,
primaryBrowser varchar(20),
operatingSystem varchar(20),
primary key (row)) engine=innodb;
'''
cursor.execute(command)

# function checks a dictionary for a value, increments the value or initializes it into the dict with a count of 1
def dictionaryIncrementer(value, dictionary):
    if value not in dictionary:
        dictionary[value] = 1
    else:
        dictionary[value] += 1    
        
# need function to parse the first two lines of the CSV file to determine the questions and answer options

count = 0
notPC = 0
bots = 0
notPrimary = 0
totalSecondsSpent = 0
sampleSize = 0

ffxBrowserVersion = {}
crBrowserVersion = {}

ffxPlugins = {}
crPlugins = {}

crOS = {}
ffxOS = {}

# Input filepaths

# MacbookAir Filepath
#pfile = "//Users//thomas//Desktop//VideoSurveyAll.csv"

# Desktop Filepath
pfile = "C:\\Users\\G1_SNIPA\\Desktop\\DataProjects\\VideoSurveyAll.csv"

with open(pfile, 'rb') as csvfile:
    lines = csv.reader(csvfile, delimiter=',', quotechar='"')
    
    
    for line in lines:
        print line
        print len(line)
        
        print count
        count += 1        
        
        # Need function for reading in the first two lines to determine the questions and answer options.
        if count == 1:
            continue
        elif count == 2:
            continue
        else:
            # user_agent library for deciphering strings
            user_agent_ext = parse(line[5]) # parses using data from "User Agent Extended" field
            
            if user_agent_ext.is_bot: # Skips if it's a bot
                bots += 1
                continue
            
            if user_agent_ext.is_pc is False: # Skips if not on desktop
                notPC += 1
                continue

            browserData = user_agent_ext.browser
            
            prefBrowser = line[9] # gets the preferred (primary) browser
            
            if browserData.family != prefBrowser: # Skips if current browser is not primary broser
                notPrimary += 1
                continue                
            
            operatingSystem = user_agent_ext.os # gets the operating system information
            
            # calculate time spent per user
            started = datetime.datetime.strptime(line[2], '%m/%d/%Y %H:%M:%S') # converts start time to datetime object
            finished = datetime.datetime.strptime(line[3], '%m/%d/%Y %H:%M:%S') # converts end time to datetime object
            delta = finished - started # calculates difference between start & finish time
            secondsSpent = delta.seconds # converts time difference to seconds
            totalSecondsSpent += secondsSpent # tallies total seconds spent by all participants
            
            # gets browser versions            
            version = browserData.version_string
            
            # gets operating system name + version 
            osFamily = operatingSystem.family
            
            # count plugins for both browsers
            plugins = line[17].split(',')
            
            if prefBrowser == 'Chrome':
                dictionaryIncrementer(version,crBrowserVersion) # counts browser version
                dictionaryIncrementer(osFamily,crOS) # counts operating system family
                for plugin in plugins:
                    dictionaryIncrementer(plugin,crPlugins) # counts plugins
            else: # if prefBrowser == 'Firefox':
                dictionaryIncrementer(version,ffxBrowserVersion)
                dictionaryIncrementer(osFamily,ffxOS)
                for plugin in plugins:
                    dictionaryIncrementer(plugin,ffxPlugins)
                
            
            
            
            # Find the longest data value per column to make uploading to mysql easier
            
            sampleSize += 1 # tracks total eligible participants
            
            print browserData
            

print 'All done!'










    
    
    