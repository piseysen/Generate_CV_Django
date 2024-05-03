from django.contrib import admin
from .models import Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "summary", "degree", "school", "university", "previous_work", "skills"]
    search_fields = ["name", "email", "phone", "summary", "degree", "school", "university", "previous_work", "skills"]
admin.site.register(Profile, ProfileAdmin)

