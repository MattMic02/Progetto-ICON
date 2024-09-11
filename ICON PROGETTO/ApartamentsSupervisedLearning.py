import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV, RepeatedKFold, cross_val_score, learning_curve
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import os

def plot_learning_curves(model, X, y, model_name):
    train_sizes, train_scores, test_scores = learning_curve(model, X, y, cv=10, scoring='neg_mean_squared_error')

    # Calcola gli errori su addestramento e test
    train_errors = -train_scores
    test_errors = -test_scores

    # Calcola la deviazione standard e la varianza degli errori su addestramento e test
    train_errors_std = np.std(train_errors, axis=1)
    test_errors_std = np.std(test_errors, axis=1)
    train_errors_var = np.var(train_errors, axis=1)
    test_errors_var = np.var(test_errors, axis=1)

    # Stampa i valori numerici della deviazione standard e della varianza
    print(
        f"\033[95m{model_name} - Train Error Std: {train_errors_std[-1]}, Test Error Std: {test_errors_std[-1]}, Train Error Var: {train_errors_var[-1]}, Test Error Var: {test_errors_var[-1]}\033[0m")

    # Calcola gli errori medi su addestramento e test
    mean_train_errors = np.mean(train_errors, axis=1)
    mean_test_errors = np.mean(test_errors, axis=1)

    # Visualizza la curva di apprendimento
    plt.figure(figsize=(16, 10))
    plt.plot(train_sizes, mean_train_errors, label='Errore di training', color='green')
    plt.plot(train_sizes, mean_test_errors, label='Errore di testing', color='red')
    plt.title(f'Curva di apprendimento per {model_name}')
    plt.xlabel('Dimensione del training set')
    plt.ylabel('Errore Medio Quadratico (MSE)')
    plt.legend()
    plt.show()

def returnBestHyperparameters(dataset, target_column):
    X = dataset.drop(target_column, axis=1).to_numpy()
    y = dataset[target_column].to_numpy()
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, shuffle=True)
    
    ridge = Ridge()
    lasso = Lasso()
    rfr = RandomForestRegressor()
    """
    Ultimo esperimento
    RidgeHyperparameters = {
        'Ridge__alpha': [0.01, 0.1, 1, 10],
        'Ridge__solver': ['auto']
    }

    LassoHyperparameters = {
        'Lasso__alpha': [0.001, 0.01, 0.1, 1, 10, 100, 1000],
        'Lasso__max_iter': [500, 1000, 2000, 5000, 10000]
    }

    RandomForestHyperparameters = {
        'RandomForest__n_estimators': [100],
        'RandomForest__max_depth': [30, None],
        'RandomForest__min_samples_split': [2, 5, 10],
        'RandomForest__min_samples_leaf': [1, 2, 4],
    }
    """
    RidgeHyperparameters = {
        'model__alpha': [0.01, 0.1, 1, 10, 100, 1000],
        'model__solver': ['auto', 'svd', 'cholesky', 'saga', 'lsqr']
    }

    LassoHyperparameters = {
        'model__alpha': [0.001, 0.01, 0.1, 1, 10, 100, 1000],
        'model__max_iter': [500, 1000, 2000, 5000, 10000]
    }

    RandomForestHyperparameters = {
        'model__n_estimators': [50, 100, 200],
        'model__max_depth': [10, 20, 30, None],
        'model__min_samples_split': [2, 5, 10],
        'model__min_samples_leaf': [1, 2, 4],
        'model__bootstrap': [True, False]
    }
    cv = RepeatedKFold(n_splits=10, n_repeats=5, random_state=42)
    gridSearchCV_ridge = GridSearchCV(Pipeline([('scaler', StandardScaler()), ('model', ridge)]), RidgeHyperparameters, cv=cv, n_jobs=os.cpu_count(), verbose=3, scoring='neg_mean_squared_error')
    gridSearchCV_lasso = GridSearchCV(Pipeline([('scaler', StandardScaler()), ('model', lasso)]), LassoHyperparameters, cv=cv, n_jobs=os.cpu_count(), verbose=3, scoring='neg_mean_squared_error')
    gridSearchCV_rfr = GridSearchCV(Pipeline([('scaler', StandardScaler()), ('model', rfr)]), RandomForestHyperparameters, cv=cv, n_jobs=os.cpu_count(), verbose=3, scoring='neg_mean_squared_error')
    
    #gridSearchCV_ridge = GridSearchCV(Pipeline([('Ridge', ridge)]), RidgeHyperparameters, cv=cv, n_jobs=os.cpu_count(), verbose=3, scoring='neg_mean_squared_error')
    #gridSearchCV_lasso = GridSearchCV(Pipeline([('Lasso', lasso)]), LassoHyperparameters, cv=cv, n_jobs=os.cpu_count(), verbose=3, scoring='neg_mean_squared_error')
    #gridSearchCV_rfr = GridSearchCV(Pipeline([('RandomForest', rfr)]), RandomForestHyperparameters, cv=cv, n_jobs=os.cpu_count(), verbose=3, scoring='neg_mean_squared_error')

    gridSearchCV_ridge.fit(X_train, y_train)
    gridSearchCV_lasso.fit(X_train, y_train)
    gridSearchCV_rfr.fit(X_train, y_train)

    bestParameters = {
        'Ridge__alpha': gridSearchCV_ridge.best_params_['model__alpha'],
        'Ridge__solver': gridSearchCV_ridge.best_params_['model__solver'],
        'Lasso__alpha': gridSearchCV_lasso.best_params_['model__alpha'],
        'Lasso__max_iter': gridSearchCV_lasso.best_params_['model__max_iter'],
        'RandomForest__n_estimators': gridSearchCV_rfr.best_params_['model__n_estimators'],
        'RandomForest__max_depth': gridSearchCV_rfr.best_params_['model__max_depth'],
        'RandomForest__min_samples_split': gridSearchCV_rfr.best_params_['model__min_samples_split'],
        'RandomForest__min_samples_leaf': gridSearchCV_rfr.best_params_['model__min_samples_leaf'],
        'RandomForest__bootstrap': gridSearchCV_rfr.best_params_['model__bootstrap']
    }
    return bestParameters

