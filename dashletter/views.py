from django.shortcuts import render

dummy_data = [
    {
        'businesses': 'Steve Jobs',
        'content': 'First content',
        'uploaded_date': 'November 30, 2018'
    },
    {
        'businesses': 'Bill Gates',
        'content': 'Second content',
        'uploaded_date': 'December 1, 2018'
    }
]

def home(request):
    context = {
        'dummy_data': dummy_data
    }
    return render(request, 'dashletter/home.html', context, {'title': 'Home'})

def about(request):
    return render(request, 'dashletter/about.html', {'title': 'About'})
