from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from file.serializers import FileSerializer, InsuranceSerializer
from file.utils import ReadingExcelFile

class FileView(APIView):
    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, requests):
        return Response({'file': 'runing'}, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        user_instance = request.user

        serializer = FileSerializer(data=data)
        if serializer.is_valid():
            file_data = serializer.save(
                created_by = user_instance,
                updated_by = user_instance,
            )
            read_file = ReadingExcelFile(file_data.get('file_path', None))
            list_of_dataframs = []
            sheet_names = read_file.get_sheet_list()
            for sheet in sheet_names:
                df = read_file.remove_nan_row(sheet)
                file_info = read_file.extract_file_info(df)
                year = file_info.get('year', '')
                month = file_info.get('month', '').capitalize()[:3]
                fixing_columns = read_file.fixing_columns(df)
                cleaning_file = read_file.cleaning_file(fixing_columns)
                list_of_dataframs.append(cleaning_file)
            extract_data = read_file.extract_data(list_of_dataframs, year, month, file_data.get('instance'))
            print(extract_data)
            # insurance_seralizer = InsuranceSerializer(data=extract_data, many=True)
            # if insurance_seralizer.is_valid():
            #     serializer.save(
            #         created_by = user_instance,
            #         updated_by = user_instance,
            #     )
            # return Response({'records': insurance_seralizer.data}, status=status.HTTP_201_CREATED)
            return Response({'records': extract_data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)