#Social Media Sentiment Analysis Dashboard

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Data%20Viz-Plotly-3F4F75.svg)](https://plotly.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An interactive, data-driven Natural Language Processing (NLP) dashboard built to analyze and visualize public sentiment from social media feeds. This application processes a real-world Twitter dataset containing over 74,000 records, allowing users to drill down into specific brands, products, or gaming entities to evaluate public perception trends.

---

##Key Features

* **Real-time Text Predictor:** Input any custom sentence or tweet to instantly compute its NLP sentiment polarity score.
* **Granular Entity Filtering:** Dynamically filter and analyze tweets linked to major corporate and gaming brands (e.g., *Nvidia, Microsoft, Borderlands, Amazon*).
* **Interactive Data Tables:** View structured, sanitized tweet data on demand with memory-optimized rendering.
* **Dynamic Visual Analytics:** Real-time distribution parsing rendered natively using interactive, color-mapped Plotly pie charts.

---

##Architecture & Tech Stack

The application leverages a modular "Local-First" architecture designed for high-throughput localized data analysis without heavy infrastructure overhead:

* **UI Framework:** [Streamlit](https://streamlit.io/) (High-performance analytical web interface)
* **Data Processing:** [Pandas](https://pandas.pydata.org/) (Data cleaning, dropping null constraints, and dynamic filtering)
* **Visualization:** [Plotly Express](https://plotly.com/python/) (Client-side interactive charting)
* **NLP Processing Engine:** [TextBlob](https://textblob.readthedocs.io/) (Lexicon-based algorithmic sentiment tracking)

---

##Local Setup & Execution

### Prerequisites
Ensure you have Python 3.13+ installed on your system. 
2. Dataset Placement
Make sure your downloaded Kaggle dataset file is renamed to twitter_training.csv and placed directly into the root folder of the project.

3. Install Dependencies
Install all the required production libraries via pip3:

Bash
pip3 install -r requirements.txt
4. Run the Application
Launch the Streamlit analytical server:

Bash
python3 -m streamlit run app.py
Your terminal will initialize the engine and automatically launch a browser tab at http://localhost:8501.

Dataset Reference
The underlying unstructured data is sourced from the Twitter Sentiment Analysis dataset on Kaggle.

Total Rows: ~74,682 instances

Data Fields Included: Tweet_ID, Entity (Brand/Topic), Sentiment (Ground Truth Label), and Tweet_Text.

Optimization Note: While the interactive charts process the entire scope of the loaded data for accuracy, the frontend data preview is intelligently capped at the top 100 entries to prevent browser-side script latency.
