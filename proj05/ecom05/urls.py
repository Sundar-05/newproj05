from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="AppHome!"),
    path("about/", views.about, name="About!"),
    path("contact/", views.contact, name="Contact!"),
    path("productview/", views.productview, name="ProductView!"),
    path("search/", views.search, name="Search!"),
]
