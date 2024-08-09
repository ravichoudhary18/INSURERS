from rest_framework import serializers
from file.models import File, Insurance


class FileSerializer(serializers.Serializer):
    
    file = serializers.FileField(required=False)
    
    class Meta:
        fields = ['file']
    
    def validate_file(self, value):
        if value.content_type not in [
            'application/vnd.ms-excel',  # For .xls files
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'  # For .xlsx files
        ]: 
            raise serializers.ValidationError({'error': 'Only Excel files are accepted.'})
            
        return value
    
    def create(self, validated_data):
        file_instance = File.objects.create(**validated_data)
        return {
            'instance': file_instance,
            'id': file_instance.file_id,
            'file': file_instance.file.url,  # This returns the file URL
            'file_path': file_instance.file.path  # This returns the file system path
        }


class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = ['year', 'month', 'clubbed_name', 'category', 'product', 'value', 'created_at', 'updated_at']
        extra_kwargs = {
                'created_by': {'required': False},
                'updated_by': {'required': False},
        }