import requests
from bs4 import BeautifulSoup



# API 요청 URL 및 인증키
url = "http://apis.data.go.kr/B551011/KorService1/locationBasedList1"
params = {
    'serviceKey':'rmmgDUVQo9EoerLv7PxQp1CP0aiSxgG8Y3MsrzCQUU7F1exTKhM3rUEckr1cXp8G3yCdkcfWNDc0mHCKrgTjbg==',
    # 실제 서비스 키로 교체해야 합니다.
    'numOfRows': 10,
    'pageNo': 1,
    # 'contentTypeId': 12,
    'MobileOS': 'ETC',
    'MobileApp': 'AppTest',
    'mapX': 126.981611,
    'mapY': 37.568477,
    'radius': 1500,
    'listYN': 'Y'
}

# API 요청
response = requests.get(url, params=params)
print(response.url)
# 응답 상태 확인
if response.status_code == 200:
    # XML 파싱
    soup = BeautifulSoup(response.text, "lxml-xml")  # response.content도 가능

    # 결과 출력
    for item in soup.find_all('item'):


         address=item.addr1.text+" "+item.addr2.text+" "+item.title.text
         print(address)


else:
    print("Error code:", response.status_code)