#!/usr/bin/env python
# coding: utf-8

# # Automatic File Sorter in File Explorer
# 

# In[9]:


import os, shutil


# In[5]:


path= r"C:/Users/LENOVO/Downloads/Automatic File Sorter Testing/"


# In[6]:


file_name = os.listdir(path)


# In[7]:


folder_names = ['excel files', 'image files', 'pdf files']

for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):
        print(path + folder_names[loop])
        os.makedirs((path + folder_names[loop]))


# In[8]:


for file in file_name:
    if ".xlsx" in file and not os.path.exists(path + "excel files/" + file):
        shutil.move(path + file, path + "excel files/" + file)
    elif ".png" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif ".pdf" in file and not os.path.exists(path + "pdf files/" + file):
        shutil.move(path + file, path + "pdf files/" + file)


# In[ ]:





# In[ ]:




