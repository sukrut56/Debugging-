'''
1.a
Using the print() function only, get the wrong_add_function to print out where
it is making a mistake, given the expected output for ex, "we are making an error 
in the loop", which you would put near the loop. 
Structure the print() statement to show what the expected output ought to be
via f-strings: ie "The correct answer is supposed to be: [...]".
'''

def wrong_add_function(arg1,arg2):
   ans = [2,3,4]
   arg1_index=0
   while arg1_index < len(arg1):
      arg_2_sum = 0
      for arg2_elements in arg2:
      	arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])  
      	print("We are making a mistake in this loop. We are iterating over the list multiple times after adding the two lists.")
      arg1[arg1_index]=arg_2_sum
      arg1_index+=1
   print(f'The correct answer is supposed to be {ans}')   
   return arg1

arg1 = [1,2,3]
arg2 = [1,1,1]

print(wrong_add_function(arg1, arg2))

'''
1.b
Then, changing as little as possible, modify the function, using the same 
general structure to output the correct answer. Call this new function 
correct_add_function() 
'''

def correct_add_function(arg1,arg2):
   arg1_index=0
   while arg1_index < len(arg1):
       arg_2_sum = 0
       arg_2_sum = sum([arg1[arg1_index]+ arg2[i] for i in range(len(arg2)) if i == arg1_index])      #making changes so that we can get the output
       arg1[arg1_index]=arg_2_sum
       arg1_index+=1
   return arg1

arg1 = [1,2,3]
arg2 = [1,1,1]

print(correct_add_function(arg1, arg2))

