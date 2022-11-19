import streamlit as st
import pandas as pd
from database import *


def display(table_name):
    result=show_table(table_name)
    if(table_name == "waiter"):
        df=pd.DataFrame(result,columns=["waiter id","waiter name","age"])
    if(table_name == "chef"):
        df = pd.DataFrame(result, columns=["emp_id","emp_name","age","head_id"])
        df['head_id']=df['head_id'].astype('Int64')
    if(table_name == "food_items"):
        df = pd.DataFrame(result, columns=["f_id","f_name","price","category","cuisine","prep_time"])
        st.dataframe(df)
        st.subheader('View ingredients')
        f_id = st.text_input('Enter food id')
        if(st.button('Show ingredients')):
            res = showingredients(f_id)
            df1 = pd.DataFrame(res)
            st.dataframe(df1)
        return
    if(table_name == "tables"):
        df = pd.DataFrame(result, columns=["table_no","capacity","reserved","w_id"])
    st.dataframe(df)


