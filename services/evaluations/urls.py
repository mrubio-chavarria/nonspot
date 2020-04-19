from django.conf.urls import url, include
from rest_framework import routers
from services.evaluations import views as evaluations
from django.contrib import admin

router = routers.SimpleRouter()
router.register('evaluations', evaluations.EvaluationViewSet, base_name='evaluations')

urlpatterns = [
    url(r'^', include(router.urls)),
]

admin.site.site_header = 'Administración de nonSpot'
admin.site.site_title = 'Administración de nonSpot'

