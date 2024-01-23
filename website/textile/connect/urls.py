# users/urls.py

from django.urls import path
from .views import user_signup, user_login, owner_dashboard, worker_dashboard, owner_publish_form, worker_profile, owner_list, filtered_owners, filtered_workers, worker_list

urlpatterns = [
    path('', user_login, name='user_login'),
    path('user_signup/', user_signup, name='user_signup'),
    path('owner_dashboard/', owner_dashboard, name='owner_dashboard'),
    path('owner/owner_publish_form', owner_publish_form, name='owner_publish_form'),
    path('owner/worker_list', worker_list, name='worker_list'),
    path('worker_dashboard/', worker_dashboard, name='worker_dashboard'),
    path('worker/worker_profile/', worker_profile, name='worker_profile'),
    path('worker/owner_list/', owner_list, name='owner_list'),
    path('api/filtered-owners/', filtered_owners, name='filtered_owners'),
    path('api/filtered-workers/', filtered_workers, name='filtered_workers'),
]
