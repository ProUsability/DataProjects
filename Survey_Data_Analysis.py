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



# Function for reading in the first two lines of data to determine the questions and answer options.

# Find the longest data value per column to make uploading to mysql easier

