from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView
#reverse lazy allows it to fully complete before executing
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from .models import Records
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

User = get_user_model()

# on page do like beginning where you return all of the records by all users then add a field in each one of owner
#is adding user based records either adding pk somewhere or when they add in models their username is a variable and when shown in my.html do something like if username = username then print this info
# Create your views here.
def index(request):
    record_list = Records.objects.all()

    context = {
        'record_list': record_list,
    }

    return render(request, 'records/index.html', context)

def my(request):
    record_list = Records.objects.filter(owner=request.user)
    context = {
        'record_list': record_list,
    }

    return render(request, 'records/my.html', context)

def user_list(request):
    users = [str(user) for user in User.objects.all()]
    record_list = Records.objects.all()
    context = {
        'users': users,
        'record_list': record_list,
    }

    return render(request, 'records/user_list.html', context)

#below gets to someones account when you click on it
# def user_items(request, id):
#     user_items = UserProfile.objects.get(pk=id)
#     context = {
#         'user_items': user_items,
#     }
#
#     return render(request, 'records/user_items', context)

# def user_items(request):
#     record_list = Records.objects.all()
#
#     context = {
#         'record_list': record_list,
#     }
#
#     return render(request, 'records/user_list.html', context)

class UserItems(generic.CreateView):
    model = Records
    # fields = UserProfile.objects.get(pk=id)
    fields = '__all__'
    template_name = 'records/user_items'



class CreateView(generic.CreateView):
    model = Records
    fields = '__all__'
    template_name = 'records/create.html'

class DeleteView(generic.DeleteView):
    model = Records
    success_url = reverse_lazy('records:index')
    template_name = 'records/delete.html'

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')


    # return HttpResponseRedirect(reverse('records:index'))
