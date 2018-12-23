from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.http import HttpResponse
from mainapp.models import Game, StaticResource
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
from mainapp.forms import CreateGameForm
from django.contrib import messages
from django.urls import reverse

class IndexView(View):
    
    def get(self, request):
        return HttpResponse("Hello, world.")

class AboutView(View):
    
    def get(self, request):
        return HttpResponse("About page.")

class DevGames(LoginRequiredMixin, View):

    login_url = settings.LOGIN_URL
    paginate_by = 10
    template_name = 'mainapp/dev_games.html'

    def get(self, request):
        all_results = Game.objects.filter(user=request.user).filter(deleted=False).order_by('-created')
        paginator = Paginator(all_results, self.paginate_by)
        page = request.GET.get('page')
        try:
            game_list = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            game_list = paginator.page(1)
            page = 1
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            game_list = paginator.page(paginator.num_pages)
            page = paginator.num_pages
        return render(request, self.template_name, { 'game_list' : game_list })

class CreateGame(LoginRequiredMixin, View):

    login_url = settings.LOGIN_URL
    form_class = CreateGameForm
    template_name = "mainapp/create_game.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form' : form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            game_name = form.cleaned_data['name']
            game_count = Game.objects.filter(name=game_name).count()
            if game_count == 0:
                game = Game(name=game_name, user=request.user)
                game.save()
                #todo : redirect to game upload page
                messages.success(request ,"Game has been created successfully")
                return redirect(reverse("mainapp:dev_games"))
            else:
                messages.error(request ,"Game name already exists")
                return redirect(reverse("mainapp:create_game"))
        else:
            messages.error(request, "Invalid form data. Only letters and numbers are allowed.")
            return render(request, self.template_name, {'form' : self.form_class()})