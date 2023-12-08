import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose
import numpy as np
import PIL
from wordcloud import WordCloud

sns.set(font="Malgun Gothic",style='whitegrid')
def pre_data(df):
    df['datetime'] = pd.to_datetime(df['datetime']).dt.date
    df_set = df.set_index('datetime').sort_index()
    return df_set

def plot_view(df_set):
    # df_set = df.set_index('datetime').sort_index()
    max_view_idx = df_set['view'].idxmax()
    min_view_idx = df_set['view'].idxmin()

    fig, ax = plt.subplots()
    sns.lineplot(data=df_set, x=df_set.index, y='view', label='조회수')

    ax.annotate(f'최대 조회수: {df_set["view"].max()} ({max_view_idx})', xy=(max_view_idx, df_set['view'].max()), xytext=(max_view_idx, df_set['view'].max() + 100),
                arrowprops=dict(facecolor='red', arrowstyle='->'), fontsize=8,color='red')

    ax.annotate(f'최소 조회수: {df_set["view"].min()} ({min_view_idx})', xy=(min_view_idx, df_set['view'].min()), xytext=(min_view_idx, df_set['view'].min() - 100),
                arrowprops=dict(facecolor='blue', arrowstyle='->'), fontsize=8, color='blue')

    ax.set_xticks(df_set.index[::80])
    ax.set_xticklabels(df_set.index[::80], rotation=45)  
    ax.set_xlabel('날짜')  
    ax.set_ylabel('조회수') 
    ax.legend()

    return fig

def plot_reco_reply(df_set):
    # df_set = df.set_index('datetime').sort_index()
    max_recommend_idx = df_set['recommendation number'].idxmax()
    min_recommend_idx = df_set['recommendation number'].idxmin()
    max_reply_idx = df_set['reply number'].idxmax()
    min_reply_idx = df_set['reply number'].idxmin()
    fig, ax = plt.subplots()
    sns.lineplot(data=df_set, x=df_set.index, y='recommendation number', label='추천수')
    sns.lineplot(data=df_set, x=df_set.index, y='reply number', label='댓글수')
    plt.annotate(f'최대 추천수: {df_set["recommendation number"].max()} ({max_recommend_idx})', xy=(max_recommend_idx, df_set['recommendation number'].max()), xytext=(max_recommend_idx, df_set['recommendation number'].max()),
                 arrowprops=dict(facecolor='red', arrowstyle='->'),fontsize=5,color='red')
    plt.annotate(f'최소 추천수: {df_set["recommendation number"].min()} ({min_recommend_idx})', xy=(min_recommend_idx, df_set['recommendation number'].min()), xytext=(min_recommend_idx, df_set['recommendation number'].min()),
                 arrowprops=dict(facecolor='blue', arrowstyle='->'),fontsize=5,color='blue')
    plt.annotate(f'최대 댓글수: {df_set["reply number"].max()} ({max_reply_idx})', xy=(max_reply_idx, df_set['reply number'].max()), xytext=(max_reply_idx, df_set['reply number'].max()),
                 arrowprops=dict(facecolor='red', arrowstyle='->'),fontsize=5, color='red')
    plt.annotate(f'최소 댓글수: {df_set["reply number"].min()} ({min_reply_idx})', xy=(min_reply_idx, df_set['reply number'].min()), xytext=(min_reply_idx, df_set['reply number'].min()),
                 arrowprops=dict(facecolor='blue', arrowstyle='->'),fontsize=5, color='blue')
    ax.set_xticks(df_set.index[::80])
    ax.set_xticklabels(df_set.index[::80], rotation=45)  
    ax.set_xlabel('날짜')  
    ax.set_ylabel('수') 
    ax.legend()

    return fig

def plot_decompose(df_set):
    df_set['sum']=df_set[['view','recommendation number', 'reply number']].sum(axis=1)
    ts_data = df_set['sum']
    result = seasonal_decompose(ts_data, model='addictive',period=4)
    fig, ax = plt.subplots(figsize=(16,12))

    # 원본 데이터
    ax_original = fig.add_subplot(4,1,1)
    ax_original.plot(ts_data, label='Original')
    ax_original.legend(loc='upper left')

    # 추세 (Trend) 데이터
    ax_trend = fig.add_subplot(4, 1, 2)
    ax_trend.plot(result.trend, label='Trend')
    ax_trend.legend(loc='upper left')

    # 계절성 (Seasonal) 데이터
    ax_seasonal = fig.add_subplot(4, 1, 3)
    ax_seasonal.plot(result.seasonal, label='Seasonal')
    ax_seasonal.legend(loc='upper left')

    # 잔차 (Residual) 데이터
    ax_residual = fig.add_subplot(4, 1, 4)
    ax_residual.plot(result.resid, label='Residual')
    ax_residual.legend(loc='upper left')

    plt.tight_layout()
    
    return fig

def word_clound1(df_set, idx):
    # max_sum_idx = df_set['view'].idxmax()
    # min_sum_idx = df_set['view'].idxmin()
    icon = PIL.Image.open('image/wordcloud.png')
    img = np.array(icon)
    comment = df_set.loc[idx].groupby('datetime')['reply'].apply(lambda x: ' '.join(x)).reset_index()
    comment = comment['reply'].values[0]
    wordcloud = WordCloud(font_path='C:/Windows/Fonts/NanumGothic.ttf', width=200, height=200, background_color='white', mask=img).generate(comment)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')

    return fig
