from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainPageView.as_view(), name='main_page'),
    path('login/', views.LoginPageView.as_view(), name='login_page'),
    path('logout/', views.logout_view, name='logout_page'),
    path('register/', views.RegisterPageView.as_view(), name='register_page'),
    path('update/<slug:user_slug>/', views.UpdatePageView.as_view(), name='update_page'),
]
