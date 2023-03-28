import streamlit as st
import pandas as pd
import plotly.express as px

header= st.container()
eda=st.container()
scatterplot=st.container()
scatterplot.markdown(
    f"""
    <style>
    .main_container {{
        display: flex;
        justify-content: center;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)
with header:
    st.text("HALLO!")

with eda:
    st.header("this is the dataset")
    kalia=pd.read_csv("C:\\Users\\utfu\\Desktop\\EDA frontend\\data\\ProcessedKaliyasotAllParams.csv")
    st.write(kalia.head())
    st.header("this is the histogram")
    fig = px.histogram(kalia, y=["ndwi", "mndwi", "ndci", "ndti", "do", "ph", "chl_a", "ssc", "wst"], title="Range of Data Collected", x=kalia["date"])
    st.write(fig)
    st.header("Outlier Detection")
    fig = px.box(kalia,  x=["wst","chl_a"] , title="Outlier Detection of chl_a and wst", points="all",boxmode="group")
    st.write(fig)
    fig = px.box(kalia,  x=["ph"] , title="Outlier Detection of pH", points="all",boxmode="group")
    st.write(fig)
    fig = px.box(kalia,  x=["ssc"] , title="Outlier Detection of SSC", points="all",boxmode="group")
    st.write(fig)
    st.header("Inter-parameter Correlation Insights")
    fig = px.scatter(kalia, x="do",title="DO vs NDCI" ,y="ndci")
    st.write(fig)
    fig = px.scatter(kalia, x="ndti",title="NDTI vs NDCI", y="ndci")
    st.write(fig)
    fig = px.scatter(kalia, x="wst",title="WST vs NDCI" ,y="ndci")
    st.write(fig)
    fig = px.scatter(kalia, x="ph", title="pH vs NDCI",y="ndci")
    st.write(fig)
    fig = px.scatter(kalia, x="chl_a",title="CHl-a vs SSC", y="ssc")
    st.write(fig)
with scatterplot:
    fig = px.scatter_matrix(kalia, dimensions=["ndwi", "mndwi", "ndci", "ndti", "do", "ph", "chl_a", "ssc", "wst"], color='date')
    fig.update_layout(width=1000,height=800,plot_bgcolor='lightgrey')
    st.write(fig)