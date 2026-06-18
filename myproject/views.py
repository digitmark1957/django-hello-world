from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("<h1>Hello World! My modern Python journey has begun.</h1>")
