from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# TODO: Add the following
# 1. model = enum of models(choices)
# 2. role = enum of roles(choices)

class QnAForm(forms.Form):
    question = forms.CharField(required=True, max_length=500)

    def clean_question(self):
        # TODO: Use tiktoken to validate and generate cost
        q: str = self.cleaned_data["question"]
        if len(q) >= 500:
            raise ValidationError(_('Question is too long'))
        return q

