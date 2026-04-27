import streamlit as st
import pandas as pd

st.title("Cloud Cost Intelligence Dashboard")

file_path = "data/sample_data.xlsx"

df = pd.read_excel(file_path)
df.columns = df.columns.str.strip().str.lower()
df['timestamp'] = pd.to_datetime(df['timestamp'], dayfirst=True)

df['total_cost'] = df['usage_hours'] * df['cost_per_hour']

st.subheader("Data Preview")
st.dataframe(df)

st.subheader("Total Cost")
st.write(df['total_cost'].sum())

st.subheader("Cost by Energy Type")
energy_cost = df.groupby('energy_type')['total_cost'].sum()
st.bar_chart(energy_cost)

st.subheader("Cost by Service")
service_cost = df.groupby('service')['total_cost'].sum()
st.bar_chart(service_cost)

st.subheader("Daily Cost Trend")
daily_cost = df.groupby(df['timestamp'].dt.date)['total_cost'].sum()
st.line_chart(daily_cost)

st.subheader("Weekly Usage")

weekly_usage = df.groupby(df['timestamp'].dt.to_period('W'))['usage_hours'].sum()
weekly_usage.index = weekly_usage.index.astype(str)

st.line_chart(weekly_usage)
st.dataframe(weekly_usage)

st.subheader("Monthly Usage")

monthly_usage = df.groupby(df['timestamp'].dt.to_period('M'))['usage_hours'].sum()
monthly_usage.index = monthly_usage.index.astype(str)

st.line_chart(monthly_usage)
st.dataframe(monthly_usage)

st.subheader("Anomalies")
threshold = df['total_cost'].mean() * 2
st.dataframe(df[df['total_cost'] > threshold])

st.subheader("Idle Resources")
st.dataframe(df[df['usage_hours'] < 1])
