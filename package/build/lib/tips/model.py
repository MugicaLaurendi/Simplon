from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_validate

def train_model_lr(X_train_scaled,y_train):
    lr_trained = LinearRegression()
    lr_trained.fit(X_train_scaled,y_train)
    return lr_trained


def scoring_lr(X_train_scaled,X_test_scaled,y_train,y_test):
    print("return lr_trained, score_cv, score_mean_cv, score_test ")
    lr_trained = train_model_lr(X_train_scaled,y_train)
    score_cv = cross_validate(lr_trained, X_train_scaled, y_train, cv=5)['test_score']
    score_mean_cv = score_cv.mean()
    score_test = lr_trained.score(X_test_scaled, y_test)
    return lr_trained, score_cv, score_mean_cv, score_test
