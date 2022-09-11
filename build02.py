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
'''
# postcondition 01
my_str = "\nGreeting from a beginning Python programmer. \nDo you want to be addressed as ..."
print(my_str)

#post condition 02
tabIn = ("....................======>")

# print that variable multiple times
print(tabIn + "Jane Margaret Doe?")
print(tabIn + "Jane Doe?")
print(tabIn + "Mr./Ms. Jane Margaret Doe?")
print(tabIn + "Dear Jane?\nor")
print(tabIn + "Doe, Jane Margaret?")