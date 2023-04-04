import streamlit as st
from data import get_data

st.set_page_config(page_title="Level", layout="wide")


def main():
    st.title("Subscription")
    st.header("Upload your Excel File here:")
    excel_file = st.file_uploader("", key="doc_file", type=['.xlsx'])
    if excel_file is not None:
        monthly, weekly, yearly = get_data(excel_file)
        st.subheader(f"Weekly Active: {weekly}")
        st.subheader(f"Monthly Active: {monthly}")
        st.subheader(f"Yearly Active: {yearly}")


if __name__ == '__main__':
    main()
