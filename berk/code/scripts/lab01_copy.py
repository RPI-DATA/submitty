#!/usr/bin/env python
# coding: utf-8

# Name: 
# Email: 

# # Class 1 Introductory Lab 
# 
# 
# Welcome!  
# 
# Before we get started, there are some administrative details.
# 
# Labs are required. Here is how you get credit. Get credit by submitting a pdf version of the notebook.
# 
# Collaborating on labs is more than okay -- it's encouraged! You should rarely be stuck for more than a few minutes on questions in labs, so ask a neighbor or an instructor for help. (Explaining things is beneficial, too -- the best way to solidify your knowledge of a subject is to explain it.) Please don't just share answers, though.
# 
# 
# #### Today's lab
# 
# In today's lab, you'll learn how to:
# 
# 1. navigate Jupyter notebooks (like this one);
# 2. write and evaluate some basic *expressions* in Python, the computer language of the course;
# 3. call *functions* to use code other people have written; and
# 4. break down Python code into smaller parts to understand it.
# 
# This lab covers parts of [Chapter 3](http://www.inferentialthinking.com/chapters/03/programming-in-python.html) of the online textbook. This is usefule but not required.

# In[8]:


# Don't change this cell; just run it. 
# The result will give you directions about how to log in to the submission system, called OK.
# Once you're logged in, you can run this cell again, but it won't ask you who you are because
# it remembers you. However, you will need to log in once per assignment.
from client.api.notebook import Notebook
ok = Notebook('lab01.ok')
_ = ok.auth(inline=True)

# In[9]:


# Change the next line so that it computes the number of
# seconds in a decade and assigns that number the name
# seconds_in_a_decade.
seconds_in_a_decade = 10 * 365 * 24 * 60 * 60;

# We've put this line in this cell so that it will print
# the value you've given to seconds_in_a_decade when you
# run it.  You don't need to change this.
seconds_in_a_decade

# In[10]:


# Test cell; please do not change!
_ = ok.grade('q32')

# In[ ]:



