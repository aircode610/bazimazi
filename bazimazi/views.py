from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, reverse
from django.core.mail import send_mail

from .models import User, Ad, Type, Category, State

import random
import json

# Create your views here.

def index(request):
    if request.session["logged_in"] == True:
        l = "true"
    else:
        l = "false"

    context = {
        "ads" : Ad.objects.all(),
        "types" : Type.objects.all(),
        "categories" : Category.objects.all(),
        "states" : State.objects.all(),
        "logged_in" : l
    }

    return render(request, "bazimazi/index.html", context)

def myads(request):

    try:
        if request.session["logged_in"] == True:

            email = request.session["user_info"]["email"]
            user_ads = []

            for ad in Ad.objects.all() :
                if ad.publisher.email == email:
                    user_ads.append(ad)

            context = {
                "logged_in" : True,
                "user_ads" : user_ads,
                "states" : State.objects.all()
            }
            return render(request, "bazimazi/my-ads.html", context)
        else:
            context = {
                "logged_in" : False,
                "states" : State.objects.all()
            }
            return render(request, "bazimazi/my-ads.html", context)
    except:
        context = {
            "logged_in" : False,
            "states" : State.objects.all()
        }
        return render(request, "bazimazi/my-ads.html", context)

def signin(request):
    context = {
        "users" : User.objects.all()
    }

    return render(request, "bazimazi/signin.html", context)

def verify(request):
    email = request.POST["email"]
    code = random.randint(1000, 9999)
    content = f"Your code: {code}"

    name = request.POST["name"]
    lastname = request.POST["lastname"]

    request.session["user_info"] = { "name" : name, "lastname" : lastname, "email" : email }

    send_mail(
        'Email verification',
        content,
        'aircode610@gmail.com',
        [email],
        fail_silently=False
    )

    context = {
        "code" : code
    }

    return render(request, "bazimazi/verify.html", context)

def verify_login(request):
    email = request.POST["email"]
    code = random.randint(1000, 9999)
    content = f"Your code: {code}"

    send_mail(
        'Email verification',
        content,
        'aircode610@gmail.com',
        [email],
        fail_silently=False
    )

    context = {
        "code" : code,
        "email" : email
    }

    return render(request, "bazimazi/login_verify.html", context)

def add_user(request):
    info = request.session["user_info"]

    new_user = User(name=info["name"], lastname=info["lastname"], email=info["email"])
    new_user.save()

    request.session["logged_in"] = True
    request.session["email"] = info["email"]

    return HttpResponseRedirect(reverse("index"))

def login(request):
    context = {
        "users" : User.objects.all()
    }

    return render(request, "bazimazi/login.html", context)

def login_user(request):
    request.session["logged_in"] = True
    email = request.POST.get("email")

    users =  User.objects.all()

    for user in users:
        if user.email == email:

            request.session["user_info"] = { "name" : user.name, "lastname" : user.lastname
            , "email" : user.email }

            request.session["email"] = user.email

            break

    return HttpResponseRedirect(reverse("index"))

def publish_ad(request):
    context = {
        "categories" : Category.objects.all(),
        "states" : State.objects.all(),
    }

    return render(request, "bazimazi/publish-ad.html", context)

def publish(request, category):
    context = {
        "category" : category,
        "types" : Type.objects.all(),
        "states" : State.objects.all(),
    }

    return render(request, "bazimazi/publish.html", context)

def publish_db(request):
    state = request.POST["state"]
    image = request.FILES.get("image")
    type = request.POST["type"]
    phone_number = request.POST.get("phone_number")
    price = request.POST["price"]
    title = request.POST["title"]
    description = request.POST["description"]

    users = User.objects.all()
    categories = Category.objects.all()
    states = State.objects.all()
    types = Type.objects.all()

    for user in users:
        if user.email == request.session["user_info"]["email"]:

            publisher = user

    for category in categories:
        if category.name == request.POST["category"]:

            category_db = category

    for state in states:
        if state.name == request.POST["state"]:

            state_db = state

    for type in types:
        if type.name == request.POST["type"]:

            type_db = type

    new_ad = Ad(publisher=publisher, category=category_db, state=state_db, image=image, type=type_db,
    phone_number=phone_number, price=price, title=title, description=description)
    new_ad.save()

    return HttpResponseRedirect(reverse("index"))

def ad(request, title):
    ad_title = title

    ads =  Ad.objects.all()

    for ad in ads:
        if ad.title == ad_title:
            ad_db = ad

    context = {
        "ad" : ad_db,
        "states" : State.objects.all()
    }

    return render(request, "bazimazi/ad.html", context)

def search_ad(request):
    keyword = request.POST["keyword"].lower()

    ads =  Ad.objects.all()
    filters = []

    for ad in ads:
        if keyword in ad.title.lower() :
            if ad.image:
                filters.append({"title" : ad.title, "price" : float(ad.price),
                 "image" : ad.image.url, "url" : "ad/" + str(ad.title) + ""})
            else:
                filters.append({"title" : ad.title, "price" : float(ad.price),
                 "image" : "None", "url" : "ad/" + str(ad.title) + ""})

    response_data = {}
    response_data['result'] = filters

    return HttpResponse(json.dumps(response_data), content_type="application/json")

