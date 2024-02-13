from django.contrib import admin
from django.urls import path
from logistic.views import TrackingDetailsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/tracking/<int:tracking_number>', TrackingDetailsView.as_view())
]
