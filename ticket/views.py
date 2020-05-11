from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket, TicketStatus
from account.models import Account
from .forms import TicketCreateForm
from django.views.generic import View, ListView, DetailView
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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

#def edit_status_view(request, pk):
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

class TicketView(View):
    def get(self, *args, **kwargs):
        context = {}
        form = TicketCreateForm()
        context = {
            'form':form
        }

        return render(self.request, 'ticket/create_ticket.html', context)
    def post(self, *args, **kwargs):
        form = TicketCreateForm(self.request.POST or None)
        try:
            
            ticket_status = get_object_or_404(Ticket, pk=pk)
            if form.is_valid:
                tick = form.save(commit=False)
                full_name = form.cleaned_data.get('full_name')
                ticket_num = form.cleaned_data.get('ticket_num')
                station = form.cleaned_data.get('station')
                ticket_category = form.cleaned_data.get('ticket_category')
                description = form.cleaned_data.get('description')
                tick = Ticket(
                    user = self.request.user,
                    ticket_num = ticket_num,
                    full_name = full_name,
                    station = station,
                    ticket_category = ticket_category,
                    description = description

                )
                tick.save()
                ticket_status.ticket = tick
                ticket_status.save()
            else:
                messages.info(self.request, "Form not valid")
                return redirect("create_ticket")

        except ObjectDoesNotExist:
            messages.warning(self.request, "You don't have a ticket")
            return redirect("create_ticket")

