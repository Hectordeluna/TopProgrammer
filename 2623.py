

word = list(raw_input())

word1 = word[:len(word)/2 - 1:-1]
word2 = word[len(word)/2 - 1::-1]

final = ""
print (final.join(word2 + word1))