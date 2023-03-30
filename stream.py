import streamlit as st
import pandas as pd
import plotly.express as px



st.title("Kaliyasot Dam Visualization Tool")
kalia=pd.read_csv("ProcessedKaliyasotAllParams.csv")
def dataset():
    st.header("this is the dataset")
    
    st.write(kalia.head())
    st.header("this is the histogram")
    fig = px.histogram(kalia, y=["ndwi", "mndwi", "ndci", "ndti", "do", "ph", "chl_a", "ssc", "wst"], title="Range of Data Collected", x=kalia["date"])
    st.write(fig)
def boxplot():
    st.header("Outlier Detection")
    st.text("A good way to know the range of data and outliers in the data is by a boxplot.")
    fig = px.box(kalia,  x=["wst","chl_a"] , title="Outlier Detection of chl_a and wst", points="all",boxmode="group")
    st.write(fig)
    fig = px.box(kalia,  x=["ph"] , title="Outlier Detection of pH", points="all",boxmode="group")
    st.write(fig)
    fig = px.box(kalia,  x=["ssc"] , title="Outlier Detection of SSC", points="all",boxmode="group")
    st.write(fig)
    fig = px.box(kalia,  x=["ndwi", "mndwi","do", "ndci", "ndti"] , title="Outlier Detection of Normalised Water Parameters (and DO)", points="all",boxmode="group")
    st.write(fig)
def insights():
    st.header("Insights")
    st.markdown("Correct asymptotic trends seen in between NDCI and temperature since chloropyhll content reaches saturation after a certain temperature.")
    st.markdown("Correct relation between ssc and ndti (both calculate the sedimentation in water body.")
    st.markdown("Correct Positive correlations between pH and NDCI. Chlorophyll does not like acidic conditions. It has an optimum pH range of 7-8.")
    st.markdown("Unexplainable Positive relation between NDTI and DO now explained thanks to Aniruddha and his peers' Work. Turbidity is exactly the opposite of what's showing in the data as more -ve means less turbid (vice-versa) and that's why we need to understand the in-depth of it's property.")
    st.markdown("Some very interesting relations are seen in between the parameters of SSC and Dissolved Oxygen. Typically it is seen that SSC and DO have a negative correlation, but it would seem that in our data, there is a posistive correlation. This seemed confusing in the beginning, but then we looked at other correlations. We noticed the correlations between SSC and Chl-a. There is a significant positive correlation. Chl-a concentration is often used in water quality assessments to determine the amount of phytoplankton in the water. The presence of phytoplanktons in the water increases the Dissolved oxygen amount. Moreover the presence of phytoplanktons are also being picked up on the SSC readings.")
    st.markdown("While looking for correlations between SSC and NDCI and Chl-a Concentration, I noticed something. There seems to be a +ve correlation between chl-a and SSC but a very strong -ve correlation between SSC and NDCI. I was surprised at first since both chl-a and NDCI are factors for chlorophyll content. But there may be an explanation for this. chl-a computes the concentration of chlorophyll-a only. But NDCI is a measurement of other pigments with respect to chlorophyll-a. So maybe since the correlation of chl-a to SSC may be positive, the relation of NDCI(other pigment wrt chlorophyll-a) may be negative. This may be further indicated by the negative correlation between the NDCI and Chl-a concentration.")
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
def scatterplot():
    st.header("Final Scatterplot Matrix showing all relations between parameters")
    fig = px.scatter_matrix(kalia, dimensions=["ndwi", "mndwi", "ndci", "ndti", "do", "ph", "chl_a", "ssc", "wst"], color='date')
    fig.update_layout(width=1000,height=800,plot_bgcolor='lightgrey')
    st.write(fig)

page_names_to_funcs = {
    "Dataset": dataset,
    "Outlier Detection": boxplot,
    "Insights": insights,
    "Scatterplot":scatterplot,
}
selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
