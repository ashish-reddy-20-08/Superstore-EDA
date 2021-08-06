#!/usr/bin/env python
# coding: utf-8

# In[2]:


#importing the required libraries
import numpy as np
import pandas as pd
import seaborn as sns 
from plotnine import *
import matplotlib.pyplot as plt


# In[3]:


#importing the dataset
superstore_data=pd.read_csv("SampleSuperstore.csv")


# In[4]:


#viewing the data
superstore_data


# In[5]:


#deleting the postal code column 
col=['Postal Code']
superstore_sample=superstore_data.drop(columns=col,axis=1)
superstore_sample.head()


# In[6]:


superstore_sample.shape


# #we have 9,994 rows and 12 columns(attributes) 

# In[8]:


superstore_sample.info()


# In[9]:


superstore_sample.describe()


# In[10]:


#checking whether we have any duplicate data or not in the data 
superstore_sample.duplicated().sum()


# In[11]:


#removing the 50 duplicate values which we found in the data 
superstore_sample.drop_duplicates(inplace=True)
superstore_sample.head()


# In[12]:


#now let us check whether the duplicate values are removed or not 
superstore_sample.duplicated().sum()


# In[13]:


superstore_sample.shape


# In[14]:


#let us see for each attribute how many different type of variables are there
superstore_sample.nunique()


# In[15]:


#correlation between the variables(sales,quantity,discount,profit)
sns.heatmap(superstore_sample.corr(),annot=True,fmt='.0%',cmap="YlGnBu")
plt.show()


# In[16]:


#covariance of the variables(sales,quantity,discount,profit)
sns.heatmap(superstore_sample.cov(),annot=True,fmt="f",cmap="Paired")
plt.show()


# In[17]:


#EDA DATA VISUALISATION


# In[27]:


#superstore category visualisation
plt.figure(figsize=(15,6))
scv=superstore_sample['Category'].value_counts()
cmap=plt.get_cmap('Spectral')
colors=['orange','yellow','magenta']
scv.plot.pie(autopct="%1.1f%%",shadow=True,colors=colors,explode=(0.03,0,0))
plt.title("Superstore Categories",fontsize=17)


# #From the above pie chart we can say that the store has Office Supplies more than the Furniture and Technology

# In[31]:


#VISUALIZING THE SUB-CATEGORY
superstore_sample['Sub-Category'].unique()


# In[19]:


superstore_sample.hist(bins=50,figsize=(20,15),color='yellow')


# In[21]:


plot_profit=(ggplot(superstore_sample, aes(x='Sub-Category', y='Profit', fill='Sub-Category'))+geom_col() +coord_flip()
+scale_fill_brewer(type='div',palette="Spectral")+theme_classic() +ggtitle('PIE CHART FOR PROFIT OF EACH SUB-CATEGORY'))

display(plot_profit)


# #FROM THE ABOVE CHART WE CAN INFER THAT THE COPIERS HAS MAXIMUM PROFIT WITHOUT ANY LOSS AND ALSO THE BINDERS HAVE EQUAL PROFIT AND LOSS VARIATION 

# In[22]:


#plot for ship mode vs count
ggplot(superstore_sample,aes(x="Ship Mode" , fill= "Category")) +geom_bar(stat='count')+ scale_colour_brewer(palette="OrRd")


# #IN THE ABOVE CHART WE CAN SEE THAT MOST OF THE CUSTOMERS HAVE CHOOSEN THE STANDARD CLASS DELIVERY AND IN THAT THE OFFICE SUPPLIES ARE MORE 

# In[24]:


superstore_sample['Ship Mode'].value_counts()


# In[45]:


#counting the number of times each state is repeated
superstore_sample['State'].value_counts()


# In[49]:


plt.figure(figsize=(17,10))
sns.countplot(x='State',data=superstore_sample,order=superstore_sample['State'].value_counts().index)
plt.xticks(rotation=90)
plt.show()


# #IN THE ABOVE CHART WE CAN SEE AND SAY THAT THE STATE CALIFORNIA HAS THE MORE NUMBER OF SALES THAN ALL THE OTHER STATES. 

# In[35]:


plt.figure(figsize=(10,8))
superstore_sample['Region'].value_counts().plot.pie()
plt.show()


# #THE WEST REGION OF UNITED STATES HAS MORE SALES

# In[36]:


#profit vs discount scatter plot

plt.subplots(figsize=(12,10))
plt.scatter(superstore_sample['Sales'],superstore_sample['Profit'])
plt.xlabel('Sales')
plt.ylabel('Profit')
plt.show()


# In[37]:


sns.lineplot(x='Discount',y='Profit',label="profit",data=superstore_sample)
plt.legend()
plt.show()


# In[38]:


#profit vs quantity

sns.lineplot(x='Quantity',y='Profit',label="profit",data=superstore_sample)
plt.legend()
plt.show()


# In[39]:


superstore_sample.groupby('Segment')[['Profit','Sales']].sum().plot.bar()
plt.ylabel('Profit/Loss and Sales')
plt.show()


# #WE CAN SEE FROM THE ABOVE CHART THAT THE CONSUMER SEGMENT HAS MORE PROFIT AND SALES THAN THE OTHER SEGMENTS

# In[40]:


#SEGMENT WISE SALES IN EACH REGION

plt.figure(figsize=(10,8))
plt.title('SEGMENT WISE SALES IN EACH REGION')
sns.barplot(x='Region',y='Sales', data=superstore_sample, hue='Segment',order=superstore_sample['Region'].value_counts().index)
plt.xlabel('Region')
plt.show()


# In[41]:


superstore_sample.groupby('Region')[['Profit','Sales']].sum().plot.bar()
plt.ylabel('profit/loss and sale')
plt.show()


# In[43]:


superstore_sample.groupby('State')[['Profit','Sales']].sum().sort_values(by='Sales',ascending=True).plot.bar(figsize=(18,10))
plt.title('profit/loss across states')
plt.xlabel('States')
plt.ylabel('profit/loss in states')
plt.show()


# #IN THE ABOVE CHART WE CAN SEE THE SALES IN CALIFORNIA HAS MORE PROFIT AND SALES WITHOUT ANY LOSS

# In[44]:


top_states=superstore_sample['State'].value_counts().nlargest(10)
top_states


# In[50]:


superstore_sample.groupby('Category')[['Profit','Sales']].sum().plot.bar(figsize=(18,10))
plt.ylabel('profit/loss and sales')
plt.show()


# In[53]:


superstore_sample.groupby('Sub-Category')[['Profit','Sales']].sum().sort_values(by='Sales',ascending=True).plot.bar(figsize=(10,10))
plt.title('profit/loss across states')
plt.xlabel('Sub-Category')
plt.ylabel('Profit/Loss in sales')
plt.show()

