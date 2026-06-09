import streamlit as st
import json
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

try:
    from stringIO import StringIO
except ImportError:
    from io import StringIO

st.title("pytopia dashboard")

with st.expander('Statistics'):
    fig, ax = plt.subplots(1, 1, figsize=(10, 5))
    sns.histplot(np.random.randn(100), ax=ax)
    st.pyplot(fig)



