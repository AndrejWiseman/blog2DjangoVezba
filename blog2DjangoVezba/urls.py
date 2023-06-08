from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    #poveyivanje sa blog url
    path('blog/', include('blog.urls', namespace='blog')),

]
