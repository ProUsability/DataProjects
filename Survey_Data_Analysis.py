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
connection.autocommit(True)
cursor = connection.cursor()

# cleans up (removes) previous table (if it exists).
command = "DROP TABLE IF EXISTS testtable1"
cursor.execute(command)

# creates new table
command = ("CREATE TABLE testtable1("
           + "row int unsigned not null auto_increment, "
           + "participant int unsigned not null, "
           + "secondsTOT int unsigned not null, "
           + "primaryBrowser varchar(20), "
           + "browserVersion varchar(20), "
           + "operatingSystem varchar(20), "
           + "pluginsReported int unsigned not null, "
           + "pluginsCounted int unsigned not null, "
           + "browserSwitchFrequency varchar(20), "
           + "youtubeFrequency varchar(10), "
           + "netflixFrequency varchar(10), "
           + "vimeoFrequency varchar(10), "
           + "funnyOrDieFrequency varchar(10), "
           + "facebookFrequency varchar(10), "
           + "yahooFrequency varchar(10), "
           + "liveleakFrequency varchar(10), "
           + "huluFrequency varchar(10), "
           + "primary key (row)) engine=innodb;"
           )
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
countIntoMySQL = 0
pluginCountDisconnect = 0

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
        #print len(line)
        
        count += 1
        #print count
                
        '''
        MAJOR MISSING PART:
        #####################################################################################################################
        # Need function that reads in the first two lines then determines the questions, answer options, and their indices. #
        #####################################################################################################################
        
        '''
        
        if count == 1:
            continue
        elif count == 2:
            
            youtubeIndex = line.index("YouTube")
            netflixIndex = line.index("Netflix")
            vimeoIndex = line.index("Vimeo")
            funnyOrDieIndex = line.index("Funny Or Die")	
            facebookIndex = line.index("Facebook")
            yahooIndex = line.index("Yahoo")
            liveleakIndex = line.index("Liveleak")
            huluIndex = line.index("Hulu")
            
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
            
            # gets current browser data from user agents
            browserData = user_agent_ext.browser
            
            prefBrowser = line[9] # gets the preferred (primary) browser
            
            if browserData.family != prefBrowser: # Skips if current browser is not primary broser
                notPrimary += 1
                continue                
            
            repNumPlugins = int(line[16]) # gets the number of plugins reported in the csv file
            
            browserSwitchFrequency = line[18] # gets 5. How often do you use another browser (e.g. [question("value"), id="83"], Edge, Safari, etc) when you want to watch videos on this computer?
            
            
            operatingSystem = user_agent_ext.os # gets the operating system information
            
            # calculate time spent per user
            started = datetime.datetime.strptime(line[2], '%m/%d/%Y %H:%M:%S') # converts start time to datetime object
            finished = datetime.datetime.strptime(line[3], '%m/%d/%Y %H:%M:%S') # converts end time to datetime object
            delta = finished - started # calculates difference between start & finish time
            secondsSpent = delta.seconds # converts time difference to seconds
            totalSecondsSpent += secondsSpent # tallies total seconds spent by all participants
            
            participant = int(line[1])
            
            # gets browser versions            
            browserVersion = browserData.version_string
            
            # gets operating system name + version 
            osFamily = str(operatingSystem.family)
            
            # gets plugins for both browsers
            plugins = line[17].split(',')
            countNumPlugins = len(plugins) #counts number of plugins reported in csv file
            
            if countNumPlugins != repNumPlugins:
                print "It's a trap!"
                pluginCountDisconnect += 1
                #break
            
            if prefBrowser == 'Chrome':
                dictionaryIncrementer(browserVersion,crBrowserVersion) # counts browser version
                dictionaryIncrementer(osFamily,crOS) # counts operating system family
                for plugin in plugins:
                    dictionaryIncrementer(plugin,crPlugins) # counts plugins
            else: # if prefBrowser == 'Firefox':
                dictionaryIncrementer(browserVersion,ffxBrowserVersion)
                dictionaryIncrementer(osFamily,ffxOS)
                for plugin in plugins:
                    dictionaryIncrementer(plugin,ffxPlugins)
                
            
            youtubeFrequency = line[youtubeIndex]
            netflixFrequency = line[netflixIndex]
            vimeoFrequency = line[vimeoIndex]
            funnyOrDieFrequency = line[funnyOrDieIndex]
            facebookFrequency = line[facebookIndex]
            yahooFrequency = line[yahooIndex]
            liveleakFrequency = line[liveleakIndex]
            huluFrequency = line[huluIndex]            
            
            # Find the longest data value per column to make uploading to mysql easier
            
            sampleSize += 1 # tracks total eligible participants
            

            # mysql upload template for data insertion
            insertCommand = ("INSERT INTO testtable1 SET "
            + "participant=%s,"
            + "secondsTOT=%s,"
            + "primaryBrowser='%s',"
            + "browserVersion='%s',"
            + "operatingSystem='%s',"
            + "pluginsReported=%s, "
            + "pluginsCounted=%s, "
            + "browserSwitchFrequency='%s', "
            + "youtubeFrequency='%s',"
            + "netflixFrequency='%s',"
            + "vimeoFrequency='%s',"
            + "funnyOrDieFrequency='%s',"
            + "facebookFrequency='%s',"
            + "yahooFrequency='%s',"
            + "liveleakFrequency='%s',"
            + "huluFrequency='%s'"
            +";")
            
            # populates mysql template with data for row insertion            
            insertCommand = insertCommand % (participant,
                                             secondsSpent,
                                             prefBrowser,
                                             browserVersion,
                                             osFamily,
                                             repNumPlugins,
                                             countNumPlugins,
                                             browserSwitchFrequency,
                                             # Video watching services frequency
                                             youtubeFrequency,
                                             netflixFrequency,
                                             vimeoFrequency,
                                             funnyOrDieFrequency,	
                                             facebookFrequency,
                                             yahooFrequency,
                                             liveleakFrequency,
                                             huluFrequency,                                             
                                             )
            
            # Tries to upload row or catches and prints error
            try:
                cursor.execute(insertCommand)
                countIntoMySQL += 1
            except Exception as error:
                print error
            
            #print browserData
            


print 'Inserted into MySQL: ' + str(countIntoMySQL)
print 'Detected ' + str(pluginCountDisconnect) + ' disconnects in the number of plugins reported:listed.'
print 'All done!'










    
    
    