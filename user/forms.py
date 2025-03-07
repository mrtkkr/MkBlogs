from django import forms

class LoginForm(forms.Form):
    username=forms.CharField(label="Kullanıcı Adı:",widget=forms.TextInput(attrs={"class": "form-control"}))
    password=forms.CharField(label="Şifre:",widget=forms.PasswordInput(attrs={"class": "form-control"}))

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, label="Kullanıcı Adı:",widget=forms.TextInput(attrs={"class": "form-control"}))
    #attrs => attiributes , ekstra özellikler verir html etiketine

    email = forms.EmailField(max_length=100, label="E-posta:",widget=forms.EmailInput(attrs={"class": "form-control"}))

    password = forms.CharField(max_length=20, label="Şifre:",widget=forms.PasswordInput(attrs={"class": "form-control"}))

    confirm = forms.CharField(max_length=20, label="Şifreyi Onayla:",widget=forms.PasswordInput(attrs={"class": "form-control"}))

    def clean(self):
        username= self.cleaned_data.get("username")
        email =self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Şifreler eşleşmiyor!")
        
        values ={
            "username": username,
            "email": email,
            "password": password
        }
        return values

