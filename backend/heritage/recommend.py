import pandas as pd
import numpy as np
from pandas import Series, DataFrame
import sqlite3

def recommend_system(user_pk):
    conn = sqlite3.connect('db.sqlite3')

    # 유저 - 태그 데이터프레임 생성
    cur = conn.cursor()

    cur2 = conn.cursor()

    cur.execute('SELECT * FROM heritage_user_tag')
    cur2.execute('SELECT * FROM heritage_tag')

    rows = cur.fetchall()
    rows2 = cur2.fetchall()

    cols = [column[0] for column in cur.description]
    cols2 = [column[0] for column in cur2.description]

    data_df = pd.DataFrame.from_records(data=rows, columns=cols)
    data_df2 = pd.DataFrame.from_records(data=rows2, columns=cols2)

    # 태그 - 문화재 데이터프레임 생성
    cur = conn.cursor()

    cur.execute('SELECT * FROM heritage_heritage_heritage_tags')

    rows = cur.fetchall()

    cols = [column[0] for column in cur.description]

    data_df3 = pd.DataFrame.from_records(data=rows, columns=cols)

    # 각 문화재에 존재하는 태그에 값을 1로 추가
    data_df3['values'] = 1


    # 문화재 방문 리스트 테이블
    cur = conn.cursor()

    cur.execute('SELECT * FROM heritage_heritage_visit_users')

    rows = cur.fetchall()

    cols = [column[0] for column in cur.description]

    data_df4 = pd.DataFrame.from_records(data=rows, columns=cols)

    conn.close()


    data_df2.rename(columns= {'id':'tag_id'}, inplace=True)
    # 모든 태그에 대한 테이블 생성
    data_df = pd.merge(data_df, data_df2, on='tag_id', how="outer").fillna(0)

    # 유저번호 Float Int로 변경
    data_df['user_id'] = data_df['user_id'].astype(int)

    # 테이블 병합 ( 유저 - 태그 가중치 PIVOT테이블 생성 ), 빈 값은 0으로 변환
    df_user_tag_weights = data_df.pivot(
        values = 'weight',
        index = 'user_id',
        columns = 'tag_id',
    ).fillna(0)


    # (태그 - 문화재 테이블 생성), 빈 값은 0 태그가 존재하면 1
    df_heritage_tag_value = data_df3.pivot(
        index = 'heritage_id',
        columns = 'tag_id',
        values = 'values'
    ).fillna(0)


    # 두 테이블 병합

    s1 = Series(df_user_tag_weights.loc[user_pk])

    result = df_heritage_tag_value.mul(s1, axis=1)

    result = result.sum(axis=1)

    result = result.sort_values(ascending=False)

    recommend_list = list(result.index)

    visited_heritage = list(data_df4['heritage_id'].values)

    user_recommend = []

    while len(user_recommend) < 10:
        for heritage in recommend_list:
            if len(user_recommend) > 10:
                break
            if heritage not in visited_heritage:
                user_recommend.append(heritage)

    return user_recommend