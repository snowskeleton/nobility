from django import forms
from hello.models import Part, Ticket
from hello.longLists import parts, devices
from hello.utils import fetchPartsFor

class TicketCreateForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('serial', 'model', 'assetTag', 'customer',)

class PartCreateForm(forms.ModelForm):
    class Meta:
        model = Part
        fields = ('cost', 'replaced', 'mpn')

class ChangePartsOnTicketForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs) #calls standard init
        print(args)
        lib = fetchPartsFor(args)
        # some = fetchPartsFor('Dell 3100 (Touch, +USB)')
        self.fields['parts'] = forms.ChoiceField(
        choices=lib)

    # class Meta:
        # model = 
    # class Meta:
    deviceModel = "generic"
    parts = fetchPartsFor(deviceModel)
    fields = (
        'part',
        "model",
        )

# class PartAddForm(forms.Form):
#     class Meta:
#         model = Part
#         fields = (
#             'model',
#             'part',
#             )

#     def __init__(self, *args, **kwargs):
#         super(PartAddForm, self).__init__(*args, **kwargs)        
#         self.fields['model'] = forms.ChoiceField(choices=[devices])
#         self.fields['part'].queryset = parts(pk=1)


class SearchForm(forms.Form):
    q = forms.CharField(label='Search', max_length=127)