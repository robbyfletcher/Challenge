def wordListConfig(wordList):      # Loads the word list, sorts it, and
     wordsFile = open('randomlist.txt','r')
     for line in wordsFile:
          wordList.append(line.rstrip())
     wordList.sort()

def writeToJS(wordList):
     jsFile = open('randomlist.js','w')
     jsFile.write('var wordList = [\n')
     for line in wordList:
          jsFile.write('"' + line + '",\n')
     jsFile.write('];')
     jsFile.close()

wordList = []
wordListConfig(wordList)
writeToJS(wordList)
