
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import ScheduleModel
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .forms import ScheduleCompleteForm

def home_view(request):
    return render(request, 'home.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = f"{name}さんからのお問い合わせ"
            body = f"送信者: {name}\nメールアドレス: {email}\n\n内容:\n{message}"
            send_mail(subject, body, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def schedule_list_view(request):
    title_query = request.GET.get('title', '')
    start_date_query = request.GET.get('start_date', '')

    schedules = ScheduleModel.objects.all()
    if title_query:
        schedules = schedules.filter(title__icontains=title_query)
    if start_date_query:
        schedules = schedules.filter(start_time__date=start_date_query)

    context = {
        'schedules': schedules,
    }
    return render(request, 'schedule_list.html', context)

def schedule_list(request):
    schedules = ScheduleModel.objects.all()
    return render(request, 'schedule_list.html', {'schedules': schedules})

def schedule_complete(request, pk):
    schedule = get_object_or_404(ScheduleModel, pk=pk)
    schedule.is_completed = True
    schedule.save()
    return redirect('schedule:schedule_list')

class ScheduleList(ListView):
    model = ScheduleModel
    template_name = 'schedule_list.html'
    context_object_name = "schedules"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        title_query = self.request.GET.get('title', None)
        start_date = self.request.GET.get('start_date', None)
        if title_query:
            queryset = queryset.filter(title__icontains=title_query)
        if start_date:
            queryset = queryset.filter(start_time__date=start_date)
        return queryset


class ScheduleCreate(CreateView):
    model = ScheduleModel
    fields = ['title', 'description', 'start_time', 'end_time']
    template_name = 'schedule_create.html'
    success_url = reverse_lazy('schedule:schedule_list')

    extra_context = {'action': '作成'}


class ScheduleUpdate(UpdateView):
    model = ScheduleModel
    fields = ['title', 'description', 'start_time', 'end_time']
    template_name = 'schedule_update.html'
    success_url = reverse_lazy('schedule:schedule_list')  # 名前空間を含める


class ScheduleDelete(DeleteView):
    model = ScheduleModel
    template_name = 'schedule_delete.html'
    success_url = reverse_lazy('schedule:schedule_list')  # 名前空間を含める

