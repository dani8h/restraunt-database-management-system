import datetime

import pandas as pd
import streamlit as st
from database import view_all_data, view_only_dealer_names, get_dealer, edit_dealer_data


def update():
    result = view_all_data()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Dealer ID', 'Dealer Name', 'Dealer City', 'Dealer Pin', 'Dealer Street'])
    with st.expander("Current Dealers"):
        st.dataframe(df)
    list_of_dealers = [i[0] for i in view_only_dealer_names()]
    selected_dealer = st.selectbox("Dealer to Edit", list_of_dealers)
    selected_result = get_dealer(selected_dealer)
    # st.write(selected_result)
    if selected_result:
        dealer_id = selected_result[0][0]
        dealer_name = selected_result[0][1]
        dealer_city = selected_result[0][2]
        dealer_pin = selected_result[0][3]
        dealer_street = selected_result[0][4]

        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_dealer_id = st.text_input("ID:", dealer_id)
            new_dealer_name = st.text_input("Name:", dealer_name)
        with col2:
            new_dealer_city = st.selectbox(dealer_city, ["Bangalore", "Chennai", "Mumbai"])
            new_dealer_pin = st.text_input("Pin Code:", dealer_pin)
        new_dealer_street = st.text_input("Street Name:", dealer_street)
        if st.button("Update Dealer"):
            edit_dealer_data(new_dealer_id, new_dealer_name, new_dealer_city, new_dealer_pin, new_dealer_street, dealer_id, dealer_name, dealer_city, dealer_pin, dealer_street)
            st.success("Successfully updated:: {} to ::{}".format(dealer_name, new_dealer_name))

    result2 = view_all_data()
    df2 = pd.DataFrame(result2, columns=['Dealer ID', 'Dealer Name', 'Dealer City', 'Dealer Pin', 'Dealer Street'])
    with st.expander("Updated data"):
        st.dataframe(df2)
