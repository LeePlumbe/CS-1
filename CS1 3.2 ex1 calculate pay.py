
# coding: utf-8

# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.
# 
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0 #this should be 525.0

# In[1]:


###this is more complex - hours about 40 is 1.5####
#get hours
hours = input('Enter hours: ')


# In[2]:


#get rate
rate = input('Enter rate: ')


# In[3]:


#use try except in case non-numerical data entered
try :
    #calculate base pay
    hours = float(hours)
    rate = float(rate)
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
        #print('no extra pay')
        
    #calculate total pay
    total_pay = base_pay + extra_pay
    print('pay:',total_pay)

except :
    print('error')

