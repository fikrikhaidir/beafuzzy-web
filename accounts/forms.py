from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

User = get_user_model()
class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        # user_qs = User.objects.filter(username=username)
        # if user_qs.count()==1:
        #     user = user_qs.first()
        if username and password  :
            user = authenticate(username=username,password=password)
            if not user:
                raise forms.ValidationError("This user doesn't exist")
            elif not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")
            elif not user.is_active:
                raise forms.ValidationError("This user no longer active")
        return super(UserLoginForm,self).clean(*args,**kwargs)

class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Alamat Email')
    email2 = forms.EmailField(label='Konfirmasi Alamat Email')
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(label='Nama Depan (max: 15 Karakter)', max_length='15')
    last_name = forms.CharField(label='Nama Belakang (max: 20 Karakter)', max_length='20')
    class Meta:
        model= User
        fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'email2',
        'password',
]
    def clean_email2(self):
        print(self.cleaned_data)
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        print(email,email2)
        if email != email2:
            raise forms.ValidationError('Email yang dimasukkan harus sama')
        email_qs= User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError('email sudah digunakan')
        return email
