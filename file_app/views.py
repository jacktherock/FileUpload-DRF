from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser 
from rest_framework.response import Response
from rest_framework import status
from .models import File
from .serializers import FileSerializer
from django.http.response import JsonResponse
from rest_framework.decorators import api_view


class FileView(APIView):
  parser_classes = (MultiPartParser, FormParser)
  def post(self, request, *args, **kwargs):
    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
      file_serializer.save()
      return Response(file_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete(request, pk):
    if request.method == 'DELETE': 
        file = File.objects.get(pk=pk)
        file.delete() 
        return JsonResponse({'message': 'File was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)