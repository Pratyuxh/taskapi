from http.client import HTTPResponse


from django.urls import HttpResponse

def home_page(request):
    print("home page requested")
    return HTTPResponse("This is Home Page")

