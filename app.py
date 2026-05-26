import streamlit as st
import pandas as pd
import plotly.express as px
from textblob import TextBlob

# Page configuration for a professional wide layout
st.set_page_config(page_title="Social Media Sentiment Dashboard", layout="wide")

# Dashboard Header
st.title("📊 Social Media Sentiment Analysis Dashboard")
st.markdown("An interactive application analyzing real-world public sentiment data from Kaggle.")

st.markdown("---")

# --- PART 1: Real-time Live Sentiment Predictor ---
st.subheader("🔍 Real-time Text Analysis")
user_input = st.text_input("Type any text or tweet in English to analyze its sentiment on the fly:", "I really love this product, it's absolutely amazing!")

if user_input:
    # Analyze text using TextBlob
    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity
    
    if polarity > 0:
        sentiment = "🟢 Positive"
    elif polarity < 0:
        sentiment = "🔴 Negative"
    else:
        sentiment = "🟡 Neutral"
        
    st.write(f"**Predicted Sentiment:** {sentiment} | **Polarity Score:** {polarity:.2f}")

st.markdown("---")

# --- PART 2: Bulk Dataset Exploration ---
st.subheader("📈 Kaggle Twitter Dataset Exploration")

@st.cache_data # Caches data in memory to ensure fast performance
def load_data():
    # Read the dataset and manually assign headers since the raw file doesn't have them
    df = pd.read_csv("twitter_training.csv", header=None, names=['Tweet_ID', 'Entity', 'Sentiment', 'Tweet_Text'])
    # Drop rows where the tweet text column is missing
    df = df.dropna(subset=['Tweet_Text'])
    return df

try:
    df = load_data()
    
    # Extract unique corporate or gaming brands/entities for the filter dropdown
    entities = sorted(df['Entity'].unique())
    selected_entity = st.selectbox("Select a Brand / Entity to filter the data:", entities)
    
    # Filter dataset based on selection
    filtered_df = df[df['Entity'] == selected_entity]
    
    # Create two equal columns for a balanced dashboard layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.write(f"**Sample Tweets for ({selected_entity}):**")
        # Display the first 100 rows to keep the UI snappy and readable
        st.dataframe(filtered_df[['Tweet_Text', 'Sentiment']].head(100).reset_index(drop=True), use_container_width=True)
        
    with col2:
        st.write(f"**Overall Sentiment Distribution for ({selected_entity}):**")
        
        # Calculate frequencies of each sentiment label
        sentiment_counts = filtered_df['Sentiment'].value_counts().reset_index()
        sentiment_counts.columns = ['Sentiment', 'Count']
        
        # Build an interactive Plotly Pie Chart
        fig = px.pie(
            sentiment_counts, 
            values='Count', 
            names='Sentiment',
            color='Sentiment',
            color_discrete_map={
                'Positive': '#2ca02c', 
                'Negative': '#d62728', 
                'Neutral': '#7f7f7f', 
                'Irrelevant': '#bcbd22'
            }
        )
        st.plotly_chart(fig, use_container_width=True)

except FileNotFoundError:
    st.error("⚠️ 'twitter_training.csv' not found. Please ensure the dataset is placed directly in the project directory.")