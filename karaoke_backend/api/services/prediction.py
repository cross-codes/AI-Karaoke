from os import getcwd, sep, path
from json import loads
from joblib import load
from numpy import array
from rest_framework import status

from api.services.metadata import gen_metadata
from api.services.training import Training

base_path = getcwd()
data_path = path.normpath(base_path + sep + "data")
pickle_path = path.normpath(base_path + sep + "pickle")
log_path = path.normpath(base_path + sep + "log")

X, label_encoders, _, df = gen_metadata()


class Prediction:
    def predict(self, request):
        return_dict = {}
        in_request = request.body
        in_request_dict = loads(in_request.decode("utf8").replace("'", '"'))
        in_request_arr = in_request_dict.get("data", [])
        modded_arr = [in_request_arr]
        pickle_file = path.normpath(pickle_path + sep + "knn_model.joblib")
        knn_model = load(pickle_file)
        for index in range(len(modded_arr[0])):
            modded_arr[0][index] = label_encoders[index].transform(
                [modded_arr[0][index]]
            )[0]
        response_arr = []
        modded_arr_encoded = array(modded_arr)
        _, indices = knn_model.kneighbors(modded_arr_encoded)
        try:
            _, _, arr = Training.split(_, X, df["Songs"].to_numpy())
            for idx in indices[0]:
                response_arr.append(arr[idx])

            in_request_dict["prediction"] = response_arr
            return_dict["response"] = in_request_dict
            return_dict["status"] = status.HTTP_200_OK
            return return_dict
        except Exception as e:
            in_request_dict["error"] = str(e)
            return_dict["response"] = in_request_dict
            return_dict["status"] = status.HTTP_500_INTERNAL_SERVER_ERROR
            return return_dict
