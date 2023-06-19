from django.urls import path
from medical import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('registration/', views.registration, name='registration'),
    path('home/', views.home, name='home'),
    path('appointment/', views.appointment, name='appointment'),
    path('appoint/', views.appoint, name='appoint'),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)