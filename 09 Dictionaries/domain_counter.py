import string

state = 0

while state < 1 :
    try :
        fname = input('Enter mailbox file name/path: ')
        fhandle = open (fname)
        state = 1

    except :
        print('EXCEPTION: File', fname, 'not found.')

domain_counter = { }
for line in fhandle :
    if line.startswith('From') :
        line = line.rstrip()
        # print(line) # DEBUG
        words = line.split()
        # print (words) # DEBUG
        email = words[1].split('@') # I wrote this as 2 first because i'm stupid. ZERO INDEXED REMEMBER
        # print(email) # DEBUG
        domain = email[1]
        domain_counter[domain] = domain_counter.get(domain, 0) + 1    
    else :
        continue

sorted_domain_counter = sorted(domain_counter.items(), key=lambda x:x[1], reverse=True)
print(sorted_domain_counter)