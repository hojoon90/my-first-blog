from django.db import models
from django.utils import timezone


class Post(models.Model):   # models은 Post가 장고 모델임을 의미. 이 코드 때문에 장고는 Post가 데이터베이스에 저장되어야 한다고 알게 된다.
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)   # 다른 모델에 대한 링크를 의미?
    title = models.CharField(max_length=200)    # 글자 수가 제한된 텍스트를 정의할 때 사용. 짧은 문자열 정보를 저장할 때 사용.
    text = models.TextField()   # 글자 수에 제한이 없는 긴 텍스트를 정의할 때 사용.
    created_date = models.DateTimeField(    # 날짜와 시간을 의미.
        default=timezone.now
    )
    published_date = models.DateTimeField(
        blank=True, null=True
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    """
    위에처럼 모델에 대해 정의 혹은 만든 후 
    python manage.py makemigrations 앱이름?(여기서는 blog) 
    명령어를 입력하면 데이터베이스에 반영할 수 있도록 Mig.파일을 만듦. (migrations 폴더안에 0001_initial.py)
    이후 
    python manage.py migrate blog 
    명령을 실행해, 실제 데이터베이스에 모델 추가함
    """