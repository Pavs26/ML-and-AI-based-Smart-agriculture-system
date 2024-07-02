import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Waiter Performance Analysis")

# Sample data generation
waiters = ["Alice", "Bob", "Charlie", "David", "Eva"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Generating a sample dataframe for waiter tips collected each day
np.random.seed(42)  # For reproducibility
data = {
    waiter: np.random.randint(50, 200, size=7) for waiter in waiters
}
data["Day"] = days
df_tips = pd.DataFrame(data)

# Generating a sample dataframe for waiter ratings out of 5 each day
data_ratings = {
    waiter: np.random.choice([3, 4, 4.5, 5], size=7) for waiter in waiters
}
data_ratings["Day"] = days
df_ratings = pd.DataFrame(data_ratings)

# Waiter selection
selected_waiter = st.selectbox("Select a Waiter:", waiters)

# Plotting tips for the selected waiter
st.subheader(f"Daily Tips for {selected_waiter}")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=df_tips, x="Day", y=selected_waiter, marker="o", ax=ax)
plt.title(f"Daily Tips for {selected_waiter}")
plt.ylabel("Tips ($)")
st.pyplot(fig)

# Plotting ratings for the selected waiter
st.subheader(f"Daily Ratings for {selected_waiter}")
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(data=df_ratings, x="Day", y=selected_waiter, marker="o", ax=ax)
plt.title(f"Daily Ratings for {selected_waiter}")
plt.ylabel("Rating (out of 5)")
plt.ylim(2.5, 5)
st.pyplot(fig)

# Overall tips comparison among all waiters
st.subheader("Overall Tips Comparison")
fig, ax = plt.subplots(figsize=(10, 5))
df_tips_melted = df_tips.melt(id_vars=["Day"], value_vars=waiters)
sns.barplot(data=df_tips_melted, x="variable", y="value", ax=ax, ci=None)
plt.title("Total Tips for Each Waiter")
plt.xlabel("Waiter")
plt.ylabel("Total Tips ($)")
st.pyplot(fig)

# Overall ratings comparison among all waiters
st.subheader("Overall Ratings Comparison")
fig, ax = plt.subplots(figsize=(10, 5))
df_ratings_melted = df_ratings.melt(id_vars=["Day"], value_vars=waiters)
sns.boxplot(data=df_ratings_melted, x="variable", y="value", ax=ax)
plt.title("Distribution of Ratings for Each Waiter")
plt.xlabel("Waiter")
plt.ylabel("Rating (out of 5)")
st.pyplot(fig)

# Correlation between Tips and Ratings
st.subheader("Correlation between Tips and Ratings")
df_corr = pd.concat([df_tips[selected_waiter], df_ratings[selected_waiter]], axis=1)
df_corr.columns = ["Tips", "Rating"]
fig, ax = plt.subplots(figsize=(8, 6))
sns.scatterplot(data=df_corr, x="Tips", y="Rating", ax=ax)
sns.regplot(data=df_corr, x="Tips", y="Rating", ax=ax, scatter=False)
plt.title(f"Correlation between Tips and Ratings for {selected_waiter}")
st.pyplot(fig)
