from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.post_list, name='post_list'),
]
'''
이 패턴은 장고에게 누군가 웹사이트에 'http://127.0.0.1:8000/' 주소로 들어왔을 때 views.post_list를 보여주라고 말할 거에요. 
name='post_list'는 URL에 이름을 붙인 것으로 뷰를 식별합니다.
'''