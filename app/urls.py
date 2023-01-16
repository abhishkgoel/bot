from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # path('', views.index, name = 'index'),
    path("register", views.register, name="register"),
    path("", views.login_user, name="login_user"),
    path("login_user", views.login_user, name="login_user"),
    path("logout_user", views.logout_user, name="logout_user"),
    path("home", views.home, name="home"),
    path("model_form_upload", views.model_form_upload, name="model_form_upload"),
    path("upload_pdf", views.upload_pdf, name="upload_pdf"),
    path("main", views.main, name="main"),
    # path("",views.Import_Excel_pandas,name="Import_Excel_pandas"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
