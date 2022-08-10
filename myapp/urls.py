from django.urls import path
from  django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from djangoProject3 import settings
from . import views

urlpatterns = [
    path('', views.home, name='site'),
    path('home', views.home, name='home'),
    path('login', views.loginsite, name='login'),
    path('logout', views.logoutsite, name='logout'),
    path('regist', views.register, name='registration'),
    #path('home', views.new),
    path('home1', views.home1, name="home1"),
    path('database', views.datab_data, name='datab_data'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('profile', views.profiledata, name='profile'),
    path('signUp1', views.signUp1, name='signUp1'),
    path('single/<int:movie_id>', views.single, name='single'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)