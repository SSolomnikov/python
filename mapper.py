#открываем файл
#with open(file, encoding ='utf-8') as f:
#mapper

import sys

f=sys.stdin

    list_pre = [] 
    for i in f.readlines()[1:]:
        list_pre.append(i.strip().split(','))

    dict_word_counter = {}
    list_words = []
    
    for line in list_pre:
        a = line[0].split(' ')
        for word in a:
            list_words.append(word)
            print(word)