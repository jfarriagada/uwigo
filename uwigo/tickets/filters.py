import django_filters
from django_filters.filters import CharFilter, ChoiceFilter, DateFilter
from .models import Ticket, CHOICE_STATE


class TicketFilter(django_filters.FilterSet):
    ticket_id = CharFilter(label='ID', lookup_expr='icontains')
    title = CharFilter(label='Título', lookup_expr='icontains')
    description = CharFilter(label='Descripción', lookup_expr='icontains')
    state = ChoiceFilter(label='Estado', choices=CHOICE_STATE)
    start_date = DateFilter(label='Fecha mayor que DD/MM/YY', field_name='created', lookup_expr='gte')
    end_date = DateFilter(label='Fecha menor que DD/MM/YY', field_name='created', lookup_expr='lte')

    class Meta:
        model = Ticket
        fields = ('ticket_id','title','description','state','created')
        exclude = ['created']