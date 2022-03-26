from django.shortcuts import render
from blob.models import Post # <==

# мой проект/blob/views.py
def post_list(request):
    posts = Post.objects.all()# <==
    return render(request,
                  'blob/post_list.html',
                  {'posteki':posts})# <==
def post_detail(reguest, pk):
    post = Post.objects.get(id=pk)
    page = render(reguest,
                  'blob/post_one.html',
    {'post':post})
    return page