from django.conf.urls import url
from django.urls import path,re_path
from django.contrib.auth.decorators import login_required
from apps.user.views import RegisterView, ActiveView, LoginView, LogoutView, UserInfoView, UserOrderView, AddressView

urlpatterns = [
    # url(r'^register$', views.register, name='register'), # 注册
    # url(r'^register_handle$', views.register_handle, name='register_handle'), # 注册处理

    path('register', RegisterView.as_view(), name='register'), # 注册
    re_path(r'^active/(?P<token>.*)$', ActiveView.as_view(), name='active'), # 用户激活

    path('login', LoginView.as_view(), name='login'), # 登录
    path('logout', LogoutView.as_view(), name='logout'), # 注销登录

    # url(r'^$', login_required(UserInfoView.as_view()), name='user'), # 用户中心-信息页
    # url(r'^order$', login_required(UserOrderView.as_view()), name='order'), # 用户中心-订单页
    # url(r'^address$', login_required(AddressView.as_view()), name='address'), # 用户中心-地址页

    path('', UserInfoView.as_view(), name='user'), # 用户中心-信息页
    re_path(r'^order/(?P<page>\d+)$', UserOrderView.as_view(), name='order'), # 用户中心-订单页
    re_path(r'^address$', AddressView.as_view(), name='address'), # 用户中心-地址页
]