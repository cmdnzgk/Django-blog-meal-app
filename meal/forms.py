from django import forms
from .models import Meal

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ["ad", "kalori", "miktar", "aciklama", "ogun", "protein", "karbonhidrat", "yag"]
        labels = {
            "ad": "Yiyecek adı",
            "kalori": "Kalori",
            "miktar": "Miktar",
            "aciklama": "Açıklama",
            "ogun": "Öğün",
            "protein": "Protein",
            "karbonhidrat": "Karbonhidrat",
            "yag": "Yağ"
        }
        widgets = {
            "ad": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Yiyecek adı giriniz"
            }),
            "kalori": forms.NumberInput(attrs={
                "class": "form-input",
                "placeholder": "Kalori miktarını giriniz"
            }),
            "miktar": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Yiyecek miktarını giriniz"
            }),
            "aciklama": forms.Textarea(attrs={
                "class": "form-textarea",
                "placeholder": "Açıklama giriniz"
            }),
            "protein": forms.NumberInput(attrs={
                "class": "form-input",
                "placeholder": "Protein miktarı"
            }),
            "karbonhidrat": forms.NumberInput(attrs={
                "class": "form-input",
                "placeholder": "Karbonhidrat miktarı"
            }),
            "yag": forms.NumberInput(attrs={
                "class": "form-input",
                "placeholder": "Yağ miktarı"
            })
        }
        error_messages = {
            field: {"required": "Boş bırakılamaz."} for field in fields
        }
    
    def clean_ad(self):
        ad = self.cleaned_data.get("ad")

        if len(ad) <= 1:
            raise forms.ValidationError("1 karakterden fazla olmalı.")
        
        if not ad.replace(" ", "").isalpha():
            raise forms.ValidationError("Sadece harf girebilirsiniz.")
        
        return ad
    
    def clean_kalori(self):
        kalori = self.cleaned_data.get("kalori")

        if kalori < 0:
            raise forms.ValidationError("0'dan küçük giremezsiniz.")
        
        return kalori
    
    def clean_miktar(self):
        miktar = self.cleaned_data.get("miktar")

        if len(miktar) <= 1:
            raise forms.ValidationError("1 karakterden fazla olmalı.")
        
        return miktar
    
    def clean_protein(self):
        protein = self.cleaned_data.get("protein")

        if protein < 0:
            raise forms.ValidationError("0'dan küçük giremezsiniz.")
        
        return protein
    
    def clean_karbonhidrat(self):
        karbonhidrat = self.cleaned_data.get("karbonhidrat")

        if karbonhidrat < 0:
            raise forms.ValidationError("0'dan küçük giremezsiniz.")
        
        return karbonhidrat
    
    def clean_yag(self):
        yag = self.cleaned_data.get("yag")

        if yag < 0:
            raise forms.ValidationError("0'dan küçük giremezsiniz.")
        
        return yag