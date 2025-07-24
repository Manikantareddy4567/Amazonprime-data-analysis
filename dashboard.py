import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud
from itertools import combinations

st.set_page_config(layout="wide", page_title="Prime Video Dashboard")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("prime_cleaned.csv")
    return df

df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
selected_type = st.sidebar.multiselect("Type", df['type'].dropna().unique(), default=df['type'].dropna().unique())
selected_years = st.sidebar.slider("Release Year", int(df['release_year'].min()), int(df['release_year'].max()), 
                                   (int(df['release_year'].min()), int(df['release_year'].max())))

# Apply filters
filtered_df = df[(df['type'].isin(selected_type)) & 
                 (df['release_year'].between(selected_years[0], selected_years[1]))]

st.title("Prime Video EDA Dashboard")

# 1. Distribution by Type
st.subheader("Content Type Distribution")
fig, ax = plt.subplots()
sns.countplot(data=filtered_df, x='type', ax=ax)
st.pyplot(fig)

# 2. Titles by Release Year
st.subheader("Titles by Release Year")
fig, ax = plt.subplots(figsize=(12, 5))
sns.histplot(filtered_df['release_year'], bins=30, ax=ax)
st.pyplot(fig)

# 3. Top Genres
st.subheader("Top 10 Genres")
genres = filtered_df['listed_in'].dropna().str.split(', ')
flat_genres = [g for sublist in genres for g in sublist]
top_genres = pd.Series(Counter(flat_genres)).nlargest(10)
st.bar_chart(top_genres)

# 4. WordCloud of Descriptions
st.subheader("Common Words in Descriptions")
text = " ".join(filtered_df['description'].dropna())
wordcloud = WordCloud(width=1200, height=600, background_color='white').generate(text)
fig, ax = plt.subplots(figsize=(10, 5))
ax.imshow(wordcloud, interpolation='bilinear')
ax.axis('off')
st.pyplot(fig)

# 5. Genre Co-occurrence Heatmap (advanced)
st.subheader("Genre Co-occurrence Heatmap")
genres_series = filtered_df['listed_in'].dropna().str.split(', ')
all_genres = sorted(set([g for sub in genres_series for g in sub]))
matrix = pd.DataFrame(0, index=all_genres, columns=all_genres)
for genres in genres_series:
    for g1, g2 in combinations(genres, 2):
        matrix.loc[g1, g2] += 1
        matrix.loc[g2, g1] += 1
fig, ax = plt.subplots(figsize=(12, 10))
sns.heatmap(matrix, cmap="Blues", ax=ax)
st.pyplot(fig)

# 6. Data Table
st.subheader("Filtered Dataset")
st.dataframe(filtered_df)
