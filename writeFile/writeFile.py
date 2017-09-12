#baby steps

wordList = ["red", "blue", "green", "mauve", "fuscia"]

#wordList.append("purple") # No can do on tuples

fileOut = "output.txt"
file = open(fileOut, "w")

# write a string
file.writelines(wordList)
file.write("\n\nFormatted text:\n")

for word in wordList:
    print >> file, "\t%s is the color" % word

file.close()
