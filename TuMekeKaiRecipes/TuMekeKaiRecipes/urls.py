from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', include('MyRecipes.urls')),
    path('register/', user_views.register, name ='user-register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name ='user-login'), 
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name ='user-logout'),
    path('profile/', user_views.profile, name = "user-profile"),
    path('profile/update/', user_views.update_profile, name='update_profile'),
    
    # Password reset URLs
    path('password_reset/', auth_views.PasswordResetView.as_view(), name = 'password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name = 'password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
