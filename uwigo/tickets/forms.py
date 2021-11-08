from django import forms
from .models import Ticket, CHOICE_STATE


class TicketForm(forms.ModelForm):
    ticket_id = forms.CharField(label="ID")
    title = forms.CharField(label="Título")
    description = forms.CharField(widget=forms.Textarea(attrs={
        'rows': '2','maxlength': '250',
    }), label="Descripción")
    state = forms.ChoiceField(choices=CHOICE_STATE, label="Estado")

    class Meta:
        model = Ticket
        fields = ('ticket_id','title','description','state')