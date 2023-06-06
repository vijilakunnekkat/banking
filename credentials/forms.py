# import self as self
# from django import forms
# from .models import Final, Branch
#
# class PersonForm(forms.ModelForm):
#     class Meta:
#         model = Final
#         fields = ('name', 'dob', 'age', 'gender','phone','email','address','district','branch','account','materials')
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['branch'].queryset = Branch.objects.none()
#
#     # if 'district' in self.data:
#     #     try:
#     #         district_id = int(self.data.get('district'))
#     #         self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id).order_by('name')
#     #     except (ValueError, TypeError):
#     #         pass  # invalid input from the client; ignore and fallback to empty City queryset
#     # elif self.instance.pk:
#     #     self.fields['branch'].queryset = self.instance.district.branch_set.order_by('name')
