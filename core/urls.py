from django.urls import path
from .views import home
from .views import galeria
from .views import encabezado
from .views import evaluacion
from .views import consulta

urlpatterns= {
    path('',home,name="home"),
    path('galeria/',galeria,name="galeria"),
    path('encabezado/',encabezado,name="encabezado"),
    path('evaluacion/',evaluacion,name="evaluacion"),
    path('consulta/',consulta,name="consulta")
}