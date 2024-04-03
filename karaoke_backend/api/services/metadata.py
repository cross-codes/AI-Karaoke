from os import sep, path, getcwd
from numpy import array
from pandas import read_csv
from sklearn.preprocessing import LabelEncoder


def gen_metadata():
    base_path = getcwd()
    data_path = path.normpath(base_path + sep + "data")

    train_data = path.normpath(data_path + sep + "knn_dataset.csv")
    df = read_csv(train_data)
    df = df.sample(frac=1)
    X = df[["Mood", "Energy", "Beats"]].to_numpy()
    label_encoders = [LabelEncoder() for _ in range(len(X[0]))]
    X = array(X)
    for i in range(len(X[0])):
        X[:, i] = label_encoders[i].fit_transform([x[i] for x in X])

    return X, label_encoders, train_data, df
