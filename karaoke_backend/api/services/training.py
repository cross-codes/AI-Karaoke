from os import path, getcwd, sep
from joblib import dump
from rest_framework import status
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

import constants as knn_constants
from api.services.metadata import gen_metadata

base_path = getcwd()
data_path = path.normpath(base_path + sep + "data")
pickle_path = path.normpath(base_path + sep + "pickle")
log_path = path.normpath(base_path + sep + "log")


class Training:
    def split(self, X, y):
        X_train, X_test, y_train, _ = train_test_split(
            X,
            y,
            test_size=knn_constants.TEST_SIZE,
            random_state=knn_constants.RANDOM_STATE,
        )
        return X_train, X_test, y_train

    def train(self, _):
        return_dict = {}
        X, _, _, df = gen_metadata()

        y = df["Songs"].to_numpy()

        X_train, X_test, y_train = self.split(X, y)

        knn_model = KNeighborsClassifier(n_neighbors=knn_constants.N_NEIGHBOURS)
        knn_model.fit(X_train, y_train)
        try:
            _ = knn_model.predict(X_test)
            pickle_file = path.normpath(pickle_path + sep + "knn_model.joblib")
            with open(pickle_file, "wb") as fh:
                dump(knn_model, fh)

            return_dict["response"] = {"message": "Model Training complete"}
            return_dict["status"] = status.HTTP_200_OK
            return return_dict
        except Exception as e:
            return_dict["response"] = {"error": str(e)}
            return_dict["status"] = status.HTTP_500_INTERNAL_SERVER_ERROR
            return return_dict
