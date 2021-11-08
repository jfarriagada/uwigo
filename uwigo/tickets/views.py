from django.shortcuts import render, redirect
from .forms import TicketForm
from .models import Ticket
from .filters import TicketFilter
from django.contrib.auth.decorators import login_required, permission_required

from uwigo.settings import LOGIN_URL


@login_required(login_url=LOGIN_URL)
def index(request):
    tickets_list = Ticket.objects.all().order_by('-id')
    template = 'tickets/index.html'
    tickets_filter = TicketFilter(request.GET, queryset=tickets_list)
    tickets_list = tickets_filter.qs

    context = {
        'tickets_list': tickets_list,
        'tickets_filter': tickets_filter,
    }

    return render(request, template, context)



@login_required(login_url=LOGIN_URL)
@permission_required('tickets.add_ticket')
def create_ticket(request):
    template = "tickets/create_ticket.html"
    
    context = {
        'form':TicketForm
    }

    if request.method == 'POST':
        form = TicketForm(data=request.POST)

        if form.is_valid():
            if request.user.is_authenticated:
                ticket = form.save(commit=False)
                ticket.user = request.user
                ticket = form.save()

            return redirect('tickets')
        context['form'] = form

    return render(request, template, context)