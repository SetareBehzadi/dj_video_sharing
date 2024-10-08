from django.shortcuts import render
from rest_framework import generics


# Create your views here.
class AccountsListView(generics.ListAPIView):
    pass

class AccountsDetailView(generics.AccountsDetailView):
    pass