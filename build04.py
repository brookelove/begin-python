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
this will be using the format function
'''
# Postcondition 01
my_str = "\nGreeting from a beginning Python programmer. \nDo you want to be addressed as ...\n"

print(my_str)
# Postcondition 02
tabIn = ("....................======>")

# put in the tabIn to ge the arrows then concat the beginning then use format function for name and concat a question mark 

# Postcondition 03
# Jane Margaret Doe
first="Jane"
middle = " Margaret"
last = " Doe"

# Postcondition 04
print(tabIn + "{0}{1}{2} ?".format(first, middle, last))
print(tabIn + "{0}{2}?".format(first, middle, last))
print(tabIn + "Mr./Ms. {0}{1}{2}?".format(first, middle, last))
print(tabIn + "Dear {0}".format(first, middle, last) + "? \n or")
print(tabIn + "{2},{0}{1} ?\n".format(first, middle, last))

# Archibald Montague Abercrombie
first = "Archibald"
middle = " Montague"
last = " Abercrombie"
print(tabIn + "{0}{1}{2} ?".format(first, middle, last))
print(tabIn + "{0}{2}?".format(first, middle, last))
print(tabIn + "Mr./Ms.{0}{1}{2}?".format(first, middle, last))
print(tabIn + "Dear {0}".format(first, middle, last) + "? \n or")
print(tabIn + "{2},{0}{1} ?\n".format(first, middle, last))

# Cleopatra Anastasia Montgomery 
first = "Cleopatra"
middle = " Anastasia"
last = " Montgomery"
print(tabIn + "{0}{1}{2} ?".format(first, middle, last))
print(tabIn + "{0}{2}?".format(first, middle, last))
print(tabIn + "Mr./Ms. {0}{1}{2}?".format(first, middle, last))
print(tabIn + "Dear {0}".format(first, middle, last) + "? \n or")
print(tabIn + "{2},{0}{1} ?\n".format(first, middle, last))
