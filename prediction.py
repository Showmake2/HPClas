#!/usr/bin/env python
# coding: utf-8

# In[5]:


import joblib
from sklearn.metrics import confusion_matrix, roc_auc_score, average_precision_score
import pandas as pd
import math


# In[11]:


def loadmodel():
    catBoost_model_path = "model/catBoost_model.pkl"
    catBoost_model = joblib.load(catBoost_model_path)
    return catBoost_model
def valiadation(y_test, y_pred, y_score):
    con_matrix = confusion_matrix(y_test, y_pred, labels=[0, 1])
    tn, fp, fn, tp = con_matrix.ravel()
    acc = (tp + tn) / (tp + fp + tn + fn)
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (recall * precision) / (recall + precision)
    mcc = (tp * tn - fp * fn) / math.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
    AUROC = roc_auc_score(y_test, y_score)
    AUPRC = average_precision_score(y_test, y_score)
    performance = [recall, specificity, precision, acc, mcc, f1_score, AUROC, AUPRC]
    return performance
def prediction(output_name="", threshold=0.45):
    if output_name:
        X = pd.read_csv("features/%s.csv" % output_name, header=None)
        output_file = "%s.csv" % output_name
    else:
        X = pd.read_csv("features/test.csv", header=None)
        output_file = "output/result.csv"
    label = X.index
    clf = loadmodel()
    output = dict()
    output["pred_prob"] = clf.predict_proba(X)[:, 1]
    df_level = pd.DataFrame(output, index=label)
    print(df_level)
    df_level["pred"] = (df_level["pred_prob"] >= threshold).astype(int)
    df_level.to_csv(output_file)
    print(df_level)
    return df_level

if __name__ == "__main__":
    prediction()


# In[ ]:




