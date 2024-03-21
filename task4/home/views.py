from django.shortcuts import render,HttpResponse

def home(request):
    dynamic_data = {
        'name': 'Akshay',
        'age': 25,
        'company': 'Tyloones software private limited'
    }
    
    # context = {'data': dynamic_data}
    return render(request, 'index.html', dynamic_data)

def about(request):
    return HttpResponse("hello from about")

def contact(request):
    return HttpResponse("hello from contact")
