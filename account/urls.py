from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

# app_name = 'account'

urlpatterns = [
    # path('login/', views.user_login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),

    # # login/logout urls
    # path('login/', auth_views.LoginView.as_view(), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # # change password urls
    # path('password-change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # # reset password urls
    # path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # below urls is the Urls pattern provided by Django for authentication view that are equivalen to the above urls that we created
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),



]

# when user is logged out, it redirect to admin logout page ????????????

# LogoutView redirect user to Logged_out.html page from registration after being logout 

#  check the INSTALLED_APPS setting of your project and make sure that django.
# contrib.admin comes after the account application.

# LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView are class based views provided by Django Authentication