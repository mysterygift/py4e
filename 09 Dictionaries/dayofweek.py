state = 0
while state < 1 :
    try :
        fname = input('Enter mailbox filename: ')
        fhandle = open(fname)
        state = 1
        
    
    except :
        print(f'EXCEPTION: File', fname, 'not found. Please try again.') 