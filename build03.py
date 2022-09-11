'''
Intent: Begin to provide options for the form of one person to be addressed.

Postconditions: The following are on the console (excluding the numbering):
1.
Greetings from a beginning Python programmer.
2.
Do you want to be addressed as ...
.......................................======>Jane Margaret Doe?
.......................................======>Jane Doe?
.......................................======>Mr./Ms. Jane Margaret Doe?
.......................................======>Dear Jane?
or 
.......................................======>Doe, Jane Margaret?
3.
After a blank line, the same output, but applied to Archibald Montague Abercrombie
4.
After a blank line, the same output, but applied to Cleopatra Anastasia Montgomery
'''
# build 01
my_str = "\nGreeting from a beginning Python programmer. \nDo you want to be addressed as ..."
print(my_str)

# postcondition 02
tabIn = ("....................======>")

# post condition 03 
# using more than one type 

# Jane Margaret Doe 
first = "Jane"
middle = " Margaret"
last = " Doe"
print(tabIn + first +  middle + last + " ?")
print(tabIn + first +  last +" ?")
print(tabIn + "Mr./Ms. "+ first + middle + " "+ last + " ?")
print(tabIn + "Dear "+ first + " ?")
print("or \n" + tabIn + last + ", " + first +  middle + "\n")

# Archibald Montague Abercrombie
first = "Archibald"
middle = " Montague"
last = " Abercrombie"
print(tabIn + first +  middle + last + " ?")
print(tabIn + first + last +" ?")
print(tabIn + "Mr./Ms. "+ first + middle + last + " ?")
print(tabIn + "Dear "+ first + " ?")
print("or \n" + tabIn + last + ", " + first + middle + "\n")

# Cleopatra Anastasia Montgomery
first = "Cleopatra"
middle = " Anastasia"
last = " Montgomery"
print(tabIn + first +  middle + last + " ?")
print(tabIn + first +  last +" ?")
print(tabIn + "Mr./Ms. "+ first + middle + last + " ?")
print(tabIn + "Dear "+ first + " ?")
print("or \n" + tabIn + last + ", " + first + middle + "\n")
