from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import SubmitData
from .serializers import SubmitDataSerializer
from .utils import create_dataframe_from_serializer
from .recommend import recommend, get_place_id, get_place_photo_url, get_place_details, search_nearby_restaurants
@api_view(['POST'])
def api_endpoint(request):
    if request.method == 'POST':
        serializer = SubmitDataSerializer(data=request.data)
        if serializer.is_valid():
            # 유효성 검사 통과한 경우, 데이터 저장 및 추가 작업 수행

            #데이터프레임 구성
            user_info=create_dataframe_from_serializer(serializer)
            print(user_info)
            place_name = recommend(user_info)
            place_id = get_place_id(place_name)
            place_photo = get_place_photo_url(place_id)
            place_lat, place_lng, place_url =get_place_details(place_id)

            #추천 정보
            recommend_place_information=[place_name,place_photo,place_url]

            restaurant = []
            results =search_nearby_restaurants(place_lat, place_lng, 500)
            if results is not None:
                # 'results' 필드가 존재하면 해당 리스트 가져오기, 그렇지 않으면 빈 리스트 반환
                places = results.get('results', [])

                # 상위 3개의 장소만 선택
                top_3_results = places[:3]

                for place in top_3_results:
                    place_lat_lng_url_tuple = get_place_details(place['place_id'])
                    temp=[place['name'],place_lat_lng_url_tuple[2]]
                    restaurant.append(temp)
            else:
                print("Error getting place details")
            print(recommend_place_information,restaurant)









            # 여기서 필요한 로직 수행 후 결과값 반환
            # return Response({'status': 'success'}, status=200)
            return Response(
                {'status': 'success', 'recommend_place_information': recommend_place_information,
                 'restaurant': restaurant},
                status=200)


        else:
            # 유효성 검사 실패한 경우, 에러 응답 반환
            return Response(serializer.errors, status=400)
    else:
        return JsonResponse({'error': 'Invalid Method'}, status=405)


@api_view(['GET'])
def another_api_endpoint(request,my_data_id):
    # 여기서 필요한 로직을 수행하고 결과값을 반환합니다.
    try:
        my_data = SubmitData.objects.get(id=my_data_id)
        serializer = SubmitDataSerializer(my_data)

        return Response(serializer.data)
    except SubmitData.DoesNotExist:
        return Response({'error': 'Data not found'}, status=404)


@api_view(['GET'])
def mydata_list(request):
    queryset = SubmitData.objects.all()
    serializer = SubmitDataSerializer(queryset, many=True)
    return Response(serializer.data)