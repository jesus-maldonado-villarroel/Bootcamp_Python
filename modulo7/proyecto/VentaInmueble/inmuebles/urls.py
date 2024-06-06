from django.urls import path
from .views import index, register, register_profile, update_profile, profile, register_inmueble, obtener_inmueble, update_inmueble, listar_inmuebles_disponibles, contact, messages
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', index, name='home'),
    path('login/', LoginView.as_view(next_page='profile'), name='login_url'),
    path('logout/', LogoutView.as_view(next_page='login_url'), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('register_profile/', register_profile, name='register_profile'),
    path('update_profile/', update_profile, name='update_profile'),
    path('register_inmueble/<str:username>/',
         register_inmueble, name='register_inmueble'),
    path('update_inmueble/<int:inmueble_id>/',
         update_inmueble, name='update_inmueble'),
    path('inmuebles/', obtener_inmueble, name='obtener_inmueble'),
    path('inmuebles_disponibles/', listar_inmuebles_disponibles,
         name='listar_inmuebles_disponibles'),
    path('contact/<int:id>/', contact, name='contact'),
    path('messages/', messages, name='mensaje'),
]
