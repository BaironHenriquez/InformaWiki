from django.shortcuts import render

def home_view(request):
    # Código para procesar la solicitud y preparar los datos
    # ...

    return render(request, 'index.html')

def cursos_view(request):
    return render(request, 'cursos.html')

def pago_view(request):
    return render(request, 'pago.html')

def profile_view(request):
    return render(request, 'profile.html')

def sobreNosotros_view(request):
    return render(request, 'sobreNosotros.html')










