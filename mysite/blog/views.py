from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post    #from 다음에 있는 마침표(.)는 현재 디렉토리 또는 애플리케이션을 의미합니다. 동일한 디렉터리 내 views.py, models.py파일이 있기 때문에 . 파일명 (.py확장자를 붙이지 않아도)으로 내용을 가져올 수 있습니다.
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):  # 새 Post 폼을 추가하기 위해 PostForm() 함수를 호출하도록 하여 템플릿에 넘깁니다.
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)  # commit=False란 넘겨진 데이터를 바로 Post 모델에 저장하지는 말라는 뜻 (작성자 추가 후 저장)
            post.author = request.user  # 작성자 추가
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form':form})