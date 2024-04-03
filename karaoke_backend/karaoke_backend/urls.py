from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("health/", views.Health.as_view(), name="status_check"),
    path("training/", views.TrainModel.as_view(), name="model_training"),
    path("prediction/", views.Predict.as_view(), name="model_prediction"),
]
