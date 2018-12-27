from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class NewUserForm(forms.Form):
    email = forms.CharField(label="e-mail",
                            max_length=30,
                            required=True
                            )
    user = forms.CharField(label="Usuario",
                           max_length=20,
                           required=True
                           )
    name = forms.CharField(label="Nombre",
                           max_length=25,
                           required=True
                           )
    token_s = forms.CharField(label="Token",
                              max_length=140,
                              required=True
                              )

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-newUserForm'
        self.helper.form_class = 'form-group'
        self.helper.form_method = 'post'
        self.helper.form_action = 'index'
        self.helper.add_input(Submit('submit', 'Enviar'))


class NewFeelingForm(forms.Form):
    happiness = forms.IntegerField(label="Felicidad",
                                   required=True
                                   )
    anger = forms.IntegerField(label="Enfado",
                               required=True
                               )
    neutral = forms.IntegerField(label="Neutro",
                                 required=True
                                 )
    sadness = forms.IntegerField(label="Tristeza",
                                 required=True
                                 )
    fear = forms.IntegerField(label="Temor",
                              required=True
                              )
    surprise = forms.IntegerField(label="Sorpresa",
                                  required=True
                                  )
    disgust = forms.IntegerField(label="Asco",
                                 required=True
                                 )

    def __init__(self, *args, **kwargs):
        super(NewFeelingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-newFeelingForm'
        self.helper.form_class = 'form-group'
        self.helper.form_method = 'post'
#        self.helper.form_action = 'user_detail'
        self.helper.add_input(Submit('submit', 'Enviar'))
