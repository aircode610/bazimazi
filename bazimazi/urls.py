from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("myads", views.myads, name="myads"),
    path("verify", views.verify, name="verify"),
    path("signin", views.signin, name="signin"),
    path("add_user", views.add_user, name="add_user"),
    path("login", views.login, name="login"),
    path("verify_login", views.verify_login, name="verify_login"),
    path("login_user", views.login_user, name="login_user"),
    path("publish_ad", views.publish_ad, name="publish_ad"),
    path("publish/<str:category>", views.publish, name="publish"),
    path("publish_db", views.publish_db, name="publish_db"),
    path("ad/<str:title>", views.ad, name="ad"),
    path("search_ad", views.search_ad, name="search_ad"),
    path("history", views.history, name="history"),
    path("save/<str:title>", views.save, name="save"),
    path("saved_ads", views.saved_ads, name="saved_ads"),
    path("region", views.region, name="region"),
    path("category", views.category, name="category"),
    path("price", views.price, name="price"),
    path("image", views.image, name="image"),
    path("image_rev", views.image_rev, name="image_rev"),
    path("chat", views.chat, name="chat"),
    path("logout", views.logout, name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
