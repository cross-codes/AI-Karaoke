from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.services.prediction import Prediction
from api.services.training import Training


class TrainModel(APIView):
    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        self.add_cors_headers(response)
        return response

    def add_cors_headers(self, response):
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        response["Access-Control-Allow-Credentials"] = "true"
        response["Access-Control-Expose-Headers"] = "Content-Length, X-Content-Length"
        response["Access-Control-Max-Age"] = "3600"

    def get(self, request):
        train_obj = Training()
        response_dict = train_obj.train(request)
        response = response_dict["response"]
        status_value = response_dict["status"]
        return Response(response, status_value)


class Predict(APIView):
    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        self.add_cors_headers(response)
        return response

    def add_cors_headers(self, response):
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        response["Access-Control-Allow-Credentials"] = "true"
        response["Access-Control-Expose-Headers"] = "Content-Length, X-Content-Length"
        response["Access-Control-Max-Age"] = "3600"

    def post(self, request):
        pred_obj = Prediction()
        response_dict = pred_obj.predict(request)
        response = response_dict["response"]
        status_value = response_dict["status"]
        return Response(response, status_value)


class Health(APIView):
    def dispatch(self, *args, **kwargs):
        response = super().dispatch(*args, **kwargs)
        self.add_cors_headers(response)
        return response

    def add_cors_headers(self, response):
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
        response["Access-Control-Allow-Credentials"] = "true"
        response["Access-Control-Expose-Headers"] = "Content-Length, X-Content-Length"
        response["Access-Control-Max-Age"] = "3600"

    def get(self, _):
        response = {"message": "Server is active"}
        status_value = status.HTTP_200_OK
        return Response(response, status_value)
