

word = list(raw_input())

if len(word) % 2 == 0:
    word1 = word[:len(word)/2 - 1:-1]
    word2 = word[len(word)/2 - 1::-1]
else:
    word1 = word[:len(word)/2:-1]
    word2 = word[len(word)/2 - 1::-1]

final = ""
if len(word) % 2 == 0:
    print (final.join(word2 + word1))
else:
    print (final.join(word2) + str(word[len(word) / 2]) + final.join(word1))