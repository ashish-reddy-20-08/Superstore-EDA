# Superstore-EDA (Exploratory Data Analysis)
In this project we will be performing EDA on the superstore data and we will draw meaningful insights from the data about the store items and sales. 

## What is data cleaning? 

- Data cleaning is one of the important parts of machine learning. It plays a significant part in building a model. 
-  It surely isn’t the fanciest part of machine learning and at the same time, there aren’t any hidden tricks or secrets to uncover.
- However, the success or failure of a project relies on proper data cleaning. 
- Professional data scientists usually invest a very large portion of their time in this step because of the belief that “Better data beats fancier algorithms”
- If we have a well-cleaned dataset, there are chances that we can get achieve good results with simple algorithms also, which can prove very beneficial at times especially in terms of computation when the dataset size is large.

## Steps involved in Data Cleaning: 

![image](https://user-images.githubusercontent.com/63282184/136796151-96b9df02-8c78-424c-8aff-7c464151296a.png)

## Removal of unwanted observations

This includes deleting duplicate/ redundant or irrelevant values from your dataset. 

Duplicate observations most frequently arise during data collection and Irrelevant observations are those that don’t actually fit the specific problem that you’re trying to solve. 

- Redundant observations alter the efficiency by a great extent as the data repeats and may add towards the correct side or towards the incorrect side, thereby producing unfaithful results.
- Irrelevant observations are any type of data that is of no use to us and can be removed directly.

## Fixing Structural errors

The errors that arise during measurement, transfer of data, or other similar situations are called structural errors.

Structural errors include typos in the name of features, the same attribute with a different name, mislabeled classes, i.e. separate classes that should really be the same, or inconsistent capitalization. 

- For example, the model will treat America and America as different classes or values, though they represent the same value or red, yellow, and red-yellow as different classes or attributes, though one class can be included in the other two classes. 
