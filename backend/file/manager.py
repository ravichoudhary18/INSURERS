from django.db import models
from django.db.models import F

class InsuranceManager(models.Manager):

    def download_file(self, id):
        
        return self.filter(file=id).annotate(
                Year = F('year'),
                Month = F('month'),
                Product = F('product'),
                Value = F('value')
            ).values(
                'Year',
                'Month',
                'Product',
                'Value',
                'category',
                'clubbed_name'
            ).order_by('clubbed_name', 'category', 'Product')