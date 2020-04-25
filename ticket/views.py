from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket
from account.models import Account
from .forms import TicketCreateForm, UpdateTicketForm

# Create your views here.

def all_ticket_view(request):
    ticket = Ticket.objects.all()
    return render(request, 'ticket/show_tickets.html', {'ticket':ticket})

def get_ticket_detail_view(request, pk):
    context = {}
    ticket = get_object_or_404(Ticket, pk=pk)
    context['ticket_detail'] = ticket
    return render(request, 'ticket/ticket_detail.html', context)

def create_ticket_view(request):
    context = {}
    if request.method == "POST":
        form = TicketCreateForm(request.POST)
        if form.is_valid():
            tic = form.save(commit=False)
            tic.user = request.user
            form.save()
            return redirect('show_tickets')
        else:
            context['ticket_form'] = form
    else:
        form = TicketCreateForm()
        context['ticket_form'] = form
    return render(request, 'ticket/create_ticket.html', context)

def edit_ticket_view(request, pk):
    context = {}
    ticket = get_object_or_404(Ticket, pk=pk)

    if request.method == "POST":
        form  = TicketCreateForm(request.POST, instance=ticket)
        if form.is_valid():
            tk = form.save(commit=False)
            tk.user = request.user
            form.save()
            return redirect('show_tickets')
    else:
        form = TicketCreateForm(instance=ticket)
        context['ticket_form'] = form
    return render(request, 'ticket/edit_ticket.html', context)

def edit_status_view(request, pk):
    context = {}
    ticket = get_object_or_404(Ticket, pk=pk)

    if request.method == "POST":
        form  = UpdateTicketForm(request.POST, instance=ticket)
        if form.is_valid():
            tk = form.save(commit=False)
            tk.user = request.user
            form.save()
            return redirect('ticket_detail')
    else:
        form = UpdateTicketForm(instance=ticket)
        context['ticket_form'] = form
    return render(request, 'ticket/ticket_detail.html', context)
