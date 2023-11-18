import streamlit as st
from PIL import Image
import pandas as pd
import json
from ongoing_event_analysis import ongoing_event_sentiment, word_cloud, sentiment_piechart
from sunday_maple import plot_view, plot_reco_reply, plot_decompose, pre_data, word_clound1
from job import filter_data, plot_barchart, group_data
import streamlit.components.v1 as components
from subprocess import check_output
import warnings

ongoing_event = pd.read_csv('data/ongoing_event.csv')
sunday_maple = pd.read_csv('data/sunday_maple_event.csv')
job_data = pd.read_csv('data/jobs.csv')

def overview():
    st.text_area("개요",
                 "- 타겟 대상: 넥슨 / 메이플스토리 \n"
                "- 사용방법\n \t 1. Python version = 3.11.4 \n \t 2. pip install requirements.txt \n \t 3. crawling.ipynb 파일 실행 \n \t 4. topick_modeling.ipynb 실행 \n \t 5. streamlit run main.py \n"
                "- 수집사이트 \n \t 1. https://www.fmkorea.com/ \n \t 2. https://maplestory.nexon.com/Home/Main\n"
                "- 수집내용 \n \t 1. 현재 진행중인 이벤트에 대한 기간, 댓글 수, 조회수, 댓글 내용 \n \t 2. 정기적으로 진행하는 이벤트에 대한 조회수, 추천수, 댓글 수, 댓글 내용, 진행한 날짜 \n \t 3. 메이플스토리에 있는 직업 별로 게시글, 게시글 분류 항목, 조회수, 댓글 수, 추천 수, 게시글 날짜\n"
                "- 활용도/의미 \n \t 1. 이벤트 기획의 향상: 이벤트 참여자들의 감정 및 피드백을 파악하여 이를 기반으로 미래 이벤트의 주제, 형식, 진행방식 등을 개선하고 다양한 참여자의 의견을 수렴할 수 있습니다. \n \t 2. 성과 평가: 정기적인 이벤트의 성과를 정량적으로 측정하고 평가함으로써, 해당 이벤트가 목표를 달성했는지를 확인할 수 있습니다. 이를 통해 이벤트의 효과성을 평가하고 개선점을 도출할 수 있습니다. \n \t"
                "3. 효율적인 마케팅: 인기 직업을 파악하고, 특정 직업에 대한 세부적인 관심도, 트렌드를 파악하여 맞춤형 이벤트나 업데이트, 관련 콘텐츠 강화 등 효과적인 마케팅 전략을 수립할 수 있습니다. \n"
                "- 데이터 분석 과정 \n \t 1. 현재 진행중인 이벤트에 대한 데이터 분석 \n \t \t ☛ 워드클라우드 분석  \n \t \t ☛ 감성 분석 \n \t"
                "2. 정기적으로 진행하는 이벤트(썬데이 메이플)에 대한 데이터 분석 \n \t \t ☛ 시계열 분석 \n \t \t ☛ 워드클라우드 분석 \n \t"
                "3. 메이플스토리 직업별 게시글 데이터 분석 \n \t \t ☛ 막대그래프 분석 \n \t \t ☛ 토픽 모델링")
def plus():
     with st.expander("설명"):
        st.write('1. 댓글 내용에서 추출한 키워드들을 워드클라우드로 시각화하여 어떤 주요 주제들이 도드라지는지 확인 \n'
                 '2. 긍정적인 키워드와 부정적인 키워드의 빈도를 비교하여 이벤트에 대한 참여자들의 감정을 파악 \n'
                 '3. 조회수, 추천수, 댓글 수의 시계열 데이터를 분석하여 이벤트의 성과 추이를 확인.특정 날짜에 조회수와 댓글 수가 증가하는 경향이 파악 \n'
                 '4. 조회수와 추천수의 합이 가장 큰 날과 작은 날에 대한 댓글 내용을 워드클라우드로 시각화하여 어떤 주제들이 큰 관심을 받았는지 또는 어떤 주제가 덜 주목받았는지 확인 \n'
                 '5. 최근 3개월 동안 각 직업의 조회수, 게시글 수, 댓글 수, 추천 수를 합산한 막대그래프를 통해 어떤 직업이 가장 활발하게 활동하고 있는지 확인 \n'
                 '6. 가장 인기 있는 직업 3가지와 가장 인기 없는 직업 3가지에 대해 게시글 제목을 활용하여 토픽 모델링을 진행함으로써 해당 직업들이 어떤 특정 주제에 대해 많은 관심을 가지고 있는지를 확인')
@st.cache_data
def layout1(df):
    result_df = ongoing_event_sentiment(df)
    st.header('현재 진행중인 이벤트')
    tab_labels = list(df['title'].unique())
    tabs = st.tabs(tab_labels)
    for idx, (tab_label, tab) in enumerate(zip(tab_labels, tabs)):
        with tab:
            col1, col2, = st.columns(2)
            with col1:
                st.markdown('워드클라우드')
                fig = word_cloud(df,tab_label)
                st.pyplot(fig)
            with col2:
                st.markdown('이벤트 만족도 분포')
                fig = sentiment_piechart(result_df, tab_label)
                st.pyplot(fig)

@st.cache_data
def layout2(df):
    df = pre_data(df)
    st.header('썬데이 메이플')
    tab1, tab2 = st.tabs(['시계열 분석', '댓글 분석'])
    with tab1:
        col1, col2 = st.columns(2)
        with col1: 
            st.pyplot(plot_view(df))
        with col2:
            st.pyplot(plot_reco_reply(df))
            
        st.divider()
        st.markdown('추세, 계절성, 잔차')
        st.pyplot(plot_decompose(df))
    with tab2:
        max_sum_idx = df['view'].idxmax()
        min_sum_idx = df['view'].idxmin()   
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('가장 관심이 많았을 때')
            st.pyplot(word_clound1(df, max_sum_idx))
        with col2:
            st.markdown('가장 관심이 적었을 때')
            st.pyplot(word_clound1(df, min_sum_idx))
            
def layout3(df):
    st.header('메이플 직업 분석')
    filtered_data, months=filter_data(df)
    result = [str(month) + '월' for month in months]
    for i, month in enumerate(st.tabs(result)):
        with month:
            mon = months[i]
            grouped_data, sum_data, top_jobs_index, bottom_jobs_index = group_data(filtered_data, mon)
            top_job_list = grouped_data['job'][top_jobs_index].values
            bottom_job_list = grouped_data['job'][bottom_jobs_index].values
            st.pyplot(plot_barchart(grouped_data, sum_data, top_jobs_index, bottom_jobs_index, mon))
            st.divider()
            st.markdown('인기 직업의 토픽 모델링')
            for j in range(len(top_job_list)):
                job = top_job_list[j]
                button_key = f'{mon}_top_{job}_button'
                if st.button(f'{job} 토픽 모델링 결과',key=button_key):
                    file_name = f'result/lda_result_{mon}월_{job}.html'
                    check_output("start " + file_name, shell=True)
            st.divider()
            st.markdown('비인기 직업의 토픽 모델링')
            for j in range(len(bottom_job_list)):
                job = bottom_job_list[j]
                button_key = f'{mon}_top_{job}_button'
                if st.button(f'{job} 토픽 모델링 결과', key=button_key):
                    file_name = f'result/lda_result_{mon}월_{job}.html'
                    check_output("start " + file_name, shell=True)
def main():
    background = Image.open('image/background.jpg')
    st.image(background, use_column_width='always')
    st.title("메이플스토리 데이터 분석") 
    css = '''
    <style>
        .element-container:has(>.stTextArea), .stTextArea {
            width: 800px !important;
        }
        .stTextArea textarea {
            height: 630px;
        }
    </style>
    '''
    st.write(css, unsafe_allow_html=True)
    overview()
    plus()
    layout1(ongoing_event)
    layout2(sunday_maple)
    layout3(job_data)
    
if __name__=="__main__":
    main()