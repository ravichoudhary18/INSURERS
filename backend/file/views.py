from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from file.serializers import FileSerializer
from file.utils import ReadingExcelFile

class FileView(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, requests):
        return Response({'file': 'runing'}, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = request.data.copy()

        serializer = FileSerializer(data=data)
        if serializer.is_valid():
            file_data = serializer.save(
                created_by = request.user,
                updated_by = request.user,
            )
            read_file = ReadingExcelFile(file_data.get('file_path', None))
            df = read_file.extract_file_info()
            df_combined = read_file.cleaning_file(df)
            return Response(file_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)