from django.shortcuts import render
from .models import Post    #from 다음에 있는 마침표(.)는 현재 디렉토리 또는 애플리케이션을 의미합니다. 동일한 디렉터리 내 views.py, models.py파일이 있기 때문에 . 파일명 (.py확장자를 붙이지 않아도)으로 내용을 가져올 수 있습니다.

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})