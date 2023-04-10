def count_words(word):
    wordlist = word.split()
    wordq={}
    for i in wordlist:
        if i in wordq:
            wordq[i]+=1
        else: 
            wordq[i]=1
    return wordq
