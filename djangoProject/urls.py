from django.contrib import admin
from django.urls import path, include  # include 함수를 import

from myapp.views import api_endpoint, another_api_endpoint, mydata_list
urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
    path('api/<int:my_data_id>/', another_api_endpoint),
    path('mydata/', mydata_list)
]