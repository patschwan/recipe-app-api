from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# recommendation for translations
from django.utils.translation import gettext as _

from core import models


class UserAdmin(BaseUserAdmin):  # modify the default admin user
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        # section
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('name',)}),
        (
            _('Permissions'),
            {'fields': ('is_active', 'is_staff', 'is_superuser')}
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    # das ist für test_create_user_page ToDo Docs nachschauen
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )


admin.site.register(models.User, UserAdmin)
