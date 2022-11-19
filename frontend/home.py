import streamlit as st
import pandas as pd
from database import *

def Home():
    result=HomeData()
    df=pd.DataFrame(result,columns=["tables available"])
    st.dataframe(df)