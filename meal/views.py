from django.shortcuts import render, redirect, get_object_or_404
from .models import Meal
from .forms import MealForm, RegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.db.models import Sum

def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("meal_list")
    
    return render(request, "register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, "Giriş başarılı.")
            
            return redirect("meal_list")
        else:
            messages.error(request, "Kullanıcı adı veya şifre hatalı.")
    return render(request, "login.html")

def meal_list(request):
    query = request.GET.get("q")
    ogun = request.GET.get("ogun")
    meals = Meal.objects.all().order_by("-created_at")

    if query:
        meals = meals.filter(ad__icontains = query)
    
    if ogun:
        meals = meals.filter(ogun = ogun)
    
    toplam_kalori = meals.aggregate(Sum("kalori"))["kalori__sum"] or 0
    toplam_protein = meals.aggregate(Sum("protein"))["protein__sum"] or 0
    toplam_karbonhidrat = meals.aggregate(Sum("karbonhidrat"))["karbonhidrat__sum"] or 0
    toplam_yag = meals.aggregate(Sum("yag"))["yag__sum"] or 0
    gunluk_hedef = 2000
    kalan_kalori = gunluk_hedef - toplam_kalori
    hedef_asildi = kalan_kalori < 0
    toplam_ogun = meals.count()

    return render(request, "meal_list.html", {
        "meals": meals,
        "query": query,
        "ogun": ogun,
        "toplam_kalori": toplam_kalori,
        "toplam_ogun": toplam_ogun,
        "gunluk_hedef": gunluk_hedef,
        "kalan_kalori": kalan_kalori,
        "hedef_asildi": hedef_asildi,
        "toplam_protein": toplam_protein,
        "toplam_karbonhidrat": toplam_karbonhidrat,
        "toplam_yag": toplam_yag,
    })

def meal_detail(request, id):
    meal = get_object_or_404(Meal, id = id)
    
    return render(request, "meal_detail.html", {"meal": meal})

def meal_create(request): 
    form = MealForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, "Yiyecek başarıyla eklendi.")
        return redirect("meal_list")
    
    return render(request, "meal_create.html", {"form": form})

def meal_update(request, id):
    meal = get_object_or_404(Meal, id = id)
    form = MealForm(request.POST or None, instance=meal)

    if form.is_valid():
        form.save()
        messages.success(request, f"{meal.ad} İsimli bilgi başarıyla güncellendi.")
        return redirect("meal_list")
    
    return render(request, "meal_update.html", {
        "form": form,
        "meal": meal,})

def meal_delete(request, id):
    meal = get_object_or_404(Meal, id = id)

    if request.method == "POST":
        meal.delete()
        messages.success(request, f"{meal.ad} başarıyla silindi.")
        return redirect("meal_list")
    
    return render(request, "meal_delete.html", {"meal": meal})