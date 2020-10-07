""" UTgram URls """

from django.contrib import admin
from django.urls import path

# Static files config
from django.conf import settings
from django.conf.urls.static import static

from posts import views as posts_views
from users import views as users_views


urlpatterns = [

    # Django
    path('admin/', admin.site.urls),

    # Posts views
    path('posts/feed/', posts_views.list_post, name='feed'),

    # Users views
    path('accounts/login/', users_views.login_view, name='login' ),
    path('accounts/logout/', users_views.logout_view, name='logout'),
    path('accounts/signup/', users_views.signup, name='signup'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
