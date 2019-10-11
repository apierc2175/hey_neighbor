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


# Create your views here.
def index(request):
    record_list = Records.objects.all()

    context = {
        'record_list': record_list,
    }

    return render(request, 'records/index.html', context)

def my(request):
    record_list = Records.objects.all()
    context = {
        'record_list': record_list,
    }

    return render(request, 'records/my.html', context)

def user_list(request):
    users = "test"
    context = {
        'users': users,
    }

    return render(request, 'records/user_list.html', context)


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
