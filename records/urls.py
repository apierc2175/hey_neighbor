from django.urls import path
from . import views

app_name = 'records'

urlpatterns = [
    path("", views.index, name='index'),
    path('add/', views.CreateView.as_view(), name='create'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
    path('my/', views.my, name='my'),
    path('user_list/', views.user_list, name="user_list"),
    path('<int:pk>/user_items/', views.UserItems.as_view(), name="user_items"),
]
