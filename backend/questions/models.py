from django.db import models

class Question(models.Model):
    TEXT = 'text'
    MULTIPLE_CHOICE = 'multiple_choice'
    TRUE_FALSE = 'true_false'
    MATCHING = 'matching'

    QUESTION_TYPES = [
        (TEXT, 'Texto (completar)'),
        (MULTIPLE_CHOICE, 'Selección múltiple'),
        (TRUE_FALSE, 'Verdadero/Falso'),
        (MATCHING, 'Unir columnas'),
    ]

    question_type = models.CharField(max_length=40, choices=QUESTION_TYPES)
    text = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.TextField() 
    is_correct = models.BooleanField(default=False) 

    def __str__(self):
        return self.text