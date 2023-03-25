import streamlit as st
import pandas as pd
import numpy as np

st.markdown("""            
            <style>
            .css-1rs6os.edgvbvh3
            {
                visibility: hidden;
            }
            .css-1lsmgbg.egzxvld0
            {
                visibility: hidden;
            }
            </style>
            
            """,unsafe_allow_html=True)

st.markdown("""
                <!DOCTYPE html>
<html>
<head>
<title>AI Average</title>
</head>
<body>

<h1></h1>


</body>
</html
                """,unsafe_allow_html=True)

q  = st.file_uploader("Upload CSV",type=["xlsx"])
if q is not None:
    f = pd.read_excel(q)
    f=pd.DataFrame(f)
    st.dataframe(f)
    Average=[]
    for i in range(len(f)):
        arr=np.empty(3)
        arr = np.array(f.iloc[i][2:4])
        arr.sort()
        avg = (arr[-1]+arr[-2])/2
        Average.append(avg)
    f['Average']=Average
    st.markdown("<h1>Average of Mid Marks</h1>",unsafe_allow_html=True)
    st.dataframe(f)
    @st.cache
    def convert_df(f):

        return f.to_csv().encode('utf-8')

    csv = convert_df(f)

    st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='Average.csv',
    mime='text/csv',
    )