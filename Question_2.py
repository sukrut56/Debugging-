'''
#2.a
#Update the numeric section of the function with your changes from 1 for both 
#2.b and 2.c
'''

def wrong_add_function(arg1,arg2):
   #numeric section
   if sum([type(i)==int for i in arg1])==len(arg1) and \
      sum([type(i)==int for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = 0
            for arg2_elements in arg2:
               arg_2_sum = sum([arg1[arg1_index]+ arg2[i] for i in range(len(arg2)) if i == arg1_index])    #making changes to the second question code
            arg1[arg1_index]=arg_2_sum  
            arg1_index+=1
         return arg1
   #string section
   elif sum([type(i)==str for i in arg1])==len(arg1) and \
      sum([type(i)==str for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = ''
            for arg2_elements in arg2:
               arg_2_sum += arg2_elements
            arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
            arg1_index+=1
         return arg1

arg_str_1=['1','2','3']
arg_str_2=['1','1', 1]

print(wrong_add_function(arg_str_1,arg_str_2))


################################################# QUESTION 2 B ############################

'''
2.b
Without modifying the string section code itself or the input directly, 
write a try, except block that catches the issue with the input below and 
returns an error message to the user, in case users give invalid inputs,
(for example an input of ["5","2", 5])
: "Your input argument [1 or 2] at element [n]
is not of the expected type. Please change this and rerun. Name this function 
exception_add_function()
'''

def wrong_add_function(arg1,arg2):

   def exception_add_function(input):
      for i,j in enumerate(input):
         try: 
            count = type(j) == str          #comparing the type of input 
            if count != True:               
               raise TypeError       
         except TypeError:                  #raising an exception for the typeerror 
            print(f"Your input argument {input} at element {i} is not of the expected type. Please change this and return")   #using f-string to indicate the mistake in input string 


   #numeric section
   if sum([type(i)==int for i in arg1])==len(arg1) and \
      sum([type(i)==int for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = 0
            for arg2_elements in arg2:
               arg_2_sum = sum([arg1[arg1_index]+i for i in range(len(arg2)) if i == arg1_index])
            arg1[arg1_index]=arg_2_sum  
            arg1_index+=1
         return arg1
   #string section
   elif sum([type(i)==str for i in arg1])==len(arg1) and \
      sum([type(i)==str for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = ''
            for arg2_elements in arg2:
               arg_2_sum += arg2_elements
            arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
            arg1_index+=1
         return arg1

   else: 
      exception_add_function(arg1)              #executing the fucntion for input 1 
      exception_add_function(arg2)              #executing the fucntion for input 2




arg_str_1=['1','2','3']

arg_str_2=['1','1', 1]

print(wrong_add_function(arg_str_1,arg_str_2))



############################################## QESTION 2 C ####################################


'''
Without modifying the string section code itself or the input directly, 
write a try, except block that catches the issue with the input below and 
gets it to process via the string section. IE, do not, outside the function,
change the values of arg_str_1 or arg_str_2. Name this function 
correction_add_function(), i.e you will not be updating the wrong_add_function,
you will simply handle the error of wrong inputs in a seperate function, you want
the wrong_add_function to output its current result you are only bolstering the 
function for edge cases. 
'''


def wrong_add_function(arg1,arg2):

   def correct_add_function(arg1, arg2):

        for i,j in enumerate(arg1):
            try:
                c = type(j) == str                                #comparing the type of input with string 
                if c != True: raise TypeError                     #raise type error if they are not the same
            except TypeError:
                arg1 = ([str(j) for i,j in enumerate(arg1)])      #using list comprehension to calculate the length of input string
        for i,j in enumerate(arg2):
            try:
                c = type(j) == str
                if c != True: raise TypeError
            except TypeError:
                arg2 = ([str(j) for i,j in enumerate(arg2)])

                
        arg1_index=0
        while arg1_index < len(arg1):
            arg_2_sum = ''
            for arg2_elements in arg2:
                arg_2_sum += arg2_elements
            arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
            arg1_index+=1        
        return arg1

   #numeric section
   if sum([type(i)==int for i in arg1])==len(arg1) and \
      sum([type(i)==int for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = 0
            for arg2_elements in arg2:
               arg_2_sum = sum([arg1[arg1_index]+i for i in range(len(arg2)) if i == arg1_index])
            arg1[arg1_index]=arg_2_sum  
            arg1_index+=1
         return arg1
   #string section
   elif sum([type(i)==str for i in arg1])==len(arg1) and \
      sum([type(i)==str for i in arg2])==len(arg2):
         arg1_index=0
         while arg1_index < len(arg1):
            arg_2_sum = ''
            for arg2_elements in arg2:
               arg_2_sum += arg2_elements
            arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
            arg1_index+=1
         return arg
   else: 
      print(correct_add_function(arg1,arg2))


arg_str_1=['1','2','3']
arg_str_2=['1','1', 1]


wrong_add_function(arg_str_1,arg_str_2)
