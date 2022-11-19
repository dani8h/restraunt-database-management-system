import streamlit as st
import pandas as pd
import mysql.connector
from create import *

mydb=mysql.connector.connect(**st.secrets["mysql"])
c = mydb.cursor()

def show_table(table_name):
    c.execute('select * from ' + table_name)
    data=c.fetchall()
    return data


def HomeData():
    c.execute('show tables')
    data = c.fetchall()
    return data

#add values to the table
def addVal(o, v):

    q = 'INSERT INTO {}  VALUES {}'.format(o,v)
    c.execute(q)
    mydb.commit()
    st.success("value added successfully")


def displayorder(n):
    q = 'SELECT * FROM bill WHERE table_no = ' + str(n)
    c.execute(q)
    res = c.fetchall()
    df = pd.DataFrame(res, columns=['table_no','food_id','quality'])
    st.dataframe(df)


def editOrder(v):
    res = v.split(',')
    q = 'UPDATE bill set quantity =' + res[2] +' where table_no = '+ res[0] + ' AND f_id ='+ res[1]
    c.execute(q)
    mydb.commit()
    st.success('value successfully updated')

def runquery(a):
    c.execute(a)
    res = c.fetchall()
    df = pd.DataFrame(res)
    st.dataframe(df)
    st.success('query executed successfully')

def placeorder(t,f_id,quantity):
    q = 'INSERT INTO bill VALUES ({},{},{})'.format(t,f_id,quantity)
    c.execute(q)
    
    # c.execute('SELECT update_inventory({},{})'.format())
    mydb.commit()
    st.success('Placed order successfully')


def generatebill(n):
    cq = 'SELECT food_items.f_id, food_items.f_name,food_items.price, bill.quantity FROM bill join food_items where bill.f_id = food_items.f_id AND bill.table_no = '+n;
    c.execute(cq)
    nres = c.fetchall()
    df1 = pd.DataFrame(nres,columns=['food_id','food_name','price','quantity ordered'])
    st.dataframe(df1)
    q = 'SELECT bill.table_no, SUM(food_items.price) AS "total bill" from bill JOIN food_items where bill.table_no ='+n+' AND bill.f_id = food_items.f_id'
    c.execute(q)
    res = c.fetchall()
    df = pd.DataFrame(res,columns=['table_no','total amount'])
    st.dataframe(df)

def showingredients(id):
    q = 'SELECT ingredients.ingr_id, ingredients.ingr_name from ingredients JOIN recepie where ingredients.ingr_id = recepie.ingr_id AND f_id = '+ id
    c.execute(q)
    res = c.fetchall()
    return res

def showview():
    q = 'CREATE VIEW IF NOT EXISTS all_employees (emp_id, emp_name) AS SELECT chef.emp_id, chef.emp_name from chef UNION SELECT waiter.w_id, waiter.w_name from waiter'
    c.execute(q)
    c.execute('SELECT * from all_employees')
    res = c.fetchall()
    df = pd.DataFrame(res)
    st.dataframe(df)

def removechef(i):
    q = 'DELETE FROM chef where emp_id = '+i
    c.execute(q)
    mydb.commit()
    st.success('Employee removed')

def removewaiter(i):
    q = 'DELETE FROM waiter where w_id ='+i
    c.execute(q)
    mydb.commit()
    st.success('Employee removed')