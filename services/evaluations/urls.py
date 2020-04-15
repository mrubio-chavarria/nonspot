from django.conf.urls import url, include
from rest_framework import routers
from services.evaluations import views as evaluations

router = routers.SimpleRouter()
router.register('evaluations', evaluations.EvaluationViewSet, base_name='evaluations')

urlpatterns = [
    url(r'^', include(router.urls)),
]
