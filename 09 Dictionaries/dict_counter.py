state = 0
while state < 1 :
    try :
        fname = input('Enter file: ')
        fhandle = open(fname)
        state = 1

        counts = dict()
        for line in fhandle :
            line = line.rstrip()
            words = line.split()
            for word in words :
                counts[word] = counts.get(word, 0) + 1
        
        bigcount = None
        bigword = None
        for word,count in counts.items() :
            if bigcount is None or count > bigcount :
                bigcount = count
                bigword = word
        
        print(bigword, bigcount)

    except :
        print('EXCEPTION: File not found. Please try again.')