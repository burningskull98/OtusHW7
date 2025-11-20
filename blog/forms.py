"""
Этот модуль отвечает за определение форм для обработки пользовательского ввода
в приложении.
"""
from django import forms
from .models import User, Post


class PostForm(forms.Form):
    title = forms.CharField(
        max_length=100,
        label="Название",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Введите название"}
        ),
    )
    content = forms.CharField(
        label="Содержание",
        widget=forms.Textarea(
            attrs={"class": "form-control", "rows": 8, "placeholder": "Введите пост"}
        ),
    )

    user = forms.ModelChoiceField(
        queryset=User.objects.all(),
        label="Пользователь",
        empty_label="Выберите пользователя",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    def clean_title(self):
        title = self.cleaned_data["title"]
        if len(title) < 8:
            raise forms.ValidationError("Название должен быть не менее 8 символов")
        return title


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "user",
        ]
        labels = {
            "title": "Название",
            "content": "Содержание",
            "user": "Пользователи",
        }
        widgets = {
            "title": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Введите название"}
            ),
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 8,
                    "placeholder": "Введите пост",
                }
            ),
            "user": forms.Select(attrs={"class": "form-control"}),
        }
