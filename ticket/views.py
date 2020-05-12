from django.shortcuts import render, redirect, get_object_or_404
from .models import Ticket, TicketStatus
from account.models import Account
from .forms import TicketCreateForm, TicketStatusForm
from django.views.generic import View, ListView, DetailView
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

def all_ticket_view(request):
    ticket = TicketStatus.objects.all()
    return render(request, 'ticket/show_tickets.html', {'ticket':ticket})

class TicketDetailView(View):
    def get(self, request, pk):
        context = {}
        ticket = get_object_or_404(TicketStatus, pk=pk)
        form = TicketStatusForm(instance=ticket)
        context = {
            'ticket_detail' : ticket,
            'status_form':form
        }
        return render(request, 'ticket/ticket_detail.html', context)
    def post(self, request, pk):
        context = {}
        ticket = get_object_or_404(TicketStatus, pk=pk)
        if self.request.method == "POST":
            
            form = TicketStatusForm(self.request.POST)
            if form.is_valid():
                ts = form.save(commit=False)
                ticket_num = form.cleaned_data.get('ticket_num')
                ticket_qs = Ticket.objects.filter(user = self.request.user, ticket_num = ticket_num)
                if ticket_qs.exists():
                    ticket = ticket_qs[0]
                ts.ticket = ticket
                form.save()
                return redirect("ticket:ticket_detail")
            else:
                form = TicketStatusForm(instance=ticket)
                context['status_form'] = form
        else:
            form = TicketStatusForm(instance=ticket)
            return render(self.request, 'ticket/ticket_detail.html', context)
        

def get_ticket_detail_view(request, pk):
    context = {}
    ticket = get_object_or_404(TicketStatus, pk=pk)
    form = TicketStatusForm(instance=ticket)
    context = {
        'ticket_detail' : ticket,
        'status_form':form
    }
    return render(request, 'ticket/ticket_detail.html', context)

def add_ticket_status_view(request, pk):
    context ={}
    if request.method == "POST":
        form = TicketStatusForm(request.POST)
        if form.is_valid():
            ts = form.save(commit=False)
            ticket_num = form.cleaned_data.get('ticket_num')
            ticket_qs = Ticket.objects.filter(user = request.user, ticket_num = ticket_num)
            if ticket_qs.exists():
                ticket = ticket_qs[0]
            ts.ticket = ticket
            form.save()
            return redirect("ticket:ticket_detail")
            
                
                



    


#def create_ticket_view(request):
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

class CreateTicketView(View):
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
            
            #ticket_status = get_object_or_404(Ticket, pk=pk)
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
                form.save()
                return redirect("ticket:show_tickets")
            else:
                messages.info(self.request, "Form not valid")
                return redirect("create_ticket")

        except ObjectDoesNotExist:
            messages.warning(self.request, "You don't have a ticket")
            return redirect("ticket/create_ticket")


    def get(self, *args, **kwargs):
        try:
            ticket = TicketStatus.objects.get()
        except expression as identifier:
            pass