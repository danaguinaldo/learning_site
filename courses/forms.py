from django import forms

from . import models

class QuizForm(forms.ModelForm):
    class Meta:
        model = models.Quiz
        fields = [
            'title',
            'description',
            'order',
            'total_questions',
        ]

class TrueFalseQuestionForm(forms.ModelForm):
    class Meta:
        model = models.TrueFalseQuestion
        fields = ['order', 'prompt']


class MultipleQuestionForm(forms.ModelForm):
    class Meta:
        model = models.MultipleQuestion
        fields = [
            'order',
            'prompt',
            'shuffle_answers',
        ]