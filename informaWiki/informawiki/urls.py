from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from pagina.views import home_view, cursos_view, pago_view, profile_view,sobreNosotros_view,Formulario_view,equipocurso_view
from django.urls import include
from pagina import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('pagina.urls')),
]


    

