import re

testString = 'tawanatawanacawanacawana'

nas = re.findall("na", testString)
cas = re.findall("ca", testString)

print "na found: " + str(len(nas)) + " times"
print "ca found: " + str(len(cas)) + " times"