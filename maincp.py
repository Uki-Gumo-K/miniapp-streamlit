#moduleのインポート
# from cgitb import text
# from signal import setitimer
# from turtle import left
import streamlit as st
import time
import math

#Title, 本文
st.title('Simply Timer')

st.write('タイマーをセット')
if st.checkbox('set'):
    settimer_m1 = st.slider(
        '何分？',
        0,120,0
    )

    settimer_s1 = st.slider(
        '何秒？',
        0,60,0
    )

    '***',settimer_m1,'分',settimer_s1,'秒','でセット***'
    if st.checkbox('Start!'):

        latest_iteration1 = st.empty()
        bar1 = st.progress(0)

        settimer1 = (settimer_m1 * 60) + settimer_s1
        percent_time1 = 100 / settimer1
        pt1 = math.ceil(percent_time1)
    # progress_time = 

        for i in range(settimer1):
            latest_iteration1.text(f'経過時間:{i+1}')
            bar1.progress((i+1)/settimer1)
            time.sleep(1)

        'おつかれ！'

# st.write('タイマー2をセット')
# if st.checkbox('set 2'):
#     settimer_m2 = st.slider(
#         '何分？',
#         0,120,10
#     )

#     settimer_s2 = st.slider(
#         '何秒？',
#         0,60,0
#     )

#     '***',settimer_m2,'分',settimer_s2,'秒','でセット***'
#     if st.checkbox('Start!'):

#         latest_iteration2 = st.empty()
#         bar2 = st.progress(0)

#         settimer2 = (settimer_m2 * 60) + settimer_s2
#         percent_time2 = 100 / settimer2
#         pt2 = round(percent_time2,)
#     # progress_time = 

#         for i in range(settimer2):
#             latest_iteration2.text(f'経過時間:{i+1}')
#             bar2.progress(pt2*i+pt2)
#             time.sleep(1)

#         'Done!'

# left_column, right_column =st.columns(2)
# button = left_column.button('右カラムに文字を表示')
# if button:
#     right_column.write('ここは右カラム')

# expander = st.expander('問い合わせ')
# expander.write('問い合わせ内容を書く。')
# #テキスト入力
# text = st.text_input('あなたの趣味を教えて下さい。')
# #スライダー
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味:',text
# 'コンディション：',condition
# # if st.checkbox('Show Image'): #T or F
# #     img = Image.open('sample.JPG')
# #     st.image(img, caption='anohana',use_column_width=True)


