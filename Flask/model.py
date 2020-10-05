import pandas as pd 
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor


df = pd.read_csv('../usedCarPrice_EDA.csv')
df
df.columns

reg = df['Registered City'].unique()
reg

Year = df['Year'].unique()
Year.min()

df[df['Year'] == 2020.0]

df['Transaction Type'].unique()

df.loc[[0]]

df_dum = pd.get_dummies(df[['Log_Price','Brand','Condition','KMs Driven','Model','Registered City', 'Transaction Type','Year']])
df_dum

X = df_dum.drop('Log_Price', axis =1)
y = df_dum.Log_Price.values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

### Decision Tree Regression | Just testing

dtree=DecisionTreeRegressor()
dtree.fit(X_train,y_train)
dtree_pred = dtree.predict(X_test)

acc_dt_reg = round( dtree.score(X_train, y_train) * 100, 2)
#print (str(acc_dt_reg) + ' percent')
list(X_test.iloc[1,:])

def predic_index(x):
    return list(X_test.iloc[x,:])

def predict_price(cat_cols,numeric_cols,Model):
    
    x = np.zeros(len(X.columns))
    for i in range(len(numeric_cols)):
        x[i] = numeric_cols[i]
    for i in cat_cols:
        if i in X.columns:
            loc_index = np.where(X.columns==i)[0][0]
            x[loc_index] = 1
        else:
            pass    
    return Model.predict([x])[0]

def predict_price1(cols,Model):
    # x = np.zeros(len(cols))
    # for i in range(len(cols)):
    #     x[i] = cols[i]
    for i in cols:
        if i in X.columns:
            loc_index = np.where(X.columns==i)[0][0]
            x[loc_index] = 1
        else:
            pass  
    print("Values: ", cols)
    return Model.predict([cols])[0]


def data_all(x):
    for i in df.index.values:
        if X_test.index[x] == df.index.values[i]:
            Price = np.exp(df['Log_Price'][i])
            Brand = df['Brand'][i]
            Fuel = df['Fuel'][i]
            Condition = df['Condition'][i]
            KMs_Driven = df['KMs Driven'][i]
            Car_Model = df['Model'][i]
            Registered_City = df["Registered City"][i]
            Transaction_Type = df['Transaction Type'][i]
            Year = df['Year'][i]
            data = {
                  "Brand": Brand,
                  "Condition": Condition,
                  "Fuel": Fuel,
                  "KMs Driven": KMs_Driven,
                  "Model": Car_Model,
                  "Registered City": Registered_City,
                  "Transaction Type": Transaction_Type,
                  "Year": Year
                  }
            break
    return data
    
    
def price_estimate(x):
    for i in df.index.values:
        if X_test.index[x] == df.index.values[i]:
            Price = np.exp(df['Log_Price'][i])
            Brand = df['Brand'][i]
            Fuel = df['Fuel'][i]
            Condition = df['Condition'][i]
            KMs_Driven = df['KMs Driven'][i]
            Car_Model = df['Model'][i]
            Registered_City = df["Registered City"][i]
            Transaction_Type = df['Transaction Type'][i]
            Year = df['Year'][i]
            data = {
                  "Brand": Brand,
                  "Condition": Condition,
                  "Fuel": Fuel,
                  "KMs Driven": KMs_Driven,
                  "Model": Car_Model,
                  "Registered City": Registered_City,
                  "Transaction Type": Transaction_Type,
                  "Year": Year
                  }
            break
    return Price

predic_index(1)