from django.http import HttpResponse


def index(request):
    return HttpResponse("HelloWorld, You're at the polls index.")
