#!/usr/bin/env python
# coding: utf-8

# In[1]:


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import joblib
import pandas as pd
import numpy as np
import os
# from google.colab import drive


# In[ ]:


# drive.mount('/content/drive')


# In[ ]:


# load the best trained model
model_path = os.path.join(os.path.dirname(__file__), 'best_model.pkl')
model = joblib.load('best_model.pkl')


# In[4]:


class GovernanceInput(BaseModel):
    Q20: float = Field(..., ge=1.0, le=8.0, description="Experience of corruption?")
    Q21A: float = Field(..., ge=1.0, le=8.0, description="Trust in courts of law?")
    Q24: float = Field(..., ge=1.0, le=8.0, description="Preference for democracy?")
    Q34A: float = Field(..., ge=1.0, le=8.0, description="Gov’t handling of education?")
    Q26: float = Field(..., ge=1.0, le=8.0, description="Freedom to express views?")
    Q28: float = Field(..., ge=1.0, le=8.0, description="Media freedom from government?")
    Q32A: float = Field(..., ge=1.0, le=8.0, description="Fairness toward your ethnic group?")
    Q32B: float = Field(..., ge=1.0, le=8.0, description="Fairness toward other ethnic groups?")
    Q48A: float = Field(..., ge=1.0, le=8.0, description="Gov’t help during COVID?")
    Q48B: float = Field(..., ge=1.0, le=8.0, description="NGO help during COVID?")
    Q50A: float = Field(..., ge=1.0, le=8.0, description="Importance of top issue?")
    Q50B: float = Field(..., ge=1.0, le=8.0, description="Importance of second issue?")
    Q50C: float = Field(..., ge=1.0, le=8.0, description="Importance of third issue?")
    Q51A: float = Field(..., ge=1.0, le=8.0, description="Ease of getting IDs?")
    Q51B: float = Field(..., ge=1.0, le=8.0, description="Ease of school enrollment?")
    Q53A: float = Field(..., ge=1.0, le=8.0, description="Access to clean water?")
    Q53B: float = Field(..., ge=1.0, le=8.0, description="Access to toilet facilities?")
    Q53C: float = Field(..., ge=1.0, le=8.0, description="Access to medical services?")
    Q35A: float = Field(..., ge=1.0, le=8.0, description="Gov’t handling of economy?")
    Q36A: float = Field(..., ge=1.0, le=8.0, description="Gov’t addressing unemployment?")
    Q38A: float = Field(..., ge=1.0, le=8.0, description="Gov’t addressing poverty?")
    Q38B: float = Field(..., ge=1.0, le=8.0, description="Gov’t handling income inequality?")
    Q38C: float = Field(..., ge=1.0, le=8.0, description="Gov’t handling taxation fairness?")


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


# In[8]:


@app.get("/")
def read_root():
    return {"message": "Governance prediction API is live!"}


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