def history(request):
    ads = Ad.objects.all()
    result = []

    for ad in ads:
        if ad.image:
            result.append({"title" : ad.title, "price" : float(ad.price),
             "image" : ad.image.url, "url" : "ad/" + str(ad.title) + ""})
        else:
            result.append({"title" : ad.title, "price" : float(ad.price),
             "image" : "None", "url" : "ad/" + str(ad.title) + ""})

    if request.session["logged_in"] == True:
        l = "true"
    else:
        l = "false"

    context = {
        "states" : State.objects.all(),
        "ads" : json.dumps(result),
        "logged_in" : l
    }

    return render(request, "bazimazi/history.html", context)

def save(request, title):
    ads =  Ad.objects.all()
    users =  User.objects.all()


    for ad in ads:
        if ad.title == title :
            for user in users:
                if user.email == request.session["email"]:
                    ad.saved_ads.add(user)
                    break
            the_ad = ad
            break

    context = {
        "ad" : the_ad
    }

    return render(request, "bazimazi/ad.html", context)

def saved_ads(request):
    ads =  Ad.objects.all()
    saved_ads = []

    for ad in ads:
        for user in ad.saved_ads.all():
            if request.session["email"] == user.email:
                saved_ads.append(ad)

    context = {
        "saved_ads" : saved_ads,
        "logged_in" : request.session["logged_in"]
    }

    return render(request, "bazimazi/saved-ads.html", context)

def region(request):
    ads = Ad.objects.all()
    city = request.POST.get("city")

    filters = []

    for ad in ads:
        if ad.state.name == city:
            if ad.image:
                filters.append({"title" : ad.title, "price" : float(ad.price),
                 "image" : ad.image.url, "url" : "ad/" + str(ad.title) + ""})
            else:
                filters.append({"title" : ad.title, "price" : float(ad.price),
                 "image" : "None", "url" : "ad/" + str(ad.title) + ""})

    response_data = {}
    response_data['result'] = filters

    return HttpResponse(json.dumps(response_data), content_type="application/json")

def category(request):
    ads =  Ad.objects.all()
    category = request.POST.get("category")

    filters = []

    for ad in ads:
        if ad.category.name == category:
            if ad.image:
                filters.append({"title" : ad.title, "price" : float(ad.price),
                 "image" : ad.image.url, "url" : "ad/" + str(ad.title) + ""})
            else:
                filters.append({"title" : ad.title, "price" : float(ad.price),
                 "image" : "None", "url" : "ad/" + str(ad.title) + ""})

    response_data = {}
    response_data['result'] = filters

    return HttpResponse(json.dumps(response_data), content_type="application/json")

def price(request):
    all_ads =  Ad.objects.all()
    ads = []
    the_ads = json.loads(request.POST.get("ads"))
    f = request.POST.get("from")
    t = request.POST.get("to")

    filters = []

    for ad in all_ads:
        if ad.title in the_ads:
            ads.append(ad)

    for ad in ads:
        if ad.price >= float(f) and ad.price <= float(t):
            if ad.image:
                filters.append({"title" : ad.title, "price" : float(ad.price),
                 "image" : ad.image.url, "url" : "ad/" + str(ad.title) + ""})
            else:
                filters.append({"title" : ad.title, "price" : float(ad.price),
                 "image" : "None", "url" : "ad/" + str(ad.title) + ""})

    response_data = {}
    response_data['result'] = filters

    return HttpResponse(json.dumps(response_data), content_type="application/json")

def image(request):
    all_ads =  Ad.objects.all()
    ads = []
    the_ads = json.loads(request.POST.get("ads"))

    filters = []

    for ad in all_ads:
        if ad.title in the_ads:
            ads.append(ad)

    for ad in ads:
        if ad.image:
            filters.append({"title" : ad.title, "price" : float(ad.price),
             "image" : ad.image.url, "url" : "ad/" + str(ad.title) + ""})

    response_data = {}
    response_data['result'] = filters

    return HttpResponse(json.dumps(response_data), content_type="application/json")

def image_rev(request):
    all_ads =  Ad.objects.all()
    the_ads = json.loads(request.POST.get("ads"))

    filters = []

    for ad in all_ads:
        if ad.title in the_ads:
            if ad.image:
                filters.append({"title" : ad.title, "price" : float(ad.price),
                 "image" : ad.image.url, "url" : "ad/" + str(ad.title) + ""})
            else:
                filters.append({"title" : ad.title, "price" : float(ad.price),
                 "image" : "None", "url" : "ad/" + str(ad.title) + ""})

    response_data = {}
    response_data['result'] = filters

    return HttpResponse(json.dumps(response_data), content_type="application/json")

def chat(request):
    context = {
        "states" : State.objects.all(),
    }

    return render(request, "bazimazi/chat.html", context)

def logout(request):
    request.session["logged_in"] = False

    return HttpResponseRedirect(reverse("index"))
