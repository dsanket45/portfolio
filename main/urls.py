from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
]

# from django.urls import path
# from .views import contact_form_submission

# urlpatterns = [
#     path('submit-contact/', contact_form_submission, name='submit-contact'),
# ]

from django.urls import path
from . import views  # Import views from the app

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('submit-contact/', views.contact_form_submission, name='submit-contact'),  # Contact form
]
