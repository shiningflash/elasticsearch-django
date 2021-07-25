from django.contrib import admin
from django.urls import path, include
from user.views import PublisherDocumentView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', PublisherDocumentView.as_view({'get': 'list'})),
    path('student/', include('user.urls')),
]
