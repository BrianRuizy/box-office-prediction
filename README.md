<h1 align="center">
    <img alt="logo" title="br logo" src="https://github.com/BrianRuizy/portfolio-website-3.0/blob/master/Misc/BR%20logo%20blk.png" width="100"> </br>
  Box Office Prediction 🎬🍿💰
</h1>

<h4 align="center">
Machine learning project using a large historical dataset to find the patterns which contribute to a films 'success'.
</h4>

## About
This learning project aims at exploring the use of an official Cinema dataset by reading, writing, cleaning and then implementing a Machine Learning model to be trained and predict the success of a movie release. Success can be measured by various different parameters; this program aims at finding relationships between those parameters and consider what makes a movie "succesful". Will then compare the accuracy of both *linear Regression* against *Random Forest Regression*. 

Program will undergo this implicit pipeline:
**Cleaning phase** -> **Understanding data** -> **Prediction Models** -> **post-fact data**

## Dependencies
Tools include: [Pandas](https://pandas.pydata.org/), 
[Matplotlib](https://matplotlib.org/), 
[Numpy](https://www.numpy.org/),
[Seaborn](https://seaborn.pydata.org/),
[SciKit-Learn](https://scikit-learn.org/stable/)

## Data Pipeline
* ### Data Cleansing
At this step we want to remove records that will give us inaccuracies in our results. For instance whenever we have duplicates in the data, or places where we have null & zero values. We proceed by performing the following code...
```python
data = data.drop_duplicates(subset=['move_title', 'title_year'], keep='first').copy()
data.isnull().values.any()
```
* ### Understanding the Data
Here we use matplotlib and numpy to further explore the data set and gain an understanding of the plots. Having done so we can find positive or negative correlations between variables, or find other valubale insights.
<img src="https://github.com/BrianRuizy/box-office-prediction/blob/master/images/boxoffice-understandingData.png" > </img>
* ### ML Models
