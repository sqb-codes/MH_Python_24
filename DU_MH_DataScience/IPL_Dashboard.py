import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("datasets/ipldata_19/matches.csv")

st.set_page_config(
    page_title="IPL Dashboard",
    layout="wide"
)

st.title("IPL Dataframe")

st.dataframe(df)

st.title("IPL Data Plots")

fig_1, fig_2 = st.columns(2)

with fig_1:
    st.markdown("Number of wins...")
    fig = px.bar(df["winner"])
    st.write(fig)

with fig_2:
    st.markdown("Number of matches in each season...")
    fig = px.bar(df["city"])
    st.write(fig)


# fig_3, fig_4 = st.columns(2)

# with fig_3:
#     st.markdown("Toss decision...")
#     value = pd.value_counts(df["toss_decision"])
#     fig = px.pie(df["toss_decision"], values=value, names=["field", "bat"])
#     st.plotly_chart(fig)
#     st.write(fig)

# with fig_4:
#     st.markdown("Results...")
#     values = pd.value_counts(df["result"])
#     fig = px.pie(df["result"], values=values, names=["normal", "tie", "no result"])
#     st.write(fig)