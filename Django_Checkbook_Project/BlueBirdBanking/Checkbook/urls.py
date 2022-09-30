from django.urls import path
from . import views



urlpatterns = [
    # Balance Sheet can be displayed using a primary key
    # Sets the url path to home page index.html
    path('', views.home, name='index'),
    # Sets the url path to Create New Account page CreateNewAccount.html.
    path('create/', views.create_account, name='create'),
    # Balance Sheet can be displayed using a primary key
    path('<int:pk>/balance/', views.balance, name='balance'),
    # Sets the url path to Add New Transaction page AddNewTransaction.html.
    path('transaction/', views.transaction, name='transaction'),
]