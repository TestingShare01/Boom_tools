
from django.contrib import admin
from django.urls import path
from Tools_User import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("login",views.Login.as_view()),
    path("dev",views.DevList.as_view()),
    path("tag",views.ApiTag.as_view())
]
