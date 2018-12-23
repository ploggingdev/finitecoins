from django.contrib import admin
from .models import Game, StaticResource
from .forms import AdminGameForm, AdminStaticResourceForm
from reversion.admin import VersionAdmin

@admin.register(Game)
class GameAdmin(VersionAdmin):
    form = AdminGameForm
    list_display = ('name', 'user', 'public', 'deleted','created')

@admin.register(StaticResource)
class StaticResourceAdmin(VersionAdmin):
    form = AdminStaticResourceForm
    list_display = ('url', 'game', 'deleted','created')