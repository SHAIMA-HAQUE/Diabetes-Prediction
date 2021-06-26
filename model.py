import numpy as np 
import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle


dataset = pd.read_csv('diabetes_data_upload.csv')
print(dataset)



le = LabelEncoder()

for i in dataset.columns[1:] :
    dataset[i] = le.fit_transform(dataset[i])

X = dataset.drop(['class'], axis="columns")
Y = dataset['class']

X_FS = X[['Age','Polyuria', 'Polydipsia', 'Gender','partial paresis','sudden weight loss','Irritability', 'delayed healing','Alopecia','Itching']]
X_train, X_test, Y_train, Y_test = train_test_split(X_FS, Y, test_size = 0.2,random_state=12345,shuffle=True)

#Random Forest

rfc = RandomForestClassifier()
rfc.fit(X_train, Y_train)

Y_pred_rfc = rfc.predict(X_test)

with open('model_pickle','wb') as model:
    pickle.dump(rfc,model)