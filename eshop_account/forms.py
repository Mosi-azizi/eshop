from  django import  forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'Please enter user name'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder':'Please enter your password'})
    )
    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        password = self.cleaned_data.get('password')
        is_exist_user=User.objects.filter(username=user_name).exists()
        if not is_exist_user:
            raise forms.ValidationError('Account not found')
        return user_name

class RegisterForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder':'please enter user name'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder':'please enter your email'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Please enter your password'})
    )
    re_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Please enter your password again'})
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        is_exits_user_by_email = User.objects.filter(email=email).exists()
        if is_exits_user_by_email:
            raise forms.ValidationError('Email is exists!')
        return email

    def clean_user_name(self):
        user_name = self.cleaned_data.get('user_name')
        is_exits_user_name = User.objects.filter(username=user_name).exists()
        if is_exits_user_name:
            raise forms.ValidationError('Account is exists')
        return user_name

    def clean_re_password(self):
        password = self.cleaned_data.get('password')
        re_password = self.cleaned_data.get('re_password')
        if password != re_password:
            raise forms.ValidationError('Passwords are not matched')
        return password


