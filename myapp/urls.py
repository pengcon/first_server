from django.urls import path

from .views import api_endpoint, another_api_endpoint, mydata_list


urlpatterns = [
    path('api-endpoint/', api_endpoint),
    path('api/<int:my_data_id>/', another_api_endpoint),
    path('mydata/', mydata_list)
]