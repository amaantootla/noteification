from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    # auth
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),

    path('delete_note/<int:note_id>/<str:parent>', views.delete_note, name='delete_note'),
    path('delete_folder/<int:folder_id>', views.delete_folder, name='delete_folder'),

    # TODO delete folder

    # TODO update note
    # TODO update folder

    # TODO create note
    # TODO create folder
]