
from src.common import *
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report


min_max_scaler = MinMaxScaler()


def svc_classifier(dataset, score_filename):
    df, data_np = data_load.get_score_data(dataset, score_filename)
    data_scaled = min_max_scaler.fit_transform(data_np[:, 0:5])
    x_train, x_test, y_train, y_test = train_test_split(data_scaled[:, 0:5], data_np[:, 6],
                                                        test_size=0.10, random_state=27)
    params = [{'C': [1, 10, 100, 1000],
               'kernel': ['linear']},
              {'C': [1, 10, 100, 1000],
               'kernel': ['rbf'],
               'gamma': [1e-3, 'auto']}]
    clf = GridSearchCV(SVC(), params, cv=5, scoring='f1_macro')
    clf.fit(x_train, y_train)

    best_params = clf.best_params_
    print(best_params)
    print(clf.best_score_)
    y_true, y_pred = y_test, clf.predict(x_test)
    print(y_true)
    print(y_pred)
    print(classification_report(y_true, y_pred))

    cv_scores = cross_val_score(SVC(C=best_params['C'], kernel=best_params['kernel']),
                                data_scaled[:, 0:5], data_np[:, 6],
                                cv=10, scoring='f1_macro')
    print(cv_scores)
    print(cv_scores.mean())


def nb_classifier(dataset, score_filename):
    df, data_np = data_load.get_score_data(dataset, score_filename)
    data_scaled = min_max_scaler.fit_transform(data_np[:, 0:5])
    cv_scores = cross_val_score(GaussianNB(), data_scaled[:, 0:5], data_np[:, 6], cv=10, scoring='f1_macro')
    print(cv_scores)
    print(cv_scores.mean())
