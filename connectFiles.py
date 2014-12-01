'''
for line in files:
    add spaces to match the longest line in the LEFT file
    add blank lines to make the files have the same HEIGHT
    add the rows together, so the LAST row matches
        maybe make an option for this
'''

from sys import argv

script, file1, file2, outputFile = argv

file1 = open(file1, 'r')
file2 = open(file2, 'r')

outputFile = open(outputFile, 'w')

longestLineFile1 = 0
linesFile1 = 0
linesFile2 = 0

linesList1 = list()
linesList2 = list()

# for the left file, count the lines and add the lines to a list
#
# also determine the length of the longest line
for line in file1:
    linesFile1 = linesFile1 + 1
    line = line.rstrip("\r\n")
    #line = line[0]
    if len(line) > longestLineFile1:
        longestLineFile1 = len(line)
    linesList1.append(line)

# count the lines in the second file, and add them to a list
for line in file2:
    linesFile2 = linesFile2 + 1
    line = line.rstrip("\r\n")
    #line = line[0]
    linesList2.append(line)

# if there are more lines in the second file,
# add blank lines to the first file
#
# otherwise, we will connect the files so the bottom lines match
if linesFile2 > linesFile1:
    difference = linesFile2 - linesFile1
    linesList1.reverse()
    for i in range(0, difference):
        linesList1.append("")
    linesList1.reverse()
    linesFile1 = linesFile2

# connect the files, line-by-line
for i in range(0, linesFile1):
    #if len(linesFile1[0]) < longestLineFile1:
    # unnecessary because otherwise it will be zero:
    line = linesList1[0] + " "*(longestLineFile1 - len(linesList1[0]))
    if linesFile1 == linesFile2:
        line = line + linesList2[0]
        linesList2.remove(linesList2[0])
        linesFile2 = linesFile2 - 1
    linesFile1 = linesFile1 - 1
    linesList1.remove(linesList1[0])
    outputFile.write(line)
    outputFile.write('\n')

file1.close()
file2.close()
outputFile.close()
