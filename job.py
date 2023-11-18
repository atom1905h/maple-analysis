from datetime import datetime, timedelta
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sns.set(font="Malgun Gothic",style='whitegrid')

def filter_data(df):
    current_datetime = datetime.now()
    current_date = current_datetime.strftime("%Y.%m.%d")
    df['date'] = pd.to_datetime(df['date'], format='%Y.%m.%d')
    current_date = datetime.now()
    start_date = (current_date - timedelta(days=90)).replace(day=1)  # 3개월 전
    end_date = current_date.replace(day=1) - timedelta(days=1)  # 이전 달의 마지막 날
    filtered_data = df[(df['date'] >= start_date) & (df['date'] <= end_date)]
    filtered_data.reset_index(drop= True, inplace=True)
    months = list(filtered_data['date'].dt.month.unique())
    months = sorted(months)
    return filtered_data, months

def group_data(filtered_data, month):
    filtered_month_data = filtered_data[filtered_data['date'].dt.month==month]
    grouped_data = filtered_month_data.groupby('job').agg({
        'title': 'count',
        'reply': 'sum',
        'view': 'sum',
        'recommend': 'sum'
    }).reset_index()
    sum_data = grouped_data[['title','reply','view','recommend']].sum(axis=1)
    top_jobs_index = sum_data.nlargest(3).index
    bottom_jobs_index = sum_data.nsmallest(3).index
    return grouped_data, sum_data, top_jobs_index, bottom_jobs_index

def plot_barchart(grouped_data, sum_data, top_jobs_index, bottom_jobs_index, month):
    fig, ax = plt.subplots(figsize=(50, 40))
    sns.barplot(x='job', y='view', data=grouped_data, color='green', label='조회수')
    sns.barplot(x='job', y='reply', data=grouped_data, color='purple', label='댓글 수', bottom = grouped_data['view'])
    sns.barplot(x='job', y='recommend', data=grouped_data, color='blue', label='추천 수', bottom = grouped_data['view']+grouped_data['reply'])
    sns.barplot(x='job', y='title', data=grouped_data, color='orange', label='게시글 수', bottom = grouped_data['reply']+grouped_data['recommend']+grouped_data['view'])
    for top, bottom in zip(top_jobs_index, bottom_jobs_index):
        t_job = grouped_data['job'].loc[top]
        annotate_text = f'{t_job}'
        ax.annotate(annotate_text, xy=(top, sum_data.loc[top]+10), ha='center', va='center', fontsize=30, color='red')
        b_job = grouped_data['job'].loc[bottom]
        annotate_text = f'{b_job}'
        ax.annotate(annotate_text, xy=(bottom, sum_data.loc[bottom]+10), ha='center', va='center', fontsize=30, color='blue')
    ax.set_xlabel('직업', fontsize=30)
    ax.set_ylabel('', fontsize=30)
    plt.title(f'{month}월', fontsize=50)
    ax.legend(fontsize=30)

    return fig
