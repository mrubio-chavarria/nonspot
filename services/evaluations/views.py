from django.shortcuts import render, redirect
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Evaluation
from .serializers import EvaluationSerializer
from .forms import EvaluationForm


class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

    # Methods
    @action(detail=False, methods=['GET', 'POST'], permission_classes=(IsAuthenticated,))
    def new_analysis_view(self, request):
        """
        DESCRIPTION:
        View to render the new analysis page.
        """
        if request.method == 'POST':
            form = EvaluationForm(request.data)
            if form.is_valid():
                exam = form.save()
                exam.user = request.user
                exam.save()
                return redirect('/evaluations/my_analysis_view')
        else:
            form = EvaluationForm()
        return render(request, 'new_analysis.html', {'form': form})

    @action(detail=False, methods=['GET', 'POST'], permission_classes=(IsAuthenticated,))
    def my_analysis_view(self, request):
        """
        DESCRIPTION:
        View to render my analysis page.
        """
        evaluations = Evaluation.objects.filter(user=request.user)
        return render(request, 'my_analysis.html', {'evaluations': evaluations})

