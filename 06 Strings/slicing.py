string = 'Monty Python'
print(string[5:8]) # Prints ' py'

# If the range provided by the colon operator : goes beyond the end of the array, it just goes to the end of the string. No traceback!

string = 'Tester Bester'
print(string[1:30]) # Prints 'ester Bester'

print(string+string[2:9]) # Prints 'Tester Besterster Be' lmao

string = 'dogs are cool'
print(string,string) # Prints 'dogs are cool dogs are cool'
print(string + string) # Prints 'dogs are cooldogs are cool' (note there is no space in the middle when you use + to concatenate strings)

'dogs' in string # Returns true as 'dogs' is present in the string stored in str.

bigstr = "Wow Look at ALL thesE leTTeRzZ!"
max(bigstr) # Returns 'z' as in bigstr lowercase z has the largest value (interestingly, not capital Z)
print(max(bigstr),string) # french person talking about how cool dogs are

smallstr = bigstr.lower()
print(smallstr) # Prints 'wow look at all these letterzz!'
biggerstr = smallstr.upper()
print(biggerstr) # Prints 'WOW LOOK AT ALL THESE LETTERZZ!'
capitalstr = smallstr.capitalize()
print(capitalstr) # Prints 'Wow look at all these letterzz!'

print('I HAVE BECOME CRINGE'.lower()) # Prints 'i have become cringe'

# SEARCHING A STRING!

lorem_ipsum = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
find_result = lorem_ipsum.find('dolor') # Searches string lorem_ipsum for the substring passed into the find method 'dolor'. The position in the array is then stored in variable find_result.
print(find_result) # Prints the position of substring 'dolor'.

lorem_ipsum2 = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'

search_cond = 1 # Create a variable that the while look can compare to. I've called this the "search condition".
while search_cond >= 1 : # Checks to see if a successful search has been completed.
    search_term = input('What are you looking for?: ') # Stores search term as a string into a variable.
    search_result = lorem_ipsum2.find(search_term) # Conducts the search for the position in the array, 0 indexed, returning it as an integer. Returns -1 if not found.
    if search_result > 0 :
        conv_search_result = str(search_result) # Converts the position into a string and stores it in another variable. This is so we can concatenate it in the print function below.
        print(f"What you're looking for can be located at position {conv_search_result}.") # Prints the position. Using an f-string I can write functions directly into a string. Much tidier.
        search_cond = search_cond - 1 # I initially used this to end the loop but realised break works fine. Actually they really do the same thing, not sure which is more efficient.
        #break
    else :
        print("I'm sorry, I couldn't find that. Please try again.") # No break here, so the loop tries again.

censored = lorem_ipsum2.replace('o','*') # You cannot replace multiple characters in this way. You will need to use translate() to do that.
censored_2 = lorem_ipsum2.translate(lorem_ipsum2.maketrans({'a' : '*', 'e' : '&', 'i' : '#'})) # I think this uses dicts, which I haven't covered yet. Very useful though!
print("\n"+censored)
print("\n"+censored_2)

#print("\nEnd of program. :)")