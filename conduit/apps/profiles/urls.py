from django.urls import path

from .views import ProfileRerieveAPIView, ProfileFollowAPIView

app_name = 'profiles'
urlpatterns =[
    path('profiles/<str:username>', ProfileRerieveAPIView.as_view()),
    path('profiles/<str:username>/follow', ProfileFollowAPIView.as_view()),
]
