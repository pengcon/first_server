from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MyData
from .serializers import MyDataSerializer


@api_view(['POST'])
def api_endpoint(request):
    if request.method == 'POST':
        return JsonResponse({'status': 'success'}, status=200)

    else:
        return JsonResponse({'error': 'Invalid Method'}, status=400)
    # request.data에 POST 데이터가 들어있습니다.
    # 여기서 필요한 로직을 수행하고 결과값을 반환합니다.
    # serializer = MyDataSerializer(data=request.data)
    #
    # if serializer.is_valid():
    #     my_data = serializer.save()
    #     return Response({'my_data_id': my_data.id})
    # else:
    #     return Response(serializer.errors, status=400)


@api_view(['GET'])
def another_api_endpoint(request,my_data_id):
    # 여기서 필요한 로직을 수행하고 결과값을 반환합니다.
    try:
        my_data = MyData.objects.get(id=my_data_id)
        serializer = MyDataSerializer(my_data)
        return Response(serializer.data)
    except MyData.DoesNotExist:
        return Response({'error': 'Data not found'}, status=404)


@api_view(['GET'])
def mydata_list(request):
    queryset = MyData.objects.all()
    serializer = MyDataSerializer(queryset, many=True)
    return Response(serializer.data)