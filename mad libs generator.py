#The program design is such that it will ask users to enter a series of inputs that will be considered as a Mad Lib.
#The input could be anything, an adjective, a noun, a pronoun, etc. Once all the inputs are entered, the application will take the data and arrange the inputs into a story template form. 

name = input ("name\t")
email = input ("email\t")
familyname = input ("family name\t")
place = input ("place\t")
zipcode = int (input ("zipcode\t"))
mobile = int (input ("mobile\t"))
def address() :
    print(name)
    print(email)
    print(familyname)
    print(place)
    print(zipcode)
    print(mobile) 
print ( "Address =" )
address()
