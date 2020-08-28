from django.shortcuts import render

posts=[
    {
        'author': 'Vinay',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': '21-Aug-2020'
        
    },
    {
        'author': 'Sagar',
        'title': 'Blog post 2',
        'content': 'Other post content',
        'date_posted': '01-Aug-2020'
    }
]

def home(request):
    context={
        'posts': posts
    }
    return render(request, 'blog/home.html', context) # render func returns HttpResponse

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})