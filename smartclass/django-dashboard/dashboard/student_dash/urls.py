from django.urls import path
from django.conf.urls   import include
from .views import prof_dashboard, Attendence_data

urlpatterns = [
    path('ew/', prof_dashboard),
    path('ew/attendence_data/', Attendence_data.as_view(), name='attendence_data'),
]