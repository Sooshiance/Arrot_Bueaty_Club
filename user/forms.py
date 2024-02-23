from django import forms 

from .models import User


class RegisterUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone', 'email', 'username', 'password', 'first_name', 'last_name']
        labels = {
            'password': 'گذر واژه',
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class':'form-control my-5', 'placeholder':'example1234@gmail.com'}),
            'phone': forms.NumberInput(attrs={'class':'form-control my-5', 'placeholder':'09123456789'}),
            'username': forms.TextInput(attrs={'class':'form-control my-5', 'placeholder':'Username'}),
            'password': forms.PasswordInput(attrs={'class':'form-control my-5', 'placeholder':'••••••••••••'}),
            'first_name': forms.TextInput(attrs={'class':'form-control my-5', 'placeholder':'Ali'}),
            'last_name': forms.TextInput(attrs={'class':'form-control my-5', 'placeholder':'Alizadeh'}),
        }


class OTPForm(forms.Form):
    otp = forms.CharField(label="OTP", max_length=6)


class Mail(forms.Form):
    title = forms.CharField(widget={})
    txt   = forms.CharField(widget={})


class UserUpdate(forms.Form):
    phone = forms.CharField(label="شماره تماس")
    email = forms.EmailField(label="پست الکترونیکی")
    username = forms.CharField(label="نام کاربری")
    first_name = forms.CharField(label="نام")
    last_name = forms.CharField(label="نام خانوادگی")
    
    def __init__(self, *args, **kwargs):
        super(UserUpdate, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control my-3'})
