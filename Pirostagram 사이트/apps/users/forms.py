from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignupForm(UserCreationForm):
    username = forms.CharField(
        label='아이디',
        widget=forms.TextInput( #widget은 폼 필드의 렌더링 방식을 지정함 => 폼 필드의 외관과 상호작용 방식을 지정할 수 있음 
            attrs={ #attrs 매개변수를 사용하여 css 클래스를 지정
                'class' : 'signup_input'
            }
        )
    )
    email = forms.CharField(
        label='이메일',
        widget=forms.TextInput(
            attrs={
                'class' : 'signup_input'
            }
        )
    )
    password1 = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
                'class' : 'signup_input'
            }
        )
    )
    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput(
            attrs={
                'class' : 'signup_input'
            }
        )
    )
    name = forms.CharField(
        label='이름',
        widget=forms.TextInput(
            attrs={
                'class' : 'signup_input'
            }
        )
    )
    nickname = forms.CharField(
        label='닉네임',
        widget=forms.TextInput(
            attrs={
                'class' : 'signup_input'
            }
        )
    )
    gender = forms.ChoiceField(
        label='성별',
        choices=[('','---------')] + User.GENDER_CHOICE,
        widget=forms.Select(
            attrs={
                'class' : 'signup_input'
            }
        )
    )
    birth = forms.CharField(
        label='생일',
        widget=forms.TextInput(
            attrs={
                'class' : 'signup_input'
            }
        )
    )
    class Meta:
        model = User
        fields = ['username','email','password1','password2','name','nickname','gender','birth']