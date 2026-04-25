from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["baslik", "icerik"]

        error_messages = {
            "baslik": {
                "required": "Başlık boş bırakılamaz"
            },
            "icerik": {
                "required": "İçerik boş bırakılamaz"
            }
        }
        widgets = {
            "baslik": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Başlık giriniz"
            }),
            "icerik": forms.Textarea(attrs={
                "class": "form-textarea",
                "placeholder": "İçerik giriniz"
            })
        }

    def clean_baslik(self):
        baslik = self.cleaned_data.get("baslik")

        if len(baslik) <= 3:
            raise forms.ValidationError("3 karakterden fazla olmalı")
        
        return baslik
    
    def clean_icerik(self):
        icerik = self.cleaned_data.get("icerik")

        if len(icerik) <= 10:
            raise forms.ValidationError("10 karakterden fazla olmalı")
        
        return icerik