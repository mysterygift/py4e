# Write code that parses mbox-short.txt and outputs the emails + a count of all the lines that start with 'From'.

state = 0
while (state < 1) :
    try :
        filename = input('Please enter the name and extension of the mailbox file: ')
        fhandle = open(filename, 'r')
        state = 1
        # print(fhandle)
        emaillist = list()
        # print('DEBUG: emaillist initialised.')
        emailcount = 0
        # print('DEBUG: emailcount initialised.')
        for line in fhandle :
            if line.startswith('From:') :
                line = line.rstrip()
                linelist = line.split()
                emaillist.append(linelist[1])
                # print(line)
            else :
                continue
        # print(emaillist)
        for email in emaillist :
            print(email)
            emailcount = emailcount + 1
        print(f'There are', emailcount, 'emails found in', filename + '.')

    except :
        print("File '" + filename + "' not found. Please try again.")