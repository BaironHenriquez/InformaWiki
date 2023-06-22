from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from Pagina.views import home_view, cursos_view, pago_view, profile_view,sobreNosotros_view,Formulario_view

from Pagina import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='index'),
    path('Cursos.html/', cursos_view, name='cursos' ),
    path('pago.html/', pago_view, name='pago' ),
    path('profile.html/', profile_view, name='profile' ),
    path('sobreNosotros.html/', sobreNosotros_view, name='sobreNosotros' ),
    path('Formulario.html/',Formulario_view,name='Formulario'),
    

]


    

