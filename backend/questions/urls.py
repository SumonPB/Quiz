from django.urls import path
from .views import UploadQuestionsView, QuestionListView  # Importa la nueva vista

urlpatterns = [
    path('upload/', UploadQuestionsView.as_view(), name='upload-questions'),
    path('questions/', QuestionListView.as_view(), name='question-list'),  # Nueva ruta
]