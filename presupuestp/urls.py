from django.contrib import admin
from django.urls import path
from billetera import views

urlpatterns = [
    path('', views.getBadget),
    #path('', mostrarMov, name="mostrar"),
    path('movimiento/', views.Movement, name="movimiento"),
    path('borrarMovimiento/<int:pk>', views.deleteMovement, name="borrarMovimiento"),
    path('admin/', admin.site.urls),

]
