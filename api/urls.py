from home import views
from home.views import index, person, PersonAPI, PeopleViewSet, RegisterUser
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

router = DefaultRouter()
router.register(r'people', PeopleViewSet, basename='people')
urlpatterns = router.urls

urlpatterns = [
    # path('', include(router.urls)),
    # path('register/', views.RegisterAPI.as_view()),
    # path('login/', views.LoginAPI.as_view()),
    # path('index/', index),
    # path('person/', person),
    # path('persons/', PersonAPI.as_view()),
    path('registerapi/', RegisterUser.as_view()),
]