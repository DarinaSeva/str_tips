import pandas as pd
import numpy as np
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
import random

st.title('Динамика чаевых во времени 💸')

tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

start_date = pd.to_datetime('2023-01-01')
end_date = pd.to_datetime('2023-01-31')
random_dates = [(start_date + (end_date - start_date) * random.random()).date() for _ in range(len(tips))]
tips['time_order'] = random_dates

date_range = st.sidebar.date_input("Выберите диапазон дат", [start_date.date(), end_date.date()], min_value=start_date.date(), max_value=end_date.date())
gender = st.sidebar.selectbox("Пол", options=["Все", "Женщины", "Мужчины"], index=0)
smoker = st.sidebar.selectbox("Курящие", ["Все", "Да", "Нет"], index=0)
day = st.sidebar.selectbox("День недели", ["Все", "Четверг", "Пятница", "Суббота", "Воскресенье"], index=0)
time_of_day = st.sidebar.selectbox("Время суток", ["Все", "Обед", "Ужин"], index=0)
group_size = st.sidebar.slider("Размер группы", min_value=1, max_value=int(tips['size'].max()), value=[1, int(tips['size'].max())])

# Применение фильтров
filtered_tips = tips[(tips['time_order'] >= date_range[0]) & (tips['time_order'] <= date_range[1])]
if gender != "Все":
    filtered_tips = filtered_tips[filtered_tips['sex'] == gender]
if smoker != "Все":
    filtered_tips = filtered_tips[filtered_tips['smoker'] == smoker]
if day != "Все":
    filtered_tips = filtered_tips[filtered_tips['day'] == day]
if time_of_day != "Все":
    filtered_tips = filtered_tips[filtered_tips['time'] == time_of_day]
filtered_tips = filtered_tips[(filtered_tips['size'] >= group_size[0]) & (filtered_tips['size'] <= group_size[1])]

fig, ax = plt.subplots()
sns.lineplot(data=filtered_tips, x='time_order', y='tip', marker='o', color = 'purple')
ax.set_xlabel('Дата заказа')
ax.set_ylabel('Чаевые')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

st.pyplot(fig)


