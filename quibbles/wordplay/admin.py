from django.contrib import admin

from .models import Quibble

# admin.site.register(Quibble)


@admin.register(Quibble)
class QuibbleAdmin(admin.ModelAdmin):

    def user_name(self, obj):
        return obj.user.username

    list_display = ('id', 'text', 'category', 'status', 'user_name', 'created', 'modified')
    list_editable = ('status',)
