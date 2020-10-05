# Pakistan Used Car Price Prediction

![Example](https://user-images.githubusercontent.com/39486938/95116657-c9deaa80-0760-11eb-923c-adc3eb1bc8a9.PNG)

* This repository is for the Kaggle's Car Price Prediction to Identify Pakistan used Car prices.
* We cleaned the data and did Exploratory Data Analysis from different perspectives to know in-detail about Cars background.
* For our model building we used are  Linear, Ridge Lasso, Random Forest and Decision Tree Regressors.


## Resources We Used
* Python version 3.8
* Jupyter Notebook
* We used pandas, numpy, sklearn, matplotlib, seaborn, flask, json, pickle packages.
* Dataset Link: https://www.kaggle.com/karimali/used-cars-data-pakistan
* Flask Productionization Article: https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2


## Data Cleaning and Exploratory Data Analysis
* We analyzed and cleaned this dataset so it can be usable for our model.
* And in EDA part, we simplified our data by removing outliers from price
* And analyzed different value counts through graphs also through pivot table.


## Model Building
* We transformed our variables into dummy variables.
* Then we split it into test and train set with 20% test set.
* We used different Models to evaluate.
* The Decision Tree model performed better than the other approaches on the test set. 

Model Used | Score
------------ | -------------
Decision Tree Regression | 90.77%
Random Forest Regression | 89.07%
Linear Regression | 75.89%
Ridge Regression | 75.65%
Lasso Regression | 36.21%


## Deployed Using Flask

* Here we build Flask API that was hosted on local server with above given tutorial link
* This API will take list of values and predict the Price.
* To send request to the flask application:
    Run app.py, after installing all the required dependencies.
    In another terminal, run request.py, to get the response.
