from django.urls import path

from accounts.views import AccountsListView, AccountsDetailView

app_name = 'accounts'
urlpatterns = [
    path('', AccountsListView.as_view(), name='list'),
    path('<int:pk>/', AccountsDetailView.as_view(), name='detail'),
]