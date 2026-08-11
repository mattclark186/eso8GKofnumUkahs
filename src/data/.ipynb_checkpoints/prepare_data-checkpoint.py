#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.model_selection import train_test_split

def x_y_split(data):
    x = data.drop(columns=['Y'])
    y = data['Y']
    return x, y

def tt_split(x, y):
    return train_test_split(
        x, y, test_size=0.2, stratify=y, random_state=29
    )


# In[ ]:




