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

# Create your views here.
def index(request):
    record_list = Records.objects.all()

    context = {
        'record_list': record_list,
    }

    return render(request, 'records/index.html', context)
