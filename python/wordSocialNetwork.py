def wordListConfig(wordList):      # Loads the word list, sorts it, and
     wordsFile = open('../randomlist.txt','r')
     for line in wordsFile:
          wordList.append(line.rstrip())
     wordList.sort()

def findFriends(word, friends):
     friends = []
     for line in wordList:
          if len(line) == len(word):
               diff = 0
               for i in range(0,len(line)):
                    if word.lower()[i] != line.lower()[i]:
                         diff += 1
               if diff == 1:
                    if friends.count(line) == 0:
                         friends.append(line)
          elif abs(len(line) - len(word)) < 2:
               if len(line) < len(word):
                    shorter = line
                    longer  = word
               else:
                    shorter = word
                    longer  = line
               diff = 0
               for i in range(0,len(shorter)):
                    if shorter.lower()[i] != longer.lower()[i]:
                         if shorter.lower()[i] != longer.lower()[i+1]:
                              diff += 1
               if diff < 1:
                    if friends.count(line) == 0:
                         friends.append(line)
     print('')
     print('Friends of ' + word + ':')
     for friend in friends:
          print(friend)

def findSocialNetwork(word, socialNetwork):
     for line in wordList:
          if len(line) == len(word):
               diff = 0
               for i in range(0,len(line)):
                    if word.lower()[i] != line.lower()[i]:
                         diff += 1
               if diff == 1:
                    if socialNetwork.count(line) == 0:
                         socialNetwork.append(line)
                         findSocialNetwork(line, socialNetwork)
          elif abs(len(line) - len(word)) < 2:
               if len(line) < len(word):
                    shorter = line
                    longer  = word
               else:
                    shorter = word
                    longer  = line
               diff = 0
               for i in range(0,len(shorter)):
                    if shorter.lower()[i] != longer.lower()[i]:
                         if shorter.lower()[i] != longer.lower()[i+1]:
                              diff += 1
               if diff < 1:
                    if socialNetwork.count(line) == 0:
                         socialNetwork.append(line)
                         findSocialNetwork(line, socialNetwork)

wordList = []
socialNetwork = []
friends = []
wordListConfig(wordList)

word = raw_input("Hi! Enter a word to find its social network: ")

findSocialNetwork(word, socialNetwork)
if len(socialNetwork) != 0:
     print('')
     print('The social network for ' + word + ":")
     for friend in socialNetwork:
          print(friend)
     findFriends(word, friends)
     for friend in socialNetwork:
          findFriends(friend, friends)
else:
     print("")
     print(":(")
     print("")
     print("We're sorry, but that word is not in this social network.")
