import calendar
from datetime import datetime
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from io import StringIO

def get_current_month():
    return datetime.now().strftime("%B-%Y")

def get_month_list():
    now = datetime.now()
    return [f"{calendar.month_name[i]}-{now.year}" for i in range(1, 13)]

def extract_day(date_str):
    return datetime.strptime(date_str, "%Y-%m-%d").day

def generate_pie_chart(expense_data):
    df = pd.DataFrame(expense_data, columns=["id", "category", "amount", "type", "date", "month"])
    if df.empty:
        fig = go.Figure()
        fig.update_layout(
            title="No data available for this chart.",
            annotations=[dict(text="No data", x=0.5, y=0.5, font_size=20, showarrow=False)]
        )
        return fig
    df_grouped = df.groupby("category")["amount"].sum().reset_index()
    fig = px.pie(df_grouped, names='category', values='amount', title='Category-wise Expense Distribution')
    return fig

def generate_bar_chart_daily(expense_data):
    df = pd.DataFrame(expense_data, columns=["id", "category", "amount", "type", "date", "month"])
    if df.empty:
        return go.Figure()
    df["date"] = pd.to_datetime(df["date"])
    df_grouped = df.groupby(df["date"].dt.date)["amount"].sum().reset_index()
    fig = px.bar(df_grouped, x="date", y="amount", title="Daily Spending This Month")
    return fig

def generate_bar_chart_monthly(expense_data):
    df = pd.DataFrame(expense_data, columns=["id", "category", "amount", "type", "date", "month"])
    if df.empty:
        return go.Figure()
    df_grouped = df.groupby("month")["amount"].sum().reset_index()
    fig = px.bar(df_grouped, x="month", y="amount", title="Monthly Spending Overview")
    return fig

def generate_calendar_view(expense_data, selected_month):
    df = pd.DataFrame(expense_data, columns=["id", "category", "amount", "type", "date", "month"])
    if df.empty:
        return st.info("No data available for this month.")
    
    df['date'] = pd.to_datetime(df['date'])
    df = df[df['month'] == selected_month]

    year = datetime.now().year
    month_num = datetime.strptime(selected_month, "%B-%Y").month
    total_monthly = df['amount'].sum()

    st.subheader(f"{selected_month} Calendar View — 💰 Total: ₹{total_monthly:.2f}")
    weeks = calendar.monthcalendar(year, month_num)

    for week in weeks:
        cols = st.columns(7)
        for i, day in enumerate(week):
            with cols[i]:
                if day != 0:
                    day_total = df[df['date'].dt.day == day]['amount'].sum()
                    st.markdown(f"**{day}**")
                    st.markdown(f"₹{day_total:.2f}")

def download_expenses_csv(expense_data):
    df = pd.DataFrame(expense_data, columns=["ID", "Category", "Amount", "Type", "Date", "Month"])
    output = StringIO()
    df.to_csv(output, index=False)
    return output.getvalue()