def trainModelKFold(dataSet, target_column):
    model = {
        'RandomForest': {
            'mae_list': [],
            'mse_list': [],
            'r2_list': []
        },
        'Ridge': {
            'mae_list': [],
            'mse_list': [],
            'r2_list': []
        },
        'Lasso': {
            'mae_list': [],
            'mse_list': [],
            'r2_list': []
        }
    }

    bestParameters = returnBestHyperparameters(dataSet, target_column)
    print("\033[94m" + str(bestParameters) + "\033[0m")
    
    X = dataSet.drop(target_column, axis=1).to_numpy()
    y = dataSet[target_column].to_numpy()
    
    rfr = RandomForestRegressor(n_estimators=bestParameters['RandomForest__n_estimators'],
                                max_depth=bestParameters['RandomForest__max_depth'],
                                min_samples_split=bestParameters['RandomForest__min_samples_split'],
                                min_samples_leaf=bestParameters['RandomForest__min_samples_leaf'],
                                bootstrap=bestParameters['RandomForest__bootstrap'])
    
    ridge = Ridge(alpha=bestParameters['Ridge__alpha'],
                  solver=bestParameters['Ridge__solver'])
    
    lasso = Lasso(alpha=bestParameters['Lasso__alpha'],
                  max_iter=bestParameters['Lasso__max_iter'])

    cv = RepeatedKFold(n_splits=10, n_repeats=5, random_state=42)
    scoring_metrics = ['neg_mean_absolute_error', 'neg_mean_squared_error', 'r2']
    
    results_rfr = {}
    results_ridge = {}
    results_lasso = {}

    for metric in scoring_metrics:
        scores_rfr = cross_val_score(rfr, X, y, scoring=metric, cv=cv)
        scores_ridge = cross_val_score(ridge, X, y, scoring=metric, cv=cv)
        scores_lasso = cross_val_score(lasso, X, y, scoring=metric, cv=cv)
        
        results_rfr[metric] = -scores_rfr if metric != 'r2' else scores_rfr
        results_ridge[metric] = -scores_ridge if metric != 'r2' else scores_ridge
        results_lasso[metric] = -scores_lasso if metric != 'r2' else scores_lasso

    model['RandomForest']['mae_list'] = (results_rfr['neg_mean_absolute_error'])
    model['RandomForest']['mse_list'] = (results_rfr['neg_mean_squared_error'])
    model['RandomForest']['r2_list'] = (results_rfr['r2'])

    model['Ridge']['mae_list'] = (results_ridge['neg_mean_absolute_error'])
    model['Ridge']['mse_list'] = (results_ridge['neg_mean_squared_error'])
    model['Ridge']['r2_list'] = (results_ridge['r2'])

    model['Lasso']['mae_list'] = (results_lasso['neg_mean_absolute_error'])
    model['Lasso']['mse_list'] = (results_lasso['neg_mean_squared_error'])
    model['Lasso']['r2_list'] = (results_lasso['r2'])

    plot_learning_curves(rfr, X, y, 'RandomForest')
    plot_learning_curves(ridge, X, y, 'Ridge')
    plot_learning_curves(lasso, X, y, 'Lasso')

    visualizeMetricsGraphs(model)
    return model

