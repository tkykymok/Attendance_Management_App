import django_filters
from django_filters import DateFilter
from .models import CheckInOut

class RecordFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="date_worked", lookup_expr='gte')
    end_date = DateFilter(field_name="date_worked", lookup_expr='lte')
    
    class Meta:
        model = CheckInOut
        fields = '__all__'
        exclude = ['staff', 'date_worked', 'check_in', 'check_out', 'overtime_s', 'overtime_e', 'remark']
