from django.contrib import admin

# Import modals
from collection.models import Thing

# Setup automatic slug creation
class ThingAdmin(admin.ModelAdmin):
    model = Thing
    list_display = ('name', 'description',)
    prepopulated_fields = { 'slug': ('name',)}

# Register your models here.
admin.site.register(Thing, ThingAdmin)