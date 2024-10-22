from django.shortcuts import render

# Create your views here.


def register_view(request):
    print("hey")
    return render(request, "users/register.html")
