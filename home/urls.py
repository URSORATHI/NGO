# -*- coding: utf-8 -*-
from django.urls import include, path
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from .views import ProfileView, PostListView, PostDeleteView, PostUpdateView, PostDetailView
#CategoryView,  PostCreateView

app_name='home'

urlpatterns = [
    path('home', views.home, name ='home'),
    path('donate', PostListView.as_view(), name ='donate'),
    path('contact', views.contact, name ='contact'),
    path('register', views.register, name="register"),
    path('profile', views.profile, name="profile"),
    path('profile/<pk>/', ProfileView.as_view(), name='profile-view'),
    url('login1', auth_views.LoginView.as_view(template_name='login.html'), name="login1"),
    url('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
    url('reset_password', 
         auth_views.PasswordResetView.as_view(template_name='password_reset.html'), 
         name="reset_password"),

    url('password_reset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), 
         name="password_reset_done"),

    path('reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), 
         name="password_reset_confirm"),

    path('reset/done/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), 
         name="password_reset_complete"),
    
    path('dashboard', views.dashboard, name='dashboard'),
#   path('post/new/', PostCreateView.as_view(), name='newpost'),
    path('post/<int:pk>/', PostDetailView, name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
#   path('category/<str:cats>/', CategoryView, name='category'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)