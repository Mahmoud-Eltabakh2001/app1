
import streamlit as st
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
from ydata_profiling import ProfileReport

st.set_option('deprecation.showPyplotGlobalUse', False)

uploaded_file = st.file_uploader("Upload your walking data") #, type=["csv", "xlsx","txt"]

if uploaded_file is not None:   
    EDA_sample = pd.read_csv(uploaded_file)       #, index_col= 0
    st.write(EDA_sample)
    pr = ProfileReport(EDA_sample, explorative=True)
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)

else:
    st.info('Awaiting for CSV file to be uploaded.')
