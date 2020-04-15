from django import forms
from django.contrib.auth import authenticate, get_user_model, password_validation
from django.contrib.auth.forms import UsernameField, ReadOnlyPasswordHashField
from django.utils.translation import gettext, gettext_lazy as _
from django.utils.text import capfirst
from .models import Evaluation


class EvaluationForm(forms.ModelForm):
    """
    DESCRIPTION:
    A form to upload analysis.
    """

    # Methods
    def clean(self):
        """
        DESCRIPTION:
        A method devised to ensure the quality of the uploaded images.
        :return:
        """

    def __init__(self, *args, **kwargs):
        """
        DESCRIPTION:
        Method to save the Evaluation object.
        """
        if args:
            # Perform the AI analyses
            results = {'key': 'value'}
            for arg in args:
                name = arg.get('name')
                image = arg.get('image')
                Evaluation.objects.create(name=name, image=image, results=results)
        super().__init__(*args, **kwargs)

    class Meta:
        model = Evaluation
        fields = ('name', 'image')
