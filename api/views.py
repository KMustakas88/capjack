from django.shortcuts import render
from rest_framework import serializers

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from .models import Segments
from .serlializers import SegmentSerializer

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/segment-list/',
		'Detail View':'/segment-detail/<str:pk>/',
		'Create':'/segment-create/',
		'Update':'/segment-update/<str:pk>/',
		'Delete':'/segment-delete/<str:pk>/',
		}

	return Response(api_urls)

# Segments API
@api_view(['GET'])
def apiSegmentList(request):
    segments = Segments.objects.all()
    serializer = SegmentSerializer(segments, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def apiSegmentDetail(request, pk):
    segment = Segments.objects.get(_id=pk)
    serializer = SegmentSerializer(segment, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def apiSegmentCreate(request):
	serializer = SegmentSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()
    
	return Response(serializer.data)

@api_view(['POST'])
def apiSegmentUpdate(request, pk):
    segment = Segments.objects.get(_id=pk)
    serializer = SegmentSerializer(instance=segment, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
