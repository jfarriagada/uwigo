from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


CHOICE_STATE = (('open', _('Abierto')), ('pending', _('Pendiente')), 
        ('progress', _('En proceso')), ('resolved', _('Resuelto')),
        ('close', _('Cerrado')))


class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    ticket_id = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    state = models.CharField(max_length=20, default="open", choices=CHOICE_STATE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.title)
