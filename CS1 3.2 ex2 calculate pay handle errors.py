
# coding: utf-8

# Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:
# 
# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input

# Enter Hours: forty
# Error, please enter numeric input

# In[1]:


#get hours

hours = input('Enter hours: ')

#use try except in case non-numerical data has been entered
try :
    hours = float(hours)
except: 
    print('Please enter numeric input.')
    #another chance to enter correctly
    hours = input('Enter hours as numeric input: ')
    try:
        hours = float(hours)
    except: 
        print('Please enter numeric input; program ended.')
        
#get base rate
rate = input('Enter base rate: ')

#use try except in case non-numerical data has been entered
try :
    rate = float(rate)
except: 
    print('Please enter numeric input.')
    #another chance to enter correctly
    rate = input('Enter base rate as numeric input: ')
    try:
        rate = float(rate)
    except: 
        print('Please enter numeric input; program ended.')
    
base_pay = hours*rate
#print(base_pay)
    
#calculate extra pay
if hours >40 :
    hours2 = (float(hours)) - 40.0
    rate2 = (float(rate))*1.5        
    extra_pay = (float(hours2))*(float(rate2))
    #print(extra_pay)
if hours <=40 :
    extra_pay = 0
    #print ('no extra pay')
        
#calculate total pay
total_pay = base_pay + extra_pay
print('pay:',total_pay)


# In[2]:


#get hours

hours = input('Enter hours: ')

#use try except in case non-numerical data has been entered
try :
    hours = float(hours)
except: 
    print('Please enter numeric input.')
    #another chance to enter correctly
    hours = input('Enter hours as numeric input: ')
    try:
        hours = float(hours)
    except: 
        print('Please enter numeric input; program ended.')
        
#get base rate
rate = input('Enter base rate: ')

#use try except in case non-numerical data has been entered
try :
    rate = float(rate)
except: 
    print('Please enter numeric input.')
    #another chance to enter correctly
    rate = input('Enter base rate as numeric input: ')
    try:
        rate = float(rate)
    except: 
        print('Please enter numeric input; program ended.')
    
base_pay = hours*rate
#print(base_pay)
    
#calculate extra pay
if hours >40 :
    hours2 = (float(hours)) - 40.0
    rate2 = (float(rate))*1.5        
    extra_pay = (float(hours2))*(float(rate2))
    #print(extra_pay)
if hours <=40 :
    extra_pay = 0
    #print ('no extra pay')
        
#calculate total pay
total_pay = base_pay + extra_pay
print('pay:',total_pay)

