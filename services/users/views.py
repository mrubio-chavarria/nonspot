from django.contrib.auth import login
from django.contrib.auth.views import logout
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from django.shortcuts import render, redirect
from .forms import UserCreationForm, AuthenticationForm
from services.evaluations.models import Evaluation
from ..evaluations.serializers import EvaluationSerializer
from nonspot.settings import STATIC_URL


class UserViewSet(viewsets.ModelViewSet):
    """
    DESCRIPTION:
    Class to gather all views in a suitable way.
    """

    # Attributes
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Methods
    @action(detail=False, methods=['GET'], permission_classes=(IsAuthenticated,))
    def home_view(self, request):
        """
        DESCRIPTION:
        View to render the home page.
        """
        return render(request, 'home.html')

    @action(detail=False, methods=['GET'], permission_classes=(IsAuthenticated,))
    def profile_view(self, request):
        """
        DESCRIPTION:
        View to render the personal profile page.
        """
        return render(request, 'profile.html', {'user': request.user})

    @action(detail=False, methods=['GET', 'POST'], permission_classes=(AllowAny, ))
    def login_view(self, request):
        """
        DESCRIPTION:
        View to render the login page and log the user in.
        """
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                return redirect('/users/home_view/')
        else:
            form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    @action(detail=False, methods=['POST'], permission_classes=(AllowAny,))
    def logout_view(self, request):
        """
        DESCRIPTION:
        View to render the logout page and log the user out.
        """
        logout(request)
        return redirect('/users/login_view/')

    @action(detail=False, methods=['GET', 'POST'], permission_classes=(AllowAny,))
    def signup_view(self, request):
        """
        DESCRIPTION:
        View to render the sign up page. And manage the sign up process.
        """
        if request.method == 'POST':
            form = UserCreationForm(data=request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('/users/login_view/')
        else:
            form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


