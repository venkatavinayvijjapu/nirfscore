from django.contrib import admin
from django.urls import path
from . import views
app_name='predict'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.predictor, name='predict')
]
