from django import forms
from django.core.validators import RegexValidator
from django.forms import ModelForm
from django.forms import ValidationError
from localflavor.br.validators import cpf_digits_re, dv_maker

from colaborativa.models import ExtraInfo


from localflavor.br.validators import BRCPFValidator, cpf_digits_re


class BRCPFValidator(RegexValidator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, regex=cpf_digits_re, message="O CPF informado é inválido.", **kwargs)

    def __call__(self, value):
        if not value.isdigit():
            cpf = cpf_digits_re.search(value)
            if cpf:
                value = "".join(cpf.groups())
            else:
                raise ValidationError(self.message, code="invalid")

        if len(value) != 11:
            raise ValidationError(self.message, code="max_digits")

        orig_dv = value[-2:]
        new_1dv = sum([i * int(value[idx]) for idx, i in enumerate(range(10, 1, -1))])
        new_1dv = dv_maker(new_1dv % 11)
        value = value[:-2] + str(new_1dv) + value[-1]
        new_2dv = sum([i * int(value[idx]) for idx, i in enumerate(range(11, 1, -1))])
        new_2dv = dv_maker(new_2dv % 11)
        value = value[:-1] + str(new_2dv)
        if value[-2:] != orig_dv:
            raise ValidationError(self.message, code="invalid")
        if value.count(value[0]) == 11:
            raise ValidationError(self.message, code="invalid")


class ExtraInfoForm(ModelForm):
    cpf = forms.CharField(
        label="CPF", help_text="Informe o seu CPF.", min_length=11, max_length=14, validators=[BRCPFValidator()]
    )
    # health_hands = forms.BooleanField(required=True, label="Participa ou participou do 'Saúde em Nossas Mãos'")

    # def __init__(self, *args, **kwargs):
    #     super(ExtraInfoForm, self).__init__(*args, **kwargs)
    #     self.fields["health_hands_where"].required = False

    def clean_cpf(self):
        data = self.cleaned_data['cpf']
        return data.replace(".", "").replace("-", "")

    class Meta:
        model = ExtraInfo
        fields = (
            "cpf",
            # "gender_1",
            # "profession",
            "occupation_area",
            "hospital_work",
            # "city_1",
            # "state_1",
            # "health_hands",
            "health_hands_where",
        )