def visualizeMetricsGraphs(model):
    models = list(model.keys())

    # Creazione di array numpy per ogni metrica
    mae = np.array([model[clf]['mae_list'] for clf in models])
    mse = np.array([model[clf]['mse_list'] for clf in models])
    r2 = np.array([model[clf]['r2_list'] for clf in models])

    # Controllo della forma degli array
    print("MAE shape:", mae.shape)
    print("MSE shape:", mse.shape)
    print("R2 shape:", r2.shape)

    # Assicurati che gli array abbiano la forma corretta
    if len(mae.shape) == 1:
        mae = mae[:, np.newaxis]
    if len(mse.shape) == 1:
        mse = mse[:, np.newaxis]
    if len(r2.shape) == 1:
        r2 = r2[:, np.newaxis]

    # Calcolo delle medie per ogni modello e metrica
    mean_mae = np.mean(mae, axis=1)
    mean_mse = np.mean(mse, axis=1)
    mean_r2 = np.mean(r2, axis=1)
    print("Mean MAE:", mean_mae)
    print("Mean MSE:", mean_mse)
    print("Mean R2:", mean_r2)

    bar_width = 0.2
    index = np.arange(len(models))

    # Grafico per il MAE
    plt.figure(figsize=(16, 5))
    for i in range(mae.shape[1]):
        plt.bar(index + i * bar_width, mae[:, i], bar_width, label=f'MAE Fold {i+1}')
    plt.plot(index + 0.5 * bar_width, mean_mae, color='red', marker='o', linestyle='-', label='MAE Medio')
    plt.xlabel('Modelli')
    plt.ylabel('Mean Absolute Error (MAE)')
    plt.title('Distribuzione del MAE per modello')
    plt.xticks(index + bar_width * (mae.shape[1] / 2), models)
    plt.legend()
    plt.show()

    # Grafico per il MSE
    plt.figure(figsize=(16, 5))
    for i in range(mse.shape[1]):
        plt.bar(index + i * bar_width, mse[:, i], bar_width, label=f'MSE Fold {i+1}')
    plt.plot(index + 0.5 * bar_width, mean_mse, color='red', marker='o', linestyle='-', label='MSE Medio')
    plt.xlabel('Modelli')
    plt.ylabel('Mean Squared Error (MSE)')
    plt.title('Distribuzione del MSE per modello')
    plt.xticks(index + bar_width * (mse.shape[1] / 2), models)
    plt.legend()
    plt.show()

    # Grafico per il R2
    plt.figure(figsize=(16, 5))
    for i in range(r2.shape[1]):
        plt.bar(index + i * bar_width, r2[:, i], bar_width, label=f'R2 Fold {i+1}')
    plt.plot(index + 0.5 * bar_width, mean_r2, color='red', marker='o', linestyle='-', label='R2 Medio')
    plt.xlabel('Modelli')
    plt.ylabel('R2 Score')
    plt.title('Distribuzione del R2 per modello')
    plt.xticks(index + bar_width * (r2.shape[1] / 2), models)
    plt.legend()
    plt.show()

