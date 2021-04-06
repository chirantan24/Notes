from django.urls import path
from notesapp import views
app_name='app'
urlpatterns = [
path('create/',views.CreateNote.as_view(),name='create'),
path('notes/',views.ListNotes.as_view(),name='notes'),
path('notes/edit/<pk>',views.EditNotes.as_view(),name='edit'),
path('notes/<pk>',views.DetailNotes.as_view(),name='detail'),
path('notes/delete/<pk>',views.NotesDelete.as_view(),name='delete')
]
