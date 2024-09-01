from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # auth
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),

    path('createdit_note/<int:note_id>/<str:parent>', views.createdit_note, name='createdit_note'),
    path('delete_note/<int:note_id>/<str:parent>', views.delete_note, name='delete_note'),
]