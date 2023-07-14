from django.contrib import admin
from django.urls import path
from pagina.views import home_view, cursos_view, pago_view, profile_view, sobreNosotros_view, Formulario_view, equipocurso_view, disejuegocurso_view, cybercurso_view, javacurso_view, disejuegocurso_view, htmlcurso_view, iacurso_view, lenprocurso_view, pycurso_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='index'),
    path('cursos/', cursos_view, name='cursos'),
    path('pago/', pago_view, name='pago'),
    path('profile/', profile_view, name='profile'),
    path('sobreNosotros/', sobreNosotros_view, name='sobreNosotros'),
    path('Formulario/', Formulario_view, name='Formulario'),
    path('equipocurso/', equipocurso_view, name='equipocurso'),
    path('disejuegocurso/', disejuegocurso_view, name='disejuegocurso'),
    path('cybercurso/', cybercurso_view, name='cybercurso'),
    path('javacurso/', javacurso_view, name='javacurso'),
    path('disejuegocurso/', disejuegocurso_view, name='disejuegocurso'),
    path('htmlcurso/', htmlcurso_view, name='htmlcurso'),
    path('iacurso/', iacurso_view, name='iacurso'),
    path('lenprocurso/', lenprocurso_view, name='lenprocurso'),
    path('pycurso/', pycurso_view, name='pycurso')
]
