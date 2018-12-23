from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from mainapp.models import Game, StaticResource
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

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