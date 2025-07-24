#!/usr/bin/env python
# coding: utf-8

# In[1]:


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import joblib
import pandas as pd
import numpy as np
# from google.colab import drive


# In[ ]:


# drive.mount('/content/drive')


# In[2]:


# load the best trained model
model = joblib.load('../summative/best_model.pkl')


# In[4]:


class GovernanceInput(BaseModel):
    Q20: float = Field(..., ge=0, le=10, description="Trust in local government (0–10)")
    Q21A: float = Field(..., ge=0, le=10)
    Q24: float = Field(..., ge=0, le=10)
    Q34A: float = Field(..., ge=0, le=10)
    Q26: float = Field(..., ge=0, le=10)
    Q28: float = Field(..., ge=0, le=10)
    Q32A: float = Field(..., ge=0, le=10)
    Q32B: float = Field(..., ge=0, le=10)
    Q48A: float = Field(..., ge=0, le=10)
    Q48B: float = Field(..., ge=0, le=10)
    Q50A: float = Field(..., ge=0, le=10)
    Q50B: float = Field(..., ge=0, le=10)
    Q50C: float = Field(..., ge=0, le=10)
    Q51A: float = Field(..., ge=0, le=10)
    Q51B: float = Field(..., ge=0, le=10)
    Q53A: float = Field(..., ge=0, le=10)
    Q53B: float = Field(..., ge=0, le=10)
    Q53C: float = Field(..., ge=0, le=10)
    Q35A: float = Field(..., ge=0, le=10)
    Q36A: float = Field(..., ge=0, le=10)
    Q38A: float = Field(..., ge=0, le=10)
    Q38B: float = Field(..., ge=0, le=10)
    Q38C: float = Field(..., ge=0, le=10)


# In[5]:


app = FastAPI(
    title = 'Governance Duration Prediction api',
    description = 'prediction of the strength and duration of the governance based on survey feature from citizens',
)


# In[6]:


# define app to run on anything(add CORSmiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # allow request from any domain
    allow_credentials=True,  #allow cookies and headers
    allow_methods=["*"], # allow all http methods
    allow_headers=["*"], #allow any header
)


# In[ ]:


# post the model( endpoint prediction)
@app.post('/predict')
def predict_governance(data:GovernanceInput):
    # convert input  form pydantic data to list values
    input_data = [[
        data.Q20, data.Q21A, data.Q24, data.Q34A,
        data.Q26, data.Q28,
        data.Q32A, data.Q32B,
        data.Q48A, data.Q48B,
        data.Q50A, data.Q50B, data.Q50C,
        data.Q51A, data.Q51B,
        data.Q53A, data.Q53B, data.Q53C,
        data.Q35A, data.Q36A,
        data.Q38A, data.Q38B, data.Q38C
    ]]
    # predict and return it
    prediction = model.predict(input_data)
    return{"Governement duration prediction":prediction[0]}

