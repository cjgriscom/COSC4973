file="input.txt"
wordList=[]
wordCount=0

file = open(file, "rU")

for line in file:
    for word in line.split():
        wordList.append(word)
	wordCount+=1

print(wordList)
print("Word count is", wordCount)
