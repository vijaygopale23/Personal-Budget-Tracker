# 💰 Personal Budget Tracker

> A Python-based Personal Budget Tracker built using **Streamlit** and **SQLite** that helps users manage their daily and monthly expenses through an interactive dashboard, detailed reports, and visual analytics.

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?logo=streamlit)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📖 Overview

Managing personal finances is one of the most important aspects of financial planning. Many people struggle to keep track of their daily expenses, resulting in poor budgeting and unnecessary spending.

The **Personal Budget Tracker** is a web-based application developed using **Python** and **Streamlit** that enables users to record, organize, analyze, and monitor their expenses efficiently. The application provides interactive visualizations, categorized expense tracking, monthly reports, calendar views, and automatic monthly data management.

The main objective of this project is to provide a simple, lightweight, and user-friendly expense management system suitable for students, professionals, and families.

---

# 🎯 Objectives

- Record daily expenses efficiently.
- Track monthly spending.
- Categorize expenses.
- Visualize spending patterns using charts.
- Generate daily and monthly reports.
- Help users make better financial decisions.
- Maintain expense history.
- Provide an intuitive user interface.

---

# ✨ Features

## 👤 User Management

- User Registration
- Secure Login System
- Profile Management
- Profile Picture Upload

---

## 💵 Expense Management

- Add Expenses
- Edit Expenses
- Delete Expenses
- Categorize Expenses
- Add Notes
- Select Expense Date

---

## 📊 Dashboard

- Today's Spending
- Monthly Spending
- Total Expenses
- Category-wise Summary
- Interactive Dashboard
- Expense Statistics

---

## 📈 Data Visualization

- Pie Chart
- Bar Chart
- Monthly Analysis
- Category-wise Analysis

---

## 📅 Calendar View

- View Expenses Date-wise
- Monthly Calendar Layout
- Quick Daily Expense Lookup

---

## 📑 Reports

- Daily Reports
- Monthly Reports
- Expense History
- Archived Monthly Records

---

## 🔄 Automation

- Automatic Monthly Reset
- Archive Previous Month Data
- Manual Reset Button

---

## 📤 Export

- Export Reports
- Download Expense Data

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | Web Application Framework |
| SQLite | Database |
| Pandas | Data Processing |
| Matplotlib | Data Visualization |
| Plotly | Interactive Charts |
| Datetime | Date Handling |
| Calendar | Calendar View |
| PIL | Image Handling |

---

# 🏗️ System Architecture

```
                 User

                   │

                   ▼

          Login / Registration

                   │

                   ▼

           User Authentication

                   │

                   ▼

            Dashboard

       ┌─────────┼──────────┐
       │         │          │
       ▼         ▼          ▼

 Add Expense  Reports   Calendar View

       │

       ▼

 SQLite Database

       │

       ▼

 Data Processing (Pandas)

       │

       ▼

 Visualization

       │

       ▼

 Dashboard & Reports
```

---

# 🔄 Workflow

1. User logs into the application.
2. Dashboard is displayed.
3. User adds expense details.
4. Expense is stored in SQLite Database.
5. Dashboard updates automatically.
6. Pie chart and reports are generated.
7. Calendar displays daily expenses.
8. At the start of every month:
   - Previous month's data is archived.
   - Dashboard resets automatically.
9. Users can export reports anytime.

---

# 📂 Project Structure

```
Personal-Budget-Tracker/
│
├── app.py
├── database.py
├── authentication.py
├── dashboard.py
├── reports.py
├── calendar_view.py
├── charts.py
├── utils.py
│
├── assets/
│   ├── images/
│   └── icons/
│
├── database/
│   └── budget.db
│
├── screenshots/
│
├── requirements.txt
│
├── README.md
│
└── LICENSE
```

---

# 🖥️ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/Personal-Budget-Tracker.git
```

Go into project folder

```bash
cd Personal-Budget-Tracker
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run Streamlit

```bash
streamlit run app.py
```

---

# 📷 Application Screenshots

## Login Page

(Add Screenshot Here)

---

## Dashboard

(Add Screenshot Here)

---

## Add Expense

(Add Screenshot Here)

---

## Pie Chart

(Add Screenshot Here)

---

## Calendar View

(Add Screenshot Here)

---

## Reports

(Add Screenshot Here)

---

# 📊 Database Design

The application uses **SQLite** for storing user and expense data.

### User Table

| Field | Type |
|--------|------|
| User ID | Integer |
| Username | Text |
| Password | Text |
| Profile Image | Blob |

### Expense Table

| Field | Type |
|--------|------|
| Expense ID | Integer |
| User ID | Integer |
| Amount | Float |
| Category | Text |
| Date | Date |
| Notes | Text |

---

# 🧠 Key Functionalities

- User Authentication
- Expense Tracking
- Monthly Budget Summary
- Category-wise Analysis
- Report Generation
- Calendar Visualization
- Monthly Archive
- Export Data

---

# 📌 Advantages

- Easy to use
- Lightweight
- Fast Performance
- Secure Data Storage
- Interactive Dashboard
- Visual Reports
- Open Source
- Beginner Friendly

---

# 🚀 Future Improvements

- Cloud Database Integration
- Mobile Application
- Expense Prediction using Machine Learning
- Budget Limit Notifications
- Shared Expense Tracking
- AI-based Spending Suggestions
- PDF Report Generation

---

# 👨‍💻 Team Members

| Name | Role |
|------|------|
| Member 1 | Project Lead & UI Development |
| Member 2 | Database Management |
| Member 3 | Authentication Module |
| Member 4 | Dashboard & Charts |
| Member 5 | Reports & Calendar |
| Member 6 | Testing & Documentation |

---

# 📚 Learning Outcomes

Through this project, we gained practical experience in:

- Python Programming
- Streamlit Development
- SQLite Database Management
- Data Visualization
- Git & GitHub
- Project Documentation
- UI Design
- Software Development Lifecycle

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve the project:

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

# 📜 License

This project is developed for educational purposes as part of the **Python for Engineers Course Project** at **Vishwakarma Institute of Technology, Pune**.

Feel free to use and modify it for learning purposes.

---

# ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub.

It motivates us to build more useful projects.

---

## 📧 Contact

For suggestions or feedback, feel free to reach out.

**Project:** Personal Budget Tracker

**Developed using ❤️ with Python & Streamlit**
