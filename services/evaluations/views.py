from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Evaluation
from .serializers import EvaluationSerializer


class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
    permission_classes = (IsAuthenticated,)


