from django.contrib import admin
from . import models

admin.site.register(models.FileHash)
admin.site.register(models.EventHashLog)
admin.site.register(models.User)
