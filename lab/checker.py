import numpy as np

def check_1_1(mean_error, mean_squared_error, max_error, train_sets):
    train_set_1d, train_set_2d, train_set_10d = train_sets
    assert np.isclose(mean_error(train_set_1d, np.array([8])), 8.897352)
    assert np.isclose(mean_error(train_set_2d, np.array([2.5, 5.2])), 7.89366)
    assert np.isclose(mean_error(train_set_10d, np.array(np.arange(10))), 14.16922)

    assert np.isclose(mean_squared_error(train_set_1d, np.array([3])), 23.03568)
    assert np.isclose(mean_squared_error(train_set_2d, np.array([2.4, 8.9])), 124.9397)
    assert np.isclose(mean_squared_error(train_set_10d, -np.arange(10)), 519.1699)

    assert np.isclose(max_error(train_set_1d, np.array([3])), 7.89418)
    assert np.isclose(max_error(train_set_2d, np.array([2.4, 8.9])), 14.8628)
    assert np.isclose(max_error(train_set_10d, -np.linspace(0, 5, num=10)), 23.1727)

def check_1_2(minimize_me, minimize_mse, minimize_max, train_set_1d):
    assert np.isclose(minimize_mse(train_set_1d), -0.89735)
    assert np.isclose(minimize_mse(train_set_1d * 2), -1.79470584)
    assert np.isclose(minimize_me(train_set_1d), -1.62603)
    assert np.isclose(minimize_me(train_set_1d ** 2), 3.965143)
    assert np.isclose(minimize_max(train_set_1d), 0.0152038)
    assert np.isclose(minimize_max(train_set_1d / 2), 0.007601903895526174)

def check_1_3(me_grad, mse_grad, max_grad, train_sets):
    train_set_1d, train_set_2d, train_set_10d = train_sets
    assert all(np.isclose(
        me_grad(train_set_1d, np.array([0.99])),
        [0.46666667]
    ))
    assert all(np.isclose(
        me_grad(train_set_2d, np.array([0.99, 8.44])),
        [0.21458924, 0.89772834]
    ))
    assert all(np.isclose(
        me_grad(train_set_10d, np.linspace(0, 10, num=10)),
        [-0.14131273, -0.031631, 0.04742431, 0.0353542, 0.16364242, 0.23353252,
          0.30958123, 0.35552034, 0.4747464, 0.55116738]
    ))

    assert all(np.isclose(
        mse_grad(train_set_1d, np.array([1.24])),
        [4.27470585]
    ))
    assert all(np.isclose(
        mse_grad(train_set_2d, np.array([-8.44, 10.24])),
        [-14.25378235,  21.80373175]
    ))
    assert all(np.isclose(
        max_grad(train_set_1d, np.array([5.25])),
        [1.]
    ))
    assert all(np.isclose(
        max_grad(train_set_2d, np.array([-6.28, -4.45])),
        [-0.77818704, -0.62803259]
    ))
