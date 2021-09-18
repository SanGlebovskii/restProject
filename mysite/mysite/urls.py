"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from hw_22.views import api_cars, api_car_detail
from hw_22_2.views import APIPets, APIPetDetail
from hw_22_3.views import APIComputers, APIComputerDetail
from hw_22_4.views import APIGuitarViewSet
# from less_22.views import api_products, api_product_detail
from less_22.views import APIProducts, APIProductDetail
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('guitars', APIGuitarViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', api_cars),
    path('cars/<int:pk>', api_car_detail),
    path('pets/', APIPets.as_view()),
    path('pets/<int:pk>', APIPetDetail.as_view()),
    path('computers/', APIComputers.as_view()),
    path('computers/<int:pk>', APIComputerDetail.as_view()),
    path('api/', include(router.urls)),
    path('products/', APIProducts.as_view()),
    path('products/<int:pk>', APIProductDetail.as_view())
]
