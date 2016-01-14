from django.shortcuts import render
from django.utils import timezone

from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all().order_by('published_date')
    return render(request, 'six_site/post_list.html', {'posts':posts})