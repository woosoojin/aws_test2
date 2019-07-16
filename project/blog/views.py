from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .form import BlogPost

# Create your views here.
def home(request):
    blogs = Blog.objects #쿼리셋/ 객체들의 목록
    blog_list = Blog.objects.all() #모든 블로그 글들을 대상으로
    paginator = Paginator(blog_list, 3) #블로그 객체 세개를 한 페이지로 자르기
    page = request.GET.get('page') #key값이 page인 value값을 반환한다./
    posts = paginator.get_page(page) # request된 페이지에 해당하는 page가 반환된다. 

    return render(request, 'home.html', {'blogs': blogs, 'posts':posts}) #post도 사전형 객체를 통해 return해준다.

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details':details})

def new(request): #new.html을 띄워주는 함수
    return render(request, 'new.html')

def create(request): #입력받은 내용을 데이터 베이스에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now() #블로그를 작성한 시점을 넣어주는 함수(없어도 되는 함수)
    blog.save() #Database에 저장해준다. <-> blog.delete(): 지워준다.
    return redirect('/blog/'+str(blog.id)) #url은 항상 str이다. <-> blog.id: int type

def blogpost(request):
    # 1. 입력된 내용을 처리하는 기능 -> POST
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid(): 
            post = form.save(commit = False)# if true
            post.pub_date = timezone.now() #지금 시간
            # title과 body는 입력공간에서 넣어준 값이 들어갈 것이다.
            post.save()
            return redirect('home')

    # 2. 빈 page를 띄워주는 기능 -> GET
    else: # request.method == 'GET'
        form = BlogPost()
        return render(request, 'new.html', {'form':form}) #비어있는 객체 반환