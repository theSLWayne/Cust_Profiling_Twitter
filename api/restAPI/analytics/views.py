from types import MappingProxyType
from django.shortcuts import render
import logging

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from analytics.models import Customer, Cluster
from analytics.serializers import CustomerSerializer, ClusterSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes

# Create your views here.

@api_view(['GET', 'POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated, ))
def cluster_list(request):
    if request.method == 'POST':
        cluster_data = JSONParser().parse(request)
        cluster_serializer = ClusterSerializer(data=cluster_data)
        if cluster_serializer.is_valid():
            cluster_serializer.save()
            return JsonResponse(cluster_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(cluster_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        clusters = Cluster.objects.all()

        clusters_serializer = ClusterSerializer(clusters, many=True)
        return JsonResponse(clusters_serializer.data, safe=False)

@api_view(['POST'])
def cluster_add_cust(request):
    if request.method == 'POST':
        customer_data = JSONParser().parse(request)
        customer_serializer = CustomerSerializer(data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse(customer_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticated, ))
def cluster_get_cust(request, cluster):
    if request.method == 'GET':
        customers = Customer.objects.filter(cluster=cluster)
        customers_serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(customers_serializer.data, safe=False)
