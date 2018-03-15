
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*- 
""" 
Created on Mon Mar 12 07:35:11 2018 

@author: johnodin99 
""" 
import os 
import pandas as pd 


if __name__ == '__main__':
    # You should not modify this part.
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--training',
                        default='training_data.csv',
                        help='input training data file name')
    parser.add_argument('--testing',
                        default='testing_data.csv',
                        help='input testing data file name')
    parser.add_argument('--output',
                        default='output.csv',
                        help='output file name')
    args = parser.parse_args()
 
################################training##################################### 
""" 
userhome = os.path.expanduser('~') 
traing_data_path = userhome+"/Desktop/training_data.csv" 
traing_data_path = args.training

training_data = pd.read_csv(traing_data_path,header=None) 
training_data.columns=["open","high","low","close"] 
training_data.index=pd.to_datetime(training_data.index,unit="D") 

 
#simple moving average 
training_simple_5 = training_data["close"].rolling(window=5).mean() 
training_simple_20 = training_data["close"].rolling(window=20).mean() 

#exponential moving average 
#exponential=pd.ewma(training_data["close"],span=10,freq="D",min_periods=10) 

training_action = [] 
slot_status = 0 

 
for i  in range(len(training_simple_5.index)): 
    if (training_simple_5[i]>training_simple_20[i] and slot_status==0): 
        print("1") 
        training_action.append("1") 
        slot_status = 1 
         
    elif (training_simple_5[i]<training_simple_20[i]and slot_status==1): 
        print("-1") 
        training_action.append("-1") 
        slot_status = 0 
     
        
    else: 
        training_action.append("0") 
        print("0") 
 """ 
################################testing#################################### 
#userhome = os.path.expanduser('~') 
#testing_data_path = userhome+"/Desktop/testing_data.csv" 
testing_data_path = args.testing

testing_data = pd.read_csv(testing_data_path,header=None) 
testing_data.columns=["open","high","low","close"] 
testing_data.index=pd.to_datetime(testing_data.index,unit="D") 

 
#simple moving average 
testing_simple_5 = testing_data["close"].rolling(window=5).mean() 
testing_simple_20 = testing_data["close"].rolling(window=20).mean() 

#exponential moving average 
#exponential=pd.ewma(training_data["close"],span=10,freq="D",min_periods=10) 

testing_action = [] 
slot_status = 0 

 
for i  in range(len(testing_simple_5.index)): 
    if (testing_simple_5[i]>testing_simple_20[i] and slot_status==0): 
        testing_action.append("1") 
        slot_status = 1 
         
    elif (testing_simple_5[i]<testing_simple_20[i]and slot_status==1): 
        testing_action.append("-1") 
        slot_status = 0   
       
    else: 
        testing_action.append("0") 
         
testing_action=pd.DataFrame(testing_action) 
testing_action = testing_action[:-1] 
#path = userhome+"/Desktop/output.csv" 
path = args.output
testing_action.to_csv(path,sep=' ',header=0,index=0) 

     




# # Use moving average method(5  and 20 days)  to forecast the stock when to reverse the trend  and then provide the suggestion to invest or sell , the method is to recognize the cross point and slot status 
