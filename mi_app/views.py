from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')  # Redirige a la página de inicio de sesión o donde desees
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})




def home(request):
    return render(request, 'home.html')  # Asegúrate de crear este archivo de plantilla


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirige a la página de inicio después de iniciar sesión
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas'})
    return render(request, 'login.html')
