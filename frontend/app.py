# Importing pakages
import streamlit as st
from create import *
from home import *

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="password"
# )
# c = mydb.cursor()

# c.execute("CREATE DATABASE ebike")


def main():
    st.title("Restaurant Database Management System")
    menu = ["Home","View", "Add", "Edit order", "Place Order","Run Custom Query","Generate bill","View employees","Remove employees"]
    choice = st.sidebar.selectbox("Menu", menu)


    if choice == "Home":
        st.subheader("Database overview")
        Home()

    if(choice == "View"):
        option = st.selectbox('Select table to view',('chef','waiter','food_items','tables'))
        display(option)


    if choice == "Add":
        st.subheader("Add data to table")
        option = st.selectbox('Select table to view',('chef','waiter','food_items','tables'))
        display(option)
        vals = st.text_input('Add to table',placeholder= 'Enter tuples')
        if(st.button('Add')):
            addVal(option, vals)
    
    if choice == "Edit order":
        st.subheader("Edit your order")
        t_no = st.text_input('Enter table no')
        if(st.button('Show orders')):
            displayorder(t_no)
        vals = st.text_input('Edit value',placeholder='Enter values to be edited')
        if(st.button('Edit')):
            editOrder(vals)
        st.text('DONOT ADD PARENTHESIS HERE')
        st.text('Note: the key value for the tuple to be edited must remain the same')

    if choice == "Place Order":
        t_no = st.selectbox('Select table',('1','2','3','4','5','6','7','8'))
        display('food_items')
        f = st.text_input('Enter food id',key=121)
        q = st.text_input('Enter quantity',key=100)
        if(st.button('Place order')):
            placeorder(t_no, f, q)

    if choice == "Run Custom Query":
        st.text('Enter the query in the box below')
        q = st.text_input('Enter query')
        if(st.button('Run')):
            runquery(q)

    if choice == "Generate bill":
        st.subheader('Generate bill for table no')
        t_no = st.selectbox('Select table',('1','2','3','4','5','6','7','8'))
        if(st.button('Bill')):
            generatebill(t_no)

    if choice == "View employees":
        st.subheader('View of all the employees working for the restaurant')
        showview()
    

    if choice == "Remove employees":
        st.subheader('Remove employee')
        ans = st.selectbox('',("chef", "waiter"))
        if(ans == 'chef'):
            display('chef')
            eid = st.text_input('Enter employee id to be removed')
            if(st.button('Remove')):
                removechef(eid)
        if(ans == 'waiter'):
            display('waiter')
            eid = st.text_input('Enter employee id to be removed')
            if(st.button('Remove')):
                removewaiter(eid) 





if __name__ == '__main__':
    main()

