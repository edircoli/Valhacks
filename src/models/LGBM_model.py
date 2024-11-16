from lightgbm import LGBMClassifier, LGBMRegressor

def lgbm_model(X_train, y_train, X_test, y_test, feature_names, regression=True):
    y_train=y_train.values.ravel()
    if regression:
        model = LGBMRegressor(boosting_type='goss', objective='regression', max_depth=5, num_leaves=21, learning_rate=0.1, feature_fraction=0.7)
        metric='rmse'
    else:
        model = LGBMClassifier(boosting_type='goss', objective='binary', max_depth=5, num_leaves=21, learning_rate=0.1, feature_fraction=0.7)
        metric='binary_logloss'

    # Train LGBM model
    model.fit(X_train, y_train)

    # Use `predict_proba` for predicting probabilities
    if not regression:
        # For binary classification problem, it gives the probabilities for the positive class
        y_pred = model.predict_proba(X_test)[:, 1]
    else:
        y_pred = model.predict(X_test)

    # Get feature importances
    importances = model.feature_importances_

    # Pair each feature name with its importance
    feature_importances = list(zip(feature_names, importances))

    # Sort features by importance
    feature_importances.sort(key=lambda x: x[1], reverse=True)

    return y_pred, feature_importances,model