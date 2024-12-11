from django.shortcuts import render
from django.core.paginator import Paginator
from task2.models import News

# Create your views here.
def news(request):
    posts = News.objects.all().order_by('-date')
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {'page_obj':page_obj})