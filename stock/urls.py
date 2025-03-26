from django.urls import path

from stock.views import stock_list

from django.contrib.auth import views as auth_views

from stock.views import stock_list, stock_detail, stock_buy

from stock.views import stock_list, stock_detail, stock_buy, account, stock_sell

app_name = 'stock'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='admin/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='stock:list'), name='logout'),
    path('list/', stock_list, name='list'),
    path('detail/<int:pk>/<str:mode>/', stock_detail, name='detail'),
    path('buy/<int:pk>/', stock_buy, name='buy'),
    path('sell/<int:pk>/', stock_sell, name='sell'),
    path('account/', account, name='account')

]

