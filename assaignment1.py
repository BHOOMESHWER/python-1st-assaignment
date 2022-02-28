#!/usr/bin/env python
# coding: utf-8

# 1. In the below elements which of them are values or an expression? eg:- values can be integer or string and expressions will be mathematical operators.
# * 'hello'-87.8, - ,/ ,+	 ,6  

# In[1]:


a="hello"
type(a)


# In[3]:


a=-87.8
type(a)


# In[4]:


12-4


# In[5]:


12/4


# In[6]:


3+4


# In[7]:


a=6
type(a)


# 2. What is the difference between string and variable?
ans: A variable is a store of information,and a string is a type of information store in a variable.
     A string is usually  words, enclosed with "" or ''
    eg: s="welcome to ineuron"
    here s is the variable and we declare the string.
   
#  3. Describe three different data types?
# 
integer
whole numbers-eg:1,2,254,2448
list
numbers,charecters,floting values-eg:[14,"hello",15.6]
boolean
the stament either true or false
# 4. What is an expression made up of? What do all expressions do?

# In[ ]:


Expression is made up of values, containers, and mathematical operators
eg:
    12-4 this expression as used to substruct the values


# 5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?
ans:
Expression is made up of values, containers, and mathematical operators and
The statement is just like a command that a python interpreter executes like print.
# 6. After running the following code, what does the variable bacon contain?
# bacon = 22
# bacon + 1
# 

# In[8]:


bacon=22
bacon+1


# 7. What should the values of the following two terms be?
# 'spam' + 'spamspam'
# 'spam' * 3

# In[9]:


'spam' + 'spamspam'


# In[10]:


'spam' * 3


# 8. Why is eggs a valid variable name while 100 is invalid?
ans:
yes,why because we can't  start give a variable with an integer name, we start with a string or alphabets like e100 and egg100 is valid 
# 9. What three functions can be used to get the integer, floating-point number, or string version of a value?
str(), int(), float()
# 10. Why does this expression cause an error? How can you fix it?
# 'I have eaten ' + 99 + ' burritos.'
a string can't connect with integer thats why its an error