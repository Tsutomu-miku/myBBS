from django.urls import include
from django.conf.urls import url,re_path
from . import views

from django.conf import settings
from django.contrib.auth import views as auth_views
# from django.contrib.auth.decorators import permission_required
# permission_required({'login_url':'account/'})
app_name = 'account'
urlpatterns = [
    # url(r'^login/$',views.user_login,name="user_login"),
    url('login/', auth_views.LoginView.as_view(), name='user_login'),
    ## url('new_login/', auth_views.LoginView.as_view(),  {'template_name':'account/login.html'}),
    # 目前不可用
    url('logout/', auth_views.LogoutView.as_view(),name='user_logout'),
    url('register/', views.register,name='user_register'),

    url(r'^password_change/$', auth_views.PasswordChangeView.as_view(success_url = '/account/password_change_done') ,name='password_change'),
    url(r'^password_change_done/$', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    url('password_reset/', auth_views.PasswordResetView.as_view(success_url = '/account/password_reset_done'), name='password_reset'),
    url('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    url('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(success_url = '/account/password_reset_complete',), name='password_reset_confirm'),
    url('reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    url(r'^my_information/$',views.myself,name="my_information"),
    url(r'^edit_my_information/$',views.myself_edit,name="edit_my_information"),

    url('my_image/',views.my_image,name="my_image")
]