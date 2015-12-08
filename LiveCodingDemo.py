# MacbookAir Filepath
pfile = "//Users//thomas//Desktop//Mozilla2.txt"


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


#'c' || 'n' 'a'

wordsDict = {}
longestWord = 0

#count of unique words
for theString in lines:
    myString = theString
    myString = myString.strip("\n")
    #print myString
    words = myString.split(" ")
    for term in words:
        
        if len(term) > longestWord:
            longestWord = len(term)
        
        if term not in wordsDict:
            wordsDict[term] = 1
        else:
            wordsDict[term] += 1
    #print words
    


#count of unique words
print 'The number of unique words is: ' + str(len(wordsDict))

#maximum length of a word
print 'The longest word is: ' + str(longestWord)


print "cool!"

