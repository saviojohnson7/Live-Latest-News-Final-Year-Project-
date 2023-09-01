
from django.contrib import admin
from django.urls import path
from news_api_app.views import home, news, argentina

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="home"),
    path("news/", news, name="news"),
    path("argentina/", argentina, name="argentina"),
]
