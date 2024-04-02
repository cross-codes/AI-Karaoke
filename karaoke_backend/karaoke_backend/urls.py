from django.contrib import admin
from django.urls import path
from API import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("training/", views.TrainModel.as_view(), name="model_training"),
    path("prediction/", views.Predict.as_view(), name="model_prediction"),
]
