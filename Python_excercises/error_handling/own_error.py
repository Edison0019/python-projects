#with the raise statement we can specify our own type of errors
#this means that we will stop the excecution of the program based on the error we got
age = input('enter your age here: ')
def year(age):
    age = int(age)
    if age < 18:
        raise ValueError('{} is not a valid age'.format(age))
        #this is one of the main handlers for creating custom exception errorss
        #this will throw the result of the error to whichever object who calls the year function
    print('thank you!')

year(age)