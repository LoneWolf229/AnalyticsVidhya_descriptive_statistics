
# coding: utf-8

# In[6]:


import csv 
import numpy as np 
from nltk import sent_tokenize, word_tokenize as word_tokenize, pos_tag 
reader = csv.reader(open('C:/Users/psg/Desktop/twitter.csv', 'rU'), delimiter=',', quotechar='"') 
for line in reader: 		
    for field in line: 				
        tokens = word_tokenize(field)


# In[7]:


import nltk
nltk.download('punkt')


# In[18]:


import csv 
import numpy as np 
from nltk import sent_tokenize, word_tokenize as word_tokenize, pos_tag 
reader = csv.reader(open('C:/Users/psg/Desktop/twitter.csv'), delimiter=',', quotechar='"') 
for line in reader: 		
    for field in line: 				
        tokens.append((word_tokenize(field)))
print(tokens)


# In[19]:


print(tokens)


# In[20]:


from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer


# In[22]:


porter = PorterStemmer()
lancaster=LancasterStemmer()


# In[26]:


count = 0
for lists in tokens:
    count+=1
    if count <= 2:
        continue
    for words in lists:
        print("{0:20}{1:20}{2:20}".format(words,porter.stem(words),lancaster.stem(words)))

