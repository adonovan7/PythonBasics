
file1 = open('C:\Users\irc01\Documents\myTestFile.txt',"w") 
file1.write("Hello World...") 
file1.write("Everyone's got to start somewhere, right?") 
file1.close() 

file2 = open('C:\Users\irc01\Documents\myTestFile.txt', "w") 
newLines = ["This is to add new lines of text. ", "I added another line here..."] # list of text to add
file2.writelines(newLines) 
file2.close()

### Questions: 
# why does it only print the second chunk's changes to the file?
# why does it only print the first read line?
# why are the different lines printed on one line?

with open('C:\Users\irc01\Documents\myTestFile.txt', "a") as file4:
    file4.write('and here is some other input from append.')
file4.close()

file3 = open('C:\Users\irc01\Documents\myTestFile.txt', "r") 
print file3.read() #read file
#print file3.read(5) #read first 5 characters
#print file3.readline() #reads first line
#print file3.readlines() #read all the lines, separated