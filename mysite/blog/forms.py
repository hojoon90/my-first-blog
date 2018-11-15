from django import forms

from .models import Post

class PostForm(forms.ModelForm):    # forms.ModelForm은 ModelForm이라는 것을 알려주는 구문.

    class Meta:
        model=Post  # 이 폼을 만들기 위해서 어떤 model이 쓰여야 하는지 장고에 알려주는 구문
        fields = ('title', 'text',)