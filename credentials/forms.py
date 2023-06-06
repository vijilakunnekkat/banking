# from django import forms
# from .models import Final, Branch
#
# class PersonForm(forms.ModelForm):
#     class Meta:
#         model = Final
#         fields = ('name', 'date', 'age', 'gender','phone','email','address','district','branch','account','materials')
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['branch'].queryset = Branch.objects.none()
