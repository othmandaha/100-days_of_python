#---------------------------------------------------------------------#
#                        Simple Function                              #
#---------------------------------------------------------------------#

# def greet():
#     print("Hello")
#     print("How are you today?")
#     print("name") 

# greet()

#---------------------------------------------------------------------#
#                   Function that allows input                        #
#---------------------------------------------------------------------#

# # the "variable" inside the perenthesis is called a parameter
# def greet_with_name(name):
#     print(f"Hello {name}!!")
#     print(f"How are you doing {name}")

# # the piece of data inside the parenthesis is called an argument
# greet_with_name("amin") 

#---------------------------------------------------------------------#
#                  Function with more than 1 input                    #
#---------------------------------------------------------------------#

# def greet_with(name, location):
#     print(f"Hello {name}")
#     print(f"how is the weather in {location}")

# #The first argument get assigned to the firt parameter and the second argument get assigned to the second parameter. 
# #This is a POSITIONAL ARGUMENT
# greet_with("amin", "morocco") 


#---------------------------------------------------------------------#
#                  Function with keyword arguments                    #
#---------------------------------------------------------------------#

def greet_with_whatever(name, location, wife): 
    print(f"Hello {name}") 
    print(f"what is it like in {location}") 
    print(f"How is {wife}") 

greet_with_whatever(location= "Morocco", wife= "Khdouj", name= "amin") 
