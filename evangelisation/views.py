from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelformset_factory
from django.http import JsonResponse
from django.http.response import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from twilio.rest import Client

from evangelisation.forms import PersonneForm, MessageForm, FormNbre
from evangelisation.models import Message, Personne

from evangelisation.send_sms import send_sms


@login_required(login_url="user_login")
def notification_app_index(request, pk=None):
    context = dict()
    form = None
    message = None
    messages_send = None
    personnes = None
    messages_select = None

    if pk:
        try:
            message = Message.objects.get(id=pk)
        except Message.DoesNotExist:
            raise Http404("Pages non disponible")

    if request.method=='POST':
        if pk:
            form = MessageForm(data=request.POST, instance=message)
        else:
            form = MessageForm(request.POST)
        if form.is_valid():
            if pk:
                form.save()
                is_error = send_sms(message)
                if is_error:
                    messages.error(request, f"une erreur s'est produit durant l'envoie du SMS : ce numéro n'est pas encore accepté par le service(Twilio) des SMS")
                else:
                    messages.success(request, f"Modification et SMS renvoyé avec success!!")
                return redirect('notification:notification_app_index')
            else:
                message = form.save(commit=False)
                message.author = request.user
                message.save()
                form.save_m2m()
                is_error = send_sms(message)
                if is_error:
                    messages.error(request, f"une erreur s'est produit durant l'envoie du SMS : ce numéro n'est pas encore accepté par le service(Twilio) des SMS")
                else:
                    messages.success(request, f"Votre SMS a été envoyé avec success!!")
                return redirect('notification:notification_app_index')
    else:
        if pk:
            form = MessageForm(instance=message)
            messages_send = Message.objects.all()
            context['modifié'] = True
            context['message'] = message
            
        else:
            if 'liste-message' in request.GET:
                try:
                    message = Message.objects.get(id=int(request.GET['liste-message']))
                    messages_send = Message.objects.filter(publish=message.publish)
                    context['msg_select'] = message
                except Message.DoesNotExist:
                    raise Http404("Pages non disponible")
            else:
                messages_send = Message.objects.all()
            form = MessageForm()
        context['form'] = form
        context['messages_send'] = messages_send
        context['messages_select'] = Message.objects.all()
        context['personnes'] = Personne.objects.all()
        context['select_link'] = 'sms'
    return render(request, 'index.html', context)



@login_required(login_url="user_login")
def notification_app_delete(request, pk):
    msg = get_object_or_404(Message, id=pk)
    msg.delete()
    messages.error(request, f"Supprission reuissie du message")
    return redirect('notification:notification_app_index')




@login_required(login_url="user_login")
def notification_app_recherche(request):
    context = dict()
    messages_send = None
    if 'liste-message' in request.GET:
        try:
            message = Message.objects.get(id=int(request.GET['liste-message']))
            messages_send = Message.objects.filter(publish=message.publish)
        except Message.DoesNotExist:
            raise Http404("Pages non disponible")

    form = MessageForm()
    context['form'] = form
    context['message'] = message
    context['messages_send'] = messages_send
    return redirect('notification:notification_app_index')



@login_required(login_url="user_login")
def notification_app_ajouter_personne(request):
    context = dict()
    form = None
    if request.method=='POST':
        form = PersonneForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Personne ajouté avec successe!!")
            return redirect('notification:notification_app_ajouter_personne')
    else:
        form = PersonneForm()
    context['form'] = form
    context['select_link'] = 'sms'
    return render(request, 'pages/personne/personne.html', context)


@login_required(login_url="user_login")
def notification_app_detail_personne(request, pk):
    context = dict()
    form = None
    try:
        personne = Personne.objects.get(id=pk)
    except Personne.DoesNotExist:
        raise Http404("Pages non disponible")
    if request.method=='POST':
        form = PersonneForm(data=request.POST, instance=personne)
        if form.is_valid():
            form.save()
            messages.success(request, f"Personne modification reuissie!!")
            return redirect('notification:notification_app_index')
    else:
        form = PersonneForm(instance=personne)
        context['modifier'] = True
        context['personne'] = personne
    context['form'] = form
    context['select_link'] = 'sms'
    return render(request, 'pages/personne/personne.html', context)


@login_required(login_url="user_login")
def notification_app_supprimer_personne(request, pk):
    personne = get_object_or_404(Personne, id=pk)
    for msg in personne.messages.all():
        msg.delete()
    personne.delete()
    messages.error(request, f"Supprission reuissie de la personne")
    return redirect('notification:notification_app_index')










