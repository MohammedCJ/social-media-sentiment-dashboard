import streamlit as st
import pandas as pd
import plotly.express as px
from textblob import TextBlob


st.set_page_config(page_title="Social Media Sentiment Dashboard", layout="wide")


st.title("Social Media Sentiment Analysis Dashboard")
st.markdown("An interactive application analyzing real-world public sentiment data from Kaggle.")

st.markdown("---")

st.subheader("Real-time Text Analysis")
user_input = st.text_input("Type any text or tweet in English to analyze its sentiment on the fly:", "I really love this product, it's absolutely amazing!")

if user_input:
    
    blob = TextBlob(user_input)
    polarity = blob.sentiment.polarity
    
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
        
    st.write(f"**Predicted Sentiment:** {sentiment} | **Polarity Score:** {polarity:.2f}")

st.markdown("---")


st.subheader("Kaggle Twitter Dataset Exploration")

@st.cache_data
def load_data():
    
    df = pd.read_csv("twitter_training.csv", header=None, names=['Tweet_ID', 'Entity', 'Sentiment', 'Tweet_Text'])
    
    df = df.dropna(subset=['Tweet_Text'])
    return df

try:
    df = load_data()
    
    
    entities = sorted(df['Entity'].unique())
    selected_entity = st.selectbox("Select a Brand / Entity to filter the data:", entities)
    
  
    filtered_df = df[df['Entity'] == selected_entity]
    
   
    col1, col2 = st.columns(2)
    
    with col1:
        st.write(f"**Sample Tweets for ({selected_entity}):**")
      
        st.dataframe(filtered_df[['Tweet_Text', 'Sentiment']].head(100).reset_index(drop=True), use_container_width=True)
        
    with col2:
        st.write(f"**Overall Sentiment Distribution for ({selected_entity}):**")
        
       
        sentiment_counts = filtered_df['Sentiment'].value_counts().reset_index()
        sentiment_counts.columns = ['Sentiment', 'Count']
        
        
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
    st.error("E'twitter_training.csv' not found. Please ensure the dataset is placed directly in the project directory.")
