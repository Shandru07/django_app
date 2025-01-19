from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from blog.models import Post
from.forms import ContactForm

# Create your views here.
# post_title = [
#         {'id':1,'title': 'Post 1','content': 'Content of Post 1'},
#         {'id':2,'title': 'Post 2','content': 'Content of Post 2'},
#         {'id':3,'title': 'Post 3','content': 'Content of Post 3'},
#         {'id':4,'title': 'Post 4','content': 'Content of Post 4'},
#     ]

def index(request):
    blog_title = 'Latest Posts'
    post_title = Post.objects.all()
    return render(request,'index.html',{'blog_title':blog_title,'post_title':post_title})

def detail(request,post_id):
    # post = next((item for item in post_title if item['id'] == int(post_id)),None)

    post = Post.objects.get(pk=post_id)
    
    return render(request,'detail.html',{'post':post})

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("This is the new url")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        massage = request.POST.get('massage')

        logger = logging.getLogger("Testing")
        if form.is_valid():
            logger.debug(f"post data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}")
            success_massage = 'SUCCESS 👍🏻'
            return render(request,'contact.html',{'form':form,'success_massage':success_massage })
        else:
           logger.debug("Form validation failure")
        return render(request,'contact.html',{'form':form,'name':name,'email':email,'massge':massage})
    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')
