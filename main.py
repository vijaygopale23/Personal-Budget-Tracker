import streamlit as st
from datetime import datetime
from db.database import (
    init_db, insert_expense, get_expenses, reset_month_data,
    set_budget_limit, get_budget_limit, get_total_spent,
    save_user_profile, get_user_profile
)
from utils.helpers import (
    get_current_month, generate_pie_chart, generate_calendar_view,
    generate_bar_chart_daily, generate_bar_chart_monthly, download_expenses_csv
)

# Initialize DB on app start
init_db()

# Session State
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user_name = ""
    st.session_state.profile_pic = ""

# Login Section
if not st.session_state.logged_in:
    st.title("🔐 Welcome to Personal Budget Tracker")
    st.subheader("Please login to continue.")
    name = st.text_input("Enter your name")
    pic = st.file_uploader("Upload profile picture (optional)", type=["png", "jpg", "jpeg"])

    if st.button("Login"):
        filename = "assets/default_profile.png"
        if pic:
            filename = f"assets/{name.lower()}_pic.png"
            with open(filename, "wb") as f:
                f.write(pic.getbuffer())
        save_user_profile(name, filename)
        st.session_state.logged_in = True
        st.session_state.user_name = name
        st.session_state.profile_pic = filename
        st.success("Login successful! Reloading...")
        st.rerun()
    st.stop()

# Sidebar Layout
with st.sidebar:
    st.image(st.session_state.profile_pic, width=100)
    st.write(f"Hello, *{st.session_state.user_name}* 👋")

    menu = st.radio("Navigate", ["Dashboard", "Add Expense", "Expense Report", "Calendar View"])
    st.markdown("---")
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

# Main App UI
current_month = get_current_month()
expenses = get_expenses(current_month)

if menu == "Dashboard":
    st.title("📊 Dashboard")

    today_str = datetime.today().strftime("%Y-%m-%d")
    today_expenses = [e for e in expenses if e[4] == today_str]
    today_total = sum(e[2] for e in today_expenses)

    st.metric("🕒 Today's Spending", f"₹{today_total:.2f}")

    total_spent = get_total_spent(current_month)
    limit = get_budget_limit(current_month)

    st.metric("💸 Total Spent This Month", f"₹{total_spent:.2f}")
    if limit:
        st.metric("🚦 Budget Limit", f"₹{limit:.2f}")
        if total_spent > limit:
            st.error("⚠ You have exceeded your budget!")

    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(generate_pie_chart(expenses), use_container_width=True)
    with col2:
        st.plotly_chart(generate_bar_chart_daily(expenses), use_container_width=True)

    st.markdown("### 📅 Monthly Overview")
    st.plotly_chart(generate_bar_chart_monthly(get_expenses()), use_container_width=True)

    st.markdown("---")
    if st.button("🔄 Reset This Month's Data"):
        reset_month_data(current_month)
        st.success("Monthly data reset!")
        st.rerun()

elif menu == "Add Expense":
    st.title("➕ Add Expense")
    col1, col2 = st.columns(2)

    with col1:
        category = st.selectbox("Select Category", [
            "Food", "Travel", "Entertainment", "Groceries", "Electricity Bill",
            "Water Bill", "Internet", "Education", "Rent/Hostel"
        ])
        amount = st.number_input("Enter amount", min_value=0.0)

    with col2:
        type = st.selectbox("Type", ["Daily", "Monthly"])
        date = st.date_input("Date", value=datetime.today())

    if st.button("Add"):
        insert_expense(category, amount, type, str(date))
        st.success("Expense added!")

    st.markdown("---")
    st.subheader("🛑 Set Monthly Budget Limit")
    limit_val = st.number_input("Enter limit", min_value=0.0)
    if st.button("Save Limit"):
        set_budget_limit(limit_val, current_month)
        st.success("Budget limit saved!")

elif menu == "Expense Report":
    st.title("📄 Expense Report")

    tabs = st.tabs(["📅 Daily Reports", "📆 Monthly Summary", "📥 Download Data"])

    with tabs[0]:
        for e in expenses:
            st.write(f"🗓 {e[4]} - {e[1]}: ₹{e[2]} ({e[3]})")

    with tabs[1]:
        df = {}
        for e in expenses:
            df.setdefault(e[5], 0)
            df[e[5]] += e[2]
        for month, amt in df.items():
            st.write(f"📆 {month}: ₹{amt}")

    with tabs[2]:
        csv_data = download_expenses_csv(expenses)
        st.download_button("⬇️ Download CSV", data=csv_data, file_name="expenses_report.csv", mime="text/csv")

elif menu == "Calendar View":
    st.title("📆 Calendar Mode")
    generate_calendar_view(expenses, current_month)
