# here we'll put different urls and the connect them to our views 
# views -> controller
from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"), # this path is only for the particular web app (standalone application)
    path("todos/", views.todos, name="todos")
]