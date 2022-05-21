from django.urls import path
from analytics import views

urlpatterns = [
    path('clusters/', view=views.cluster_list),
    path('addcust/', view=views.cluster_add_cust),
    path('cluster/<cluster>', view=views.cluster_get_cust)
]
