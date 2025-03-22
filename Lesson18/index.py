import pandas as pd
import streamlit as st
import plotly as px
from numpy.ma.extras import average

st.header('Displaying DataFrames')

Data = pd.DataFrame({
    'Name': ['Alice', 'Michael', 'Andy'],
    'Age': [20, 58, 13],
    'City': ['London', 'Miami', 'New York']  # Correct order of cities
})


print(Data)

books_df = pd.read_csv('Lesson18/bestsellers_with_categories_2022_03_27.csv')

st.title('Bestselling Books Analysis')
st.write('This app analysis the amaznon top selling books from 2009 to 2022')

st.subheader("Summary Statistics")
total_books = books_df.shape[0]
unique_titles = books_df['Name'].nunique()
average_rating = books_df['User Rating'].mean()
average_price = books_df['Price'].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Books", total_books)
col2.metric("Unique Titles", unique_titles)
col3.metric("Average Rating", average_rating)
col4.metric("Average Price", average_price)

st.subheader("Summary Statistics")
st.write(f"Total Books: {total_books}")
st.write(f"Unique Titles: {unique_titles}")
st.write("Average Rating", f"{average_rating:.2f}")
st.write(f"Average Price: {average_price:.2f}")

st.subheader("Dataset Preview")
st.write(books_df.head())

col1, col2 = st.columns([1, 2])


with col1:
    st.subheader("Top 10 Book Titles")
    top_titles = books_df['Name'].head(10)
    st.bar_chart(top_titles)

    with col2:
        st.subheader("Top 10 Authors")
        top_authors = books_df['Author'].value_counts().head(10)
        st.bar_chart(top_titles)

st.subheader("Genre Distribution")
fig= px.pie(books_df, names='Genre', title='Most liked genre (2009 - 2022)', color='Genre', color_discreate_sequence=px.color.sequential.Plasma)
st.plotly_chart(fig)



