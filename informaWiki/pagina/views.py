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

def Formulario_view(request):
    return render(request,'Formulario.html')

def cybercurso_view(request):
    return render(request, 'cybercurso.html')

def disejuegocurso_view(request):
    return render(request, 'disejuegocurso.html')

def equipocurso_view(request):
    return render(request, 'equipocurso.html')

def htmlcurso_view(request):
    return render(request, 'htmlcurso.html')

def iacurso_view(request):
    return render(request, 'iacurso.html')

def javacurso_view(request):
    return render(request, 'javacurso.html')

def lenprocurso_view(request):
    return render(request, 'lenprocurso.html')

def pycurso_view(request):
    return render(request, 'pycurso.html')
