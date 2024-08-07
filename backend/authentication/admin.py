from django.contrib import admin
from .models import User
from .forms import CustomUserChangeForm, CustomUserCreationForm

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    fieldsets = (  
        (None, {'fields': ('username', 'password')}),  
        ('Permissions', {'fields': ('is_staff', 'is_active', 'role', 'is_deleted',)}),  
        ('User Settings', {'fields': ('created_by', 'modified_by', 'phone',)}),  
    )  
    add_fieldsets = (  
        (None, {  
            'classes': ('wide',),  
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active','role','phone','verified', 'created_by')}  
        ),  
    )  

    list_display = ('id', 'username', 'role', 'created_by', 'created_at')
    list_filter = ('created_by', 'role')
    search_fields = ('username',)
    list_per_page=500