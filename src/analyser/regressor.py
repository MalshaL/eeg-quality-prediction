
from src.common import *
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


min_max_scaler = MinMaxScaler()


def lin_regression(dataset, score_filename):
    df, data_np = data_load.get_score_data(dataset, score_filename)
    data_scaled = min_max_scaler.fit_transform(data_np[:, 0:6])
    x_train, x_test, y_train, y_test = train_test_split(data_scaled[:, 0:5], data_scaled[:, 5],
                                                        test_size=0.20, random_state=27)
    reg_model = LinearRegression().fit(x_train, y_train)
    r_squared = reg_model.score(x_test, y_test)
    print("R squared = %f" % r_squared)
    y_pred = reg_model.predict(x_test)
    print(y_test)
    print(y_pred)
