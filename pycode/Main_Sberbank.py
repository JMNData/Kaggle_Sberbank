from sklearn import tree
from sklearn.preprocessing import Imputer
import os
import sys
import pandas as pd

##Constants
cdirector = 'C:\\Users\\Mike\\Documents\\Github\\Kaggle_Sberbank'

#Setup ENvrionment
os.chdir(cdirector)
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 125)
##Functions
##Numeric - Fix nulls with Median
##Numeric - Fix nulls with Mean
##Numeric - Fix nulls with 0
##Numeric - Replace 0 with 1
##Numeric - Replace 0 with Mean
##Numeric - Remove Outliers
##Numeric - Fix Outliers With Mean
##Numeric - Replace Values less than an amount or greater than an amount with Mean
##Categorical - Fix Nulls with most common
##Categorical - Fix Nulls with least common

def setup(i):
    return pd.read_csv(i)


def maxfloorcleaner(df):
    #Fix Nulls - Median
    #floor > maxfloor, which can't happen. - Replacement of the value with a histogram bin? RESEACH
        print(sys._getframe().f_code.co_name + ' complete')
    
def material(df):    
    #TFix Nulls - Categorical.  Replace with 1 (Most common)
    print(sys._getframe().f_code.co_name + ' complete')   



dtrain = setup('data\\train.csv')
print(dtrain.describe())

#Scrubber
dtrain = dtrain[dtrain.id != 3530] #full_sq outlier
dtrain = dtrain[dtrain.id != 17935]
dtrain.life_sq.replace(0,dtrain.full_sq,inplace=True)

