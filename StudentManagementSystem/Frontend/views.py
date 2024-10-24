from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def getLoginForm(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == 'linda' and password == '12345':
            return render(request, 'Main.html')
        else:
            return render(request, 'LoginForm1.html')
    return render(request, 'LoginForm.html')