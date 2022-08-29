
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="ShopHome"),
    path('about/',views.about,name="AboutUs"),
    path('contactus/',views.contactus,name="ContactUs"),
    path('tracker/',views.tracker,name="Tracker"),
    path('search/',views.search,name="Search"),
    path('productview/',views.productview,name="ProductView"),
    path('checkout/',views.checkout,name="Checkout")
    
]