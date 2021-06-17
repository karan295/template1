"""project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from app1 import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()


router.register('student_viewset',views.student_viewset,basename='student__viewset')
router.register('student_viewset/<int:pk>/',views.student_viewset,basename='student__viewset')


router.register('student_model_viewset',views.student_model_viewset,basename='stu_model_viewset')

router.register('student_readonly_modelviewset',views.student_readonly_modelviewset,basename='stu_readonlymodelviewset')



urlpatterns = [
    path('admin/', admin.site.urls),
   
    path('student/',views.student_view),
    #path('student/<int:pk>/',views.student_view),
    
    path('student_api_view/',views.student_api_view.as_view()),
    path('student_api_view/<int:id>/',views.student_api_view.as_view()),

    path('',include(router.urls)),
    
    path('auth/',include('rest_framework.urls',namespace='rest_framework'))
    #upper for login and logout for user in session authentication 
]









