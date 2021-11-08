from django.contrib import admin
from .models import *


class TicketAdmin(admin.ModelAdmin):
    list_display = ('user','ticket_id','title','description','state','created')
    list_filter = ('state',)
    search_fields = ['user__username','ticket_id','title','description']


admin.site.register(Ticket, TicketAdmin)
