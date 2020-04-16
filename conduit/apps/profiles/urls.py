from django.urls import path

from .views import ProfileRerieveAPIView

app_name = 'profiles'
urlpatterns =[
    path('profiles/<str:username>', ProfileRerieveAPIView.as_view())
]
