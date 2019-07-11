from django.contrib import admin

# Register your models here.

from web.models import  *

admin.site.register([home,News,about])