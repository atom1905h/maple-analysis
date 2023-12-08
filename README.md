# maplestory-analysis

## 분석 페이지
![1](https://github.com/atom1905h/maple-analysis/assets/90888774/f276cb84-7bc4-490c-a94e-9a728754b810)
![2](https://github.com/atom1905h/maple-analysis/assets/90888774/1bcda82e-82d9-4a61-8b85-e541c1228dec)
![3](https://github.com/atom1905h/maple-analysis/assets/90888774/863c2b35-0f96-4c78-a5b8-5120e1bd33f1)
![4](https://github.com/atom1905h/maple-analysis/assets/90888774/0e9c26c7-c1ec-4b66-b8be-2556982a4007)
![5](https://github.com/atom1905h/maple-analysis/assets/90888774/9816e9d5-e820-4f72-b9d9-79e0a1e28938)
![6](https://github.com/atom1905h/maple-analysis/assets/90888774/34b31fba-62b5-4564-9f98-8cdeb21cd4a3)

## 배경
- 게임 산업에서 이벤트 기획 및 운영은 사용자 참여 유도와 게임의 인기 유지에 중요한 역할을 합니다. 그러나 현재 이벤트 기획은 사용자의 반응을 직접적으로 반영하기 어렵고, 효과적인 이벤트 기획이 어려운 경우가 많을 것이라고 생각합니다. 따라서 데이터 분석을 통해 인사이트를 얻고 더 효과적인 이벤트를 기획하는데 도움을 주기 위해 시작하였습니다.

## 사용방법
1. Python version = 3.11.4(conda create -n name python=3.11.4)
2. pip install -r requirements.txt
3. crawling.ipynb 실행
4. topick_modeling.ipynb 실행
5. streamlit run main.py

## 수집사이트
1. [FMKorea](https://www.fmkorea.com/)
2. [메이플스토리 공식 홈페이지](https://maplestory.nexon.com/Home/Main)

## 수집내용
1. 현재 진행중인 이벤트에 대한 기간, 댓글 수, 조회수, 댓글 내용
2. 정기적으로 진행하는 이벤트에 대한 조회수, 추천수, 댓글 수, 댓글 내용, 진행한 날짜
3. 메이플스토리에 있는 직업 별로 게시글, 게시글 분류 항목, 조회수, 댓글 수, 추천 수, 게시글 날짜

## 활용도/의미
1. 이벤트 기획의 향상: 이벤트 참여자들의 감정 및 피드백을 파악하여 이를 기반으로 미래 이벤트의 주제, 형식, 진행방식 등을 개선하고 다양한 참여자의 의견을 수렴할 수 있습니다.
2. 성과 평가: 정기적인 이벤트의 성과를 정량적으로 측정하고 평가함으로써, 해당 이벤트가 목표를 달성했는지를 확인할 수 있습니다. 이를 통해 이벤트의 효과성을 평가하고 개선점을 도출할 수 있습니다.
3. 효율적인 마케팅: 메이플 내의 직업의 선호도를 파악하고, 특정 직업이 가지는 세부적인 관심주제, 트렌드 등을 파악하여 맞춤형 이벤트나 업데이트, 관련 콘텐츠 강화 등 효과적인 마케팅 전략을 수립할 수 있습니다.

## 데이터 분석 과정
1. 현재 진행중인 이벤트에 대한 데이터 분석
   - 워드클라우드 분석
   - 감성 분석
2. 정기적으로 진행하는 이벤트(썬데이 메이플)에 대한 데이터 분석
   - 시계열 분석
   - 워드클라우드 분석
3. 메이플스토리 직업별 게시글 데이터 분석
   - 막대그래프 분석
   - 토픽 모델링
