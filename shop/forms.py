from django import forms
from django.forms import widgets
from .models import Department,Role,Employee

class StudentDepartment(forms.ModelForm):
    class Meta:
        model = Department
        fields =['name','locations']
        # widgets = {
        #     'name': forms.TextInput(attrs={'class':'form-control'}),
        #     'email': forms.EmailInput(attrs={'class':'form-control'}),
        #     'dob': forms.DateInput(attrs={'class':'form-control'}),
        #     'age': forms.NumberInput(attrs={'class':'form-control'})
            

        # }
    
class StudentRole(forms.ModelForm):
    class Meta:
        model = Role
        fields =['name']



class StudentEmployee(forms.ModelForm):
    class Meta:
        model = Employee
        fields =['first_name','last_name','dept','salary','bonus','phone','role','hire_date']
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),

            'debt': forms.TextInput(attrs={'class':'form-control'}),
            'salary': forms.NumberInput(attrs={'class':'form-control'}),
            'bonus': forms.NumberInput(attrs={'class':'form-control'}),
            'phone': forms.NumberInput(attrs={'class':'form-control'}),
            #'role': forms.TextInput(attrs={'class':'form-control'}),
            'hire_date': forms.DateInput(attrs={'class':'form-control'})

        
            

         }