
# coding: utf-8

# In[ ]:


import numpy as np

# sigmoid function
def nonlin(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))
    


# In[ ]:


# input dataset
X = np.array([  [0,0,1],
                [0,1,1],
                [1,0,1],
                [1,1,1] ])
    
# output dataset            
y = np.array([[0,0,1,1]]).T



# In[ ]:


# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)

# initialize weights randomly with mean 0
syn0 = 2*np.random.random((3,1)) - 1



# In[ ]:


for iter in range(10):

    # forward propagation
    l0 = X
    #print l0
    #print syn0
    l1 = nonlin(np.dot(l0,syn0))
    #print l1

    # how much did we miss?
    l1_error = y - l1
    #print l1_error

    # multiply how much we missed by the 
    # slope of the sigmoid at the values in l1
    l1_delta = l1_error * nonlin(l1,True)
    #print l1_delta

    # update weights
    syn0 += np.dot(l0.T,l1_delta)
    #print syn0


# In[ ]:


print("Output After Training:")
print(l1)

