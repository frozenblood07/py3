
text = "test.\n file write.\n"
# notifies Python that you are opening this file, with the intention to write
saveFile = open("f.txt",'w')

# actually writes the information
saveFile.write(text)

# It is important to remember to actually close the file, otherwise it will
# hang for a while and could cause problems in your script
saveFile.close()



# so here, generally it can be a good idea to start with a newline, since
# otherwise it will append data on the same line as the file left off.
# you might want that, but I'll use a new line.
# another option used is to first append just a simple newline
# then append what you want.
appendMe = '\nNew bit of information'

appendFile = open('f.txt','a')
appendFile.write(appendMe)
appendFile.close()


# similar syntax as you've seen, 'r' for read. You can just throw a .read() at
# the end, and you get:
readFile = open('f.txt','r').read()
print(readFile)


# this will instead read the file into a python list.
readFile = open('f.txt','r').readlines()
print(readFile)