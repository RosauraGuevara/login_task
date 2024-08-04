from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include(('tasks.urls', 'tasks'), namespace='task')),
    path('accounts/', include('accounts.urls')),
]
