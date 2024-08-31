from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # auth
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),

    # TODO delete note
    # TODO delete folder

    # TODO update note
    # TODO update folder

    # TODO create note
    # TODO create folder
]