from django.urls import path
from basic_app import views

# TEMPLATE TAGGING
app_name = 'basic_app' # this is used in relative_url.html file

urlpatterns = [
    path('relative',views.relative,name = 'relative_name'),
    path('other',views.other,name = 'other_name'),

]
