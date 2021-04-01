#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install sigmapie


# In[9]:


from sigmapie.fst_object import *
from sigmapie.helper import *

fakelang = [("rs","tatta"),("rS","tatda"),("rz","tattda"),("Rs","tadda"),("RS","tadta")]
inputalp = ["r","R","s","S","z"] #had to change morpheme names because program messes up with two symbols for a single morpheme
outputalp = ["t","a","d"]
G = build_ptt(fakelang,inputalp,outputalp)
print(G.Q)
print(G.stout)
print(G.E)
print(G.Sigma)
print(G.Gamma)


# In[10]:



z = onward_ptt(G,'','') 
fst = z[0]
print(fst.E)


# In[35]:


def suffix(d):
    guy = d[::-1]
    return prefix(guy)

#list of morpheme strings 
dog = list(item[0] for item in fakelang)
#morphemes reversed
suffixtuples = []
for doggy in dog: 
    suffixtuples.append(suffix(doggy))
suffixset = []
for item in suffixtuples:
    suffixset.append(item[1])
#getting unique value set
suffixset = set(suffixset)
#very ugly returning it back to list form
suffixset = list(suffixset)
print(suffixset)


# In[46]:


morphtoout = {}
prefixtoout = {}
#environments
onesuffixofprefout = {}
for item in fst.E: 
    morphtoout[item[3]] = item[2]
for item in morphtoout: 
    if len(item[0]) == 1: 
        prefixtoout[item[0]] = morphtoout[item[0]]
for item in prefixtoout:
    onesuffixofprefout[item[0]] = prefixtoout[item[0]][-1]

#set of outputs for a certain suffix with the associated prefix
outputs = {}
for suffix in suffixset:
    temp = []
    for item in fst.E: 
        if suffix in item[3]: 
            temp.append([item[0],item[2]])
    outputs[suffix] = temp
print(outputs)

#replacing associated prefixes with their output 1-suffixes
for item in outputs:
    for john in outputs[item]:
        temp = john[0]
        john[0] = onesuffixofprefout[temp]
print(outputs)  


        
    


# In[ ]:


#main omega if body 
      

