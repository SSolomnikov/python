import sys

previous_word = None
counter = 0

for line in sys.stdin:
    word = line.strip().split(',')

    if previous_word:
        if previous_word == word:
            counter +=1
        else:
            print(previous_word,counter)
            previous_word = word
            counter = 1
    else: 
        previous_word = word
        counter +=1
    
    previous_word = word

print(previous_word,counter)