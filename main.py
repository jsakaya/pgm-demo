import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

# Set page config for a wide layout and custom theme
st.set_page_config(layout="wide", page_title="NumPyro Model Dashboard", page_icon="📊")

# Custom CSS to enhance the layout and make it look slick and glossy
st.markdown("""
    <style>
    .stApp {
        background-color: #f0f2f6;
        font-family: 'Arial', sans-serif;
    }
    .stTabs {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .stTab {
        background-color: #f8f9fa;
        color: #495057;
        border-radius: 5px;
        padding: 10px 20px;
        font-weight: 600;
    }
    .stTab[data-baseweb="tab"][aria-selected="true"] {
        background-color: #007bff;
        color: white;
    }
    .stButton>button {
        background-color: #007bff;
        color: white;
        border-radius: 5px;
        border: none;
        padding: 10px 24px;
        font-weight: 600;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    .css-1aumxhk {
        font-weight: 700;
        font-size: 1.5rem;
        color: #333333;
        padding-top: 1rem;
        padding-bottom: 0.5rem;
    }
    .css-1n76uvr {
        padding: 0.75rem;
        border-radius: 10px;
        background-color: #007bff;
        color: white;
        box-shadow: 0px 5px 15px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    .stDataFrame {
        border: 1px solid #ddd;
        border-radius: 5px;
        overflow: hidden;
    }
    .stDataFrame>div {
        border-radius: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# Main app title
st.title("NumPyro Model Dashboard")

# Sidebar with improved style
st.sidebar.title("Model Controls")
model_type = st.sidebar.selectbox("Select Model", ["MMM", "Healthcare", "Finance"])
analysis_type = st.sidebar.selectbox("Select Analysis", [
    "Model", "Learning", "Relationships", 
    "Conditioning/Whatif", "Scoring", 
    "Prediction/Forecasting", "Optimization"
])

# Function to create sidebar controls based on selected analysis
def create_sidebar_controls(analysis_type):
    if analysis_type == "Model":
        st.sidebar.slider("Number of parameters", 1, 10, 5)
        st.sidebar.selectbox("Distribution type", ["Normal", "Poisson", "Gamma"])
    elif analysis_type == "Learning":
        st.sidebar.slider("Number of iterations", 1000, 10000, 5000)
        st.sidebar.slider("Warmup steps", 100, 1000, 500)
    # Add more controls for other analysis types as needed

# Call the function to create sidebar controls
create_sidebar_controls(analysis_type)

# Function to create dummy plots (replace with actual model results later)
def create_dummy_plot():
    fig = go.Figure()
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', line=dict(color='blue', width=3)))
    fig.update_layout(
        title="Sample Plot",
        xaxis_title="X Axis",
        yaxis_title="Y Axis",
        template="plotly_white",
        title_font=dict(size=20, color='black'),
        xaxis=dict(showline=True, showgrid=False),
        yaxis=dict(showline=True, showgrid=False),
    )
    return fig

# Main content with improved layout and design
st.header(f"{model_type} Model - {analysis_type} Analysis")

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(create_dummy_plot(), use_container_width=True)

with col2:
    st.write(f"This is where the {analysis_type} analysis for the {model_type} model will be displayed.")
    st.write("Key metrics and insights will be shown here.")
    
    # Add a sample data table with enhanced styling
    df = pd.DataFrame(
        np.random.randn(10, 5),
        columns=('col %d' % i for i in range(5))
    )
    st.dataframe(df.style.highlight_max(axis=0, color="yellow").highlight_min(axis=0, color="lightblue"))

# Footer with improved styling
st.markdown("---")
st.markdown("<div style='text-align: center; font-size: 0.8rem;'>© 2024 Your Company Name. All rights reserved.</div>", unsafe_allow_html=True)
