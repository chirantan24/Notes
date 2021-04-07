from django.shortcuts import render
from django.urls import reverse_lazy,reverse
from notesapp import forms
from django import forms as f
from notesapp import models
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,CreateView,DeleteView,ListView,DetailView,UpdateView
from django.utils import timezone

def index(request):
    return render(request,'index.html')
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    template_name='signup.html'
    success_url=reverse_lazy('login')
class CreateNote(LoginRequiredMixin,CreateView):
    login_url='login'
    template_name='createnote.html'
    model=models.Note
    fields=('title','text')
    success_url=reverse_lazy('app:notes')
    def get_form(self, form_class=None):
        form = super(CreateNote, self).get_form(form_class)
        form.fields['text'].widget = f.Textarea(attrs={"placeholder" : "Enter your text here..","rows" : 8,"cols":50    },);
        form.fields['text'].label='';
        form.fields['title'].widget= f.TextInput(attrs={"placeholder" : "Enter Title Here.."})
        return form
    def form_valid(self,form):
        self.object=form.save(commit=False)
        self.object.writer_id=self.request.user.id;
        self.object.time_created=timezone.now();
        self.object.save()
        return super(CreateNote,self).form_valid(form)
class ListNotes(LoginRequiredMixin,ListView):
    login_url='login'
    model=models.Note
    def get_queryset(self,*args,**kwargs):
        return models.Note.objects.all().filter(writer=self.request.user).order_by('-time_created');
class EditNotes(LoginRequiredMixin,UpdateView):
    login_url='login'
    model=models.Note
    fields=('title','text')
    template_name='createnote.html'
class DetailNotes(LoginRequiredMixin,DetailView):
    login_url='login'
    model=models.Note
class NotesDelete(LoginRequiredMixin,DeleteView):
    model=models.Note;
    login_url='login'
    success_url=reverse_lazy('app:notes')
