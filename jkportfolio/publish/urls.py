from django.urls import path
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('jk/',views.papers,name='publish.html'),
    path('',views.profile,name='index.html'),
    path('view/<pk>',views.detailed,name='view.html'),
    path('users',views.user_login,name='login.html'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)