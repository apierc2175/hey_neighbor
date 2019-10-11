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

class CreateView(generic.CreateView):
    model = Records
    fields = '__all__'
    template_name = 'records/create.html'

class DeleteView(generic.DeleteView):
    model = Records
    success_url = reverse_lazy('records:index')
    template_name = 'records/delete.html'

    # return HttpResponseRedirect(reverse('records:index'))
