import json
import pandas as pd
from wordcloud import WordCloud
import PIL
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(font="Malgun Gothic",style='whitegrid')

def ongoing_event_sentiment(df):
    with open('SentiWord/SentiWord_info.json', encoding='utf-8-sig', mode='r') as f: 
        SentiWord_info = json.load(f)
        sentiword_dic = pd.DataFrame(SentiWord_info)

    df['Review'] = df['reply'].str.replace('[^가-힣]', ' ', regex = True)
    title = list(df['title'].unique())
    result_df = pd.DataFrame(columns=("title","review", "sentiment"))  
    for i in range(len(title)):
        tokens=list(df['Review'][df['title']==title[i]])
        data = pd.DataFrame(columns=("title","review", "sentiment"))  
        idx = 0  
        for token in tokens:                              
            sentiment = 0                                   
            for j in range(0, len(sentiword_dic)):           
                if sentiword_dic.word[j] in token:              
                    sentiment += int(sentiword_dic.polarity[j])  
            data.loc[idx] = [title[i],token, sentiment]                 
            idx += 1
        result_df = pd.concat([result_df, data], ignore_index=True)
    result_df['sentiment_cate'] = result_df['sentiment'].apply(lambda x: '중립' if x == 0 else ('긍정' if x >= 0 else '부정'))

    return result_df

def word_cloud(df, title):
    icon = PIL.Image.open('image/wordcloud.png')
    img = np.array(icon)
    grouped_comments = df.groupby('title')['reply'].apply(lambda x: ' '.join(x)).reset_index()
    comments_text= grouped_comments[grouped_comments['title']==title]['reply'].values[0]
    wordcloud = WordCloud(font_path='C:/Windows/Fonts/NanumGothic.ttf', width=200, height=200, background_color='white', mask=img).generate(comments_text)
    
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    return fig

def sentiment_piechart(result_df, title):
    result_df = result_df.set_index('title')
    count_df = result_df.groupby(['title', 'sentiment_cate'],sort=False).size().unstack(fill_value=0)
    title_data = count_df.loc[title]
    fig, ax = plt.subplots()
    ax.pie(title_data, labels= title_data.index,autopct='%1.1f%%', startangle=90, colors=['lightskyblue', 'lightgreen', 'lightcoral'])

    return fig