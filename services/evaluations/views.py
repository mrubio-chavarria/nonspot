from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Evaluation
from .serializers import EvaluationSerializer


class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
    permission_classes = (IsAuthenticated,)

    # Methods
    @action(detail=False, methods=['GET', 'POST'], permission_classes=(IsAuthenticated,))
    def new_analysis_view(self, request):
        """
        DESCRIPTION:
        View to render the home page.
        """
        if request.method == 'POST':
            pass
        return render(request, 'new_analysis.html')

