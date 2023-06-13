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
        domain = email[1] # We have to push these domains into their own variable first as you cannot use .get() with a hashable (mutable) data type.
        domain_counter[domain] = domain_counter.get(domain, 0) + 1 # I tried doing this with email[1] first and it spat out an error referring to the above.
    else :
        continue

sorted_domain_counter = sorted(domain_counter.items(), key=lambda x:x[1], reverse=True) # Figured I'd sort the output here to make it more useful. Don't really get lambda functions atm, BUT...
print(sorted_domain_counter)

# From what I found online, a lambda function is just a function without a name. Using this as a key, (key=lambda x:x[1]) this will sort the values in each reference by ascending order,
# which is then reversed.

