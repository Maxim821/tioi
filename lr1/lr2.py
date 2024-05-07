import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Функция потерь (Mean Squared Error)
def J(theta, X, y):
    m = len(y)
    predictions = X.dot(theta)
    sq_error = np.square(predictions - y)
    loss = (1 / (2 * m)) * np.sum(sq_error)
    return loss

# Градиент функции потерь
def grad_J(theta, X, y):
    m = len(y)
    gradients = (1 / m) * X.T.dot(X.dot(theta) - y)
    return gradients

# Метод градиентного спуска
def gradient_descent(J, grad_J, X, y, initial_theta, learning_rate=0.01, num_iters=100):
    theta = initial_theta
    J_history = []

    for i in range(num_iters):
        gradients = grad_J(theta, X, y)
        theta = theta - learning_rate * gradients
        J_history.append(J(theta, X, y))

    return theta, J_history

# Генерируем случайные точки
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Добавляем столбец с единицами для коэффициента смещения
X_b = np.c_[np.ones((100, 1)), X]

# Точное матричное решение с помощью NumPy
theta_numpy = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)

# Решение с помощью scikit-learn
lin_reg = LinearRegression()
lin_reg.fit(X, y)
theta_sklearn = np.array([lin_reg.intercept_, lin_reg.coef_[0]]).reshape(-1, 1)

# Градиентный спуск с произвольной функцией потерь
initial_theta = np.random.randn(2, 1)
learning_rate = 0.1
num_iterations = 1000
theta_gradient_descent, J_history = gradient_descent(J, grad_J, X_b, y, initial_theta, learning_rate, num_iterations)

# График для точного матричного решения (NumPy)
plt.figure(figsize=(12, 8))
plt.scatter(X, y, color='blue', label='Точки')
plt.plot(X, X_b.dot(theta_numpy), color='red', label='Точное матричное решение (NumPy)')
plt.title('Линейная регрессия: точное матричное решение (NumPy)')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.savefig('exact_solution_numpy.png')


# График для решения с помощью scikit-learn
plt.figure(figsize=(12, 8))
plt.scatter(X, y, color='blue', label='Точки')
plt.plot(X, X_b.dot(theta_sklearn), color='green', label='Решение с помощью scikit-learn')
plt.title('Линейная регрессия: решение с помощью scikit-learn')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.savefig('solution_sklearn.png')


# График для градиентного спуска (NumPy)
plt.figure(figsize=(12, 8))
plt.scatter(X, y, color='blue', label='Точки')
plt.plot(X, X_b.dot(theta_gradient_descent), color='orange', label='Градиентный спуск (NumPy)')
plt.title('Линейная регрессия: градиентный спуск (NumPy)')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.savefig('gradient_descent_numpy.png')


