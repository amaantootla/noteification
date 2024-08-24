from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    # C
    path("create_tag", views.create_tag, name="create_tag"),
    path("create_note", views.create_note, name="create_note"),

    # R
    path("get_tags", views.get_tags, name="get_tags"),
    path("get_tag/<int:tag_id>", views.get_tag, name="get_tag"),
    path("get_notes", views.get_notes, name="get_notes"),
    path("get_note/<int:note_id>", views.get_note, name="get_note"),

    # U
    path("update_tag/<int:tag_id>", views.update_tag, name="update_tag"),
    path("update_note/<int:note_id>", views.update_note, name="update_note"),

    # D
    path("delete_tag/<int:tag_id>", views.delete_tag, name="delete_tag"),
    path("delete_note/<int:note_id>", views.delete_note, name="delete_note"),
]