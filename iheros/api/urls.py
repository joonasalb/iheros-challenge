from django.urls import include, path
from rest_framework.routers import DefaultRouter
from iheros.api import views


router = DefaultRouter()
router.register(r"user", views.UserViewSet)
router.register(r"profile", views.ProfileViewSet)
router.register(r"hero", views.HeroViewSet)
router.register(r"threat", views.ThreatViewSet)
router.register(r"assignment", views.AssignmentThreatViewSet)

urlpatterns = [
    path("", include(router.urls), name="api")
]
