from django.shortcuts import render, redirect
from department.models import Department
from .models import Blog, Comment
from doctor.models import DoctorProfile
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

# Create your views here.

User = get_user_model()

@login_required(login_url='/sign-in/')
def myBlogs(request):
    current_user = DoctorProfile.objects.filter(user__username = request.user).first()
    blogs = Blog.objects.filter(user = current_user)

    return render(request, 'MyBlogs.html', {
        'blogs':blogs
    })

@login_required(login_url='/sign-in/')
def writeBlog(request):
    allDept = Department.objects.all()

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        selected_category = request.POST.getlist('category')
        cover_img = request.FILES.get('cover-img')
        user = DoctorProfile.objects.filter(user__username = request.user.username).first()

        blog = Blog.objects.create(
            user = user,
            title = title, 
            content = content, 
            category = selected_category, 
            cover_img = cover_img
        )
        blog.save()

        return redirect('/my-blogs/')


    return render(request, 'WriteBlog.html', {
        'departments': allDept
    })

def readBlog(request, mySlug):
    blog = Blog.objects.filter(slug = mySlug).first()
    commentData = Comment.objects.filter(blog_post = blog)

    if request.user.is_authenticated:
        if request.method == 'POST':
            user = User.objects.filter(username = request.user.username).first()
            content = request.POST.get('content')

            data = Comment.objects.create(
                user = user, 
                content = content, 
                blog_post = blog,
            )

            data.save()
            commentData = Comment.objects.filter(blog_post = blog)

            return redirect(f'/blogs/{mySlug}')
    else:
        return redirect('/sign-in/')


    return render(request, 'Blog.html', {
        'blog':blog,
        'comments':commentData
    })

def has_common_elements(list1, list2):
    return bool(set(list1) & set(list2))

def allBlogs(request):
    departments = Department.objects.all()
    blogs = Blog.objects.all()

    if request.method == 'POST':
        if 'apply-filter' in request.POST:
            newList = []
            selected_filter = request.POST.getlist('category')
            for blog in blogs:
                blogList = list(blog.category)
                if has_common_elements(selected_filter, blogList):
                    newList.append(blog)

            departments = Department.objects.all()  
            if selected_filter:
                data = {
                'departments':departments,
                'filters':selected_filter,
                'blogs':newList
                }
            
            else:
                data = {
                'departments':departments,
                'filters':selected_filter,
                'blogs':newList
                }
            
            
            return render(request, 'AllBlogs.html', data)
        else:
            pass

    return render(request, 'AllBlogs.html', {
        'departments':departments,
        'blogs':blogs
    })

@login_required(login_url='/sign-in/')
def updateBlog(request, mySlug):
    blog = Blog.objects.filter(slug = mySlug).first()

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        cover_img = request.FILES.get('cover-img')

        blog = Blog.objects.filter(slug = mySlug).first()
        blog.title = title
        blog.content = content
        if cover_img is not None:
            blog.cover_img = cover_img

        blog.save()

        return redirect('/my-blogs/')


    return render(request, 'UpdateBlog.html', {
        'blog':blog
    })

@login_required(login_url='/sign-in/')
def deleteBlog(request, mySlug):
    blog = Blog.objects.filter(slug = mySlug).first()
    blog.delete()

    return redirect('/my-blogs/')
