import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from catboost import CatBoostRegressor
import requests
import json


def search_nearby_restaurants(latitude, longitude, radius):
    api_key = 'AIzaSyAV_sjZngj87Gf9WsEnEI6TTgCDS8poR5w'
    base_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'

    params = {
        'location': f'{latitude},{longitude}',
        'radius': radius,
        'type': 'restaurant',
        'key': api_key,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        return response.json()

    else:
        return None

def get_place_details(place_id):
    api_key = "AIzaSyAV_sjZngj87Gf9WsEnEI6TTgCDS8poR5w"  # 여기에 실제 API 키 입력
    base_url = 'https://maps.googleapis.com/maps/api/place/details/json'

    params = {
        'place_id': place_id,
        'fields': 'geometry/location,url',
        'key': api_key,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        print(response.json())
        result = response.json().get('result', {})
        location = result.get('geometry', {}).get('location', {})

        return location.get('lat'), location.get('lng'), result.get('url')  # 위도와 경도 반환
    else:
        return None, None, None  # 오류 발생 시 None 반환
def get_place_id(place_name):
    api_key = "AIzaSyAV_sjZngj87Gf9WsEnEI6TTgCDS8poR5w"
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
    params = {
        'input': place_name,
        'inputtype': 'textquery',
        'fields': 'place_id',
        'key': api_key
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = json.loads(response.text)

        if data['status'] == "OK":
            return data['candidates'][0]['place_id']

        else:
            print("Error with the request: ", data['status'])
            return None

    else:
        print("HTTP request failed: ", response.status_code)
        return None



def get_place_photo_url(place_id):
    url = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {
        'place_id': place_id,
        'fields': 'photo',
        'key': 'AIzaSyAV_sjZngj87Gf9WsEnEI6TTgCDS8poR5w'
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        if 'result' in data and 'photos' in data['result']:
            photo_reference = data['result']['photos'][0]['photo_reference']
            photo_url = f"https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={photo_reference}&key={'AIzaSyAV_sjZngj87Gf9WsEnEI6TTgCDS8poR5w'}"
            return photo_url

    print("Failed to fetch the photo URL.")
    return None

# 모델 로드
def recommend(user_info):
    model_path = 'C:/Users/gnsdl/PycharmProjects/djangoProject/myapp/model.h5'
    data_path = 'C:/Users/gnsdl/PycharmProjects/djangoProject/myapp/training_data.csv'
    best_model = CatBoostRegressor()
    best_model.load_model(model_path)

    # user_info = pd.DataFrame({
    #                                   'GENDER': ['남'],
    #                                   'AGE_GRP': ['30'],
    #                                   'INCOME': ['5'],
    #                                   'TRAVEL_STYL_1': ['4.0'],
    #                                   'TRAVEL_STYL_2': ['4.0'],
    #                                   'TRAVEL_STYL_3': ['4.0'],
    #                                   'TRAVEL_STYL_4': ['4.0'],
    #                                   'TRAVEL_STYL_5': ['4.0'],
    #                                   'TRAVEL_STYL_6': ['4.0'],
    #                                   'TRAVEL_STYL_7': ['4.0'],
    #                                   'TRAVEL_STYL_8': ['4.0'],
    #                                   'TRAVEL_MOTIVE_1': ['4'],
    #                                   'TRAVEL_COMPANIONS_NUM': ['1'],
    #                                   'city': ['서울']})

    training_data=pd.read_csv(data_path)
    filtered_data =training_data[['city','district','VISIT_AREA_NM','VISIT_AREA_TYPE_CD','RTM_AVG','RCMDTN_AVG','RVSYN_AVG','RVSINT_AVG','COMPANIONS_AVG','DGSTFN']]
    # 추천받을 기준이 되는 유저정보를 여행지만큼 복사한 후, 여행지 정보 값을 넣어줌
    combined_data = pd.merge(filtered_data, user_info, on='city')


    #필요한 값만 추출
    combined_data = combined_data[['GENDER','AGE_GRP','INCOME','TRAVEL_STYL_1','TRAVEL_STYL_2','TRAVEL_STYL_3',
                               'TRAVEL_STYL_4','TRAVEL_STYL_5','TRAVEL_STYL_6','TRAVEL_STYL_7','TRAVEL_STYL_8','TRAVEL_MOTIVE_1','TRAVEL_COMPANIONS_NUM'
                               ,'VISIT_AREA_NM','city','district','VISIT_AREA_TYPE_CD','RTM_AVG','RCMDTN_AVG','RVSYN_AVG','RVSINT_AVG','COMPANIONS_AVG','DGSTFN']]
    #예상만족도를 저장
    combined_data['predicted_satisfaction'] =best_model.predict(combined_data)
    #예상만족도 4.5 이상만 선별
    recommended_travel = combined_data[combined_data['predicted_satisfaction'] >= 4.5]
    #예상만족도 높은순으로 정렬 (head(n)은 n개만 정렬한다는 뜻)
    recommended_travel_final = recommended_travel.drop_duplicates(subset='VISIT_AREA_NM')
    # recommended_travel_final = recommended_travel_final.drop([78,1443,872,275,2523,1728,1295,268,203,1697,1990,833,1599,965,2737,984,62,1882,1130,2376,3146,2976,339,1196,755,3106,1399,2641,341,2483,2079,2124,1755,472,2729,496,2578,163,939,647,698,2358,2013,1231,2825,314,3158,1421,599,534,399,2133,1523,202,2937,282,396,198,2466,389,445,1401,73,2261,1646,2520,2112,2234,3150])
    recommended_travel_final = recommended_travel_final.sort_values(by='predicted_satisfaction', ascending=False).head(100)
    #중복 제거하고 만족도순으로 여행지 출력


    # print(recommended_travel_final['VISIT_AREA_NM'][0:50])
    place_name = recommended_travel_final.iloc[1, recommended_travel_final.columns.get_loc('VISIT_AREA_NM')]
    return place_name

# user_info = pd.DataFrame({
#                                       'GENDER': ['남'],
#                                       'AGE_GRP': ['30'],
#                                       'INCOME': ['5'],
#                                       'TRAVEL_STYL_1': ['4.0'],
#                                       'TRAVEL_STYL_2': ['4.0'],
#                                       'TRAVEL_STYL_3': ['4.0'],
#                                       'TRAVEL_STYL_4': ['4.0'],
#                                       'TRAVEL_STYL_5': ['4.0'],
#                                       'TRAVEL_STYL_6': ['4.0'],
#                                       'TRAVEL_STYL_7': ['4.0'],
#                                       'TRAVEL_STYL_8': ['4.0'],
#                                       'TRAVEL_MOTIVE_1': ['4'],
#                                       'TRAVEL_COMPANIONS_NUM': ['1'],
#                                       'city': ['서울']})
# user_name=recommend(user_info)
# print(user_name)

