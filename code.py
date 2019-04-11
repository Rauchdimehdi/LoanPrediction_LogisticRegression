import pandas as pd
import numpy as np                     # For mathematical calculations
import seaborn as sns                  # For data visualization
import matplotlib.pyplot as plt        # For plotting graphs
#matplotlib inline
import warnings                        # To ignore any warnings
warnings.filterwarnings("ignore")




##################################################
train=pd.read_csv("train_u6lujuX_CVtuZ9i.csv")
test=pd.read_csv("test_Y3wMUE5_7gLdaTN.csv")

#############*********COPY*************#####################################
train_original=train.copy()
test_original=test.copy()

###################printing train & test columns + data type###################################################
#print(train.columns)
#print(test.columns)
#print(train.dtypes)
#print(train.shape, test.shape)
print(train)
#print(test)
  
#################### Missing values ############################################################################
#print(train.isnull().sum())

train['Gender'].fillna(train['Gender'].mode()[0], inplace=True)
train['Married'].fillna(train['Married'].mode()[0], inplace=True)
train['Dependents'].fillna(train['Dependents'].mode()[0], inplace=True)
train['Self_Employed'].fillna(train['Self_Employed'].mode()[0], inplace=True)
train['Credit_History'].fillna(train['Credit_History'].mode()[0], inplace=True)
train['Loan_Amount_Term'].fillna(train['Loan_Amount_Term'].mode()[0], inplace=True)


######################LOAN AMOUNT#############################################################################
#print(train['Loan_Amount_Term'].value_counts())

train['LoanAmount'].fillna(train['LoanAmount'].median(), inplace=True)



#######################################################################
print(train.isnull().sum())


#########################Dropping the LoanID as it doesn't affect the Loan Status###########################################
train=train.drop('Loan_ID',axis=1)
test=test.drop('Loan_ID',axis=1)

################################Dummies variable: ############################################################################################


X = train.drop('Loan_Status',1)
y = train.Loan_Status

X=pd.get_dummies(X)
train=pd.get_dummies(train)
test=pd.get_dummies(test)

print(train)
#print(train.Loan_Status_N)
#print(test)




