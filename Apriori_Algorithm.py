import pandas as pd
import numpy as np
from itertools import combinations

df = pd.read_csv("Transaction.csv",header=None)

Candidate_set = []
Frequent_set = []
items = pd.unique(df.values.ravel('K'))
items = items[~pd.isnull(items)]
min_support = int(input("Enter Min Support")) #Input from user

for iterno in range(1,len(items)): #Max iterations is equal to length of max set possible i.e. #items in the dataset
    Count = {}
    intermediate = []
    
    if iterno==1:
        Candidate_set.append(items)
        for txn in Candidate_set[iterno-1]:
            ctr=0
            for val in df.values:
                if txn in val:
                    ctr+=1
            Count[txn] = ctr
    else:
        Candidate_set.append(list(combinations(np.unique(np.array(Frequent_set[iterno-2]).ravel('K')),iterno)))
        for txn in Candidate_set[iterno-1]:
            ctr = 0
            for val in df.values:
                if all(i in val for i in txn):
                    ctr+=1
            Count[txn] = ctr
            
    for k in Count.keys():
        if Count[k] >= min_support:
            intermediate.append(k)

    if intermediate == []:
        print(Frequent_set)
        break

    Frequent_set.append(intermediate)
