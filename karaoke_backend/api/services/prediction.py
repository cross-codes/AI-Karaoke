from os import getcwd, sep, path
from json import loads
from joblib import load
from rest_framework import status

from api.services.metadata import gen_metadata

base_path = getcwd()
data_path = path.normpath(base_path + sep + "data")
pickle_path = path.normpath(base_path + sep + "pickle")
log_path = path.normpath(base_path + sep + "log")

X, label_encoders, _, _ = gen_metadata()


class Prediction:
    def predict(self, request):
        return_dict = {}
        in_request = request.body
        in_request_dict = loads(in_request.decode("utf8").replace("'", '"'))
        in_request_arr = in_request_dict.get("data", [])
        modded_arr = [in_request_arr]
        pickle_file = path.normpath(pickle_path + sep + "knn_model.joblib")
        try:
            knn_model = load(pickle_file)
            for idx in range(len(modded_arr[0])):
                modded_arr[0][idx] = label_encoders[idx].transform(
                    [modded_arr[0][idx]]
                )[0]
            in_request_dict["prediction"] = knn_model.predict(modded_arr)[0]
            return_dict["response"] = in_request_dict
            return_dict["status"] = status.HTTP_200_OK
            return return_dict
        except Exception as e:
            in_request_dict["error"] = str(e)
            return_dict["response"] = in_request_dict
            return_dict["status"] = status.HTTP_500_INTERNAL_SERVER_ERROR
            return return_dict
