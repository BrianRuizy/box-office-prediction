# box-office-prediction 🎬🍿💰
Machine learning project using a large historical dataset to find the patterns which contribute to a films 'success'.

## About
This learning project aims at exploring the use of an official Cinema dataset by reading, writing, cleaning and then implementing a Machine Learning model to be trained and predict the success of a movie release. Success can be measured by various different parameters; this program aims at finding relationships between those parameters and consider what makes a movie "succesful". Will then compare the accuracy of both *linear Regression* against *Random Forest Regression*. 

Program will undergo this pipeline:
**Cleaning phase** -> **Understanding data** -> **Prediction Models** -> **post-fact data**

## Dependencies
* NumPy 
* Pandas 
* Matplotlib
* Seaborn 
* SciKit-learn

## Pipeline
### Cleaning
At this step we want to remove records that will give us inaccuracies in our results. For instance whenever we have duplicates in the data, or places where we have null & zero values. We proceed by performing the following code...
```python
data = data.drop_duplicates(subset=['move_title', 'title_year'], keep='first').copy()
data.isnull().values.any()
```
