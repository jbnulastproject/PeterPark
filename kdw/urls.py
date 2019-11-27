
from django.contrib import admin
from django.urls import path, include
import account.urls 
#오류 발생 원인

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    #최대한 api 연결 바로 되게 하기
]
