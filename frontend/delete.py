import pandas as pd
import streamlit as st
from database import view_all_data, view_only_dealer_names, delete_data


def delete():
    result = view_all_data()
    df = pd.DataFrame(result, columns=['Dealer ID', 'Dealer Name', 'Dealer City', 'Dealer Pin', 'Dealer Street'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_dealers = [i[0] for i in view_only_dealer_names()]
    selected_dealer = st.selectbox("Task to Delete", list_of_dealers)
    st.warning("Do you want to delete ::{}".format(selected_dealer))
    if st.button("Delete Dealer"):
        delete_data(selected_dealer)
        st.success("Dealer has been deleted successfully")
    new_result = view_all_data()
    df2 = pd.DataFrame(new_result, columns=['Dealer ID', 'Dealer Name', 'Dealer City', 'Dealer Pin', 'Dealer Street'])
    with st.expander("Updated data"):
        st.dataframe(df2)