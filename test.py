import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import numpy as np

st.set_page_config(page_title="Env Sanity Check", layout="centered")

st.title("🎉 Virtual Environment Sanity Check")
st.write("If you can see this app and the plot below, your libraries are installed correctly!")

# Create fake data
np.random.seed(42)
data = pd.DataFrame({
    "x": np.arange(50),
    "y": np.random.randn(50).cumsum(),
    "category": np.random.choice(["A", "B", "C"], size=50)
})

st.subheader("📊 Sample Data")
st.dataframe(data.head())

# Plot using seaborn + matplotlib
fig, ax = plt.subplots()
sns.lineplot(data=data, x="x", y="y", hue="category", ax=ax)
ax.set_title("Random Walk by Category")

st.pyplot(fig)

st.success("✅ All libraries imported and working!")
st.balloons()
