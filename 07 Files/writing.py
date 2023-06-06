# You use 'w' as a parameter when writing to files using open().

fout = open('loremipsum2.rtf', 'w')
print(fout) # <_io.TextIOWrapper name='loremipsum2.rtf' mode='w' encoding='UTF-8'>

# This will create a new file if one does not already exist. However, it will also overwrite an existing file of the same name! SO BE CAREFUL ALRIGHT.
# .write() puts data into the file and returns the number of characters written.

line1 = "This is line number 1!\n" # .write() does not implicitly add a newline (unlike print()) – we must add one.
fout.write(line1) # 23
fout.close() # Ensures the data is written to the disk and stops writing. We can do this for read-only access, but it's a bit sloppy as Python
# handles this automatically when a program ends.
