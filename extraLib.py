import numpy as np
import cv2


def get_matrix(new_zero, new_x):
    # input type {List}

    STW = None  # STW = stage to wafer
    WTS = None  # WTS = wafer to stage

    vector_zero = np.array(new_zero).reshape((2, 1))  # save input as array type
    vector_x = np.array(new_x).reshape((2, 1))

    vector_t = vector_x - vector_zero  # move vector to zero

    norm = np.linalg.norm(vector_t)  # calculate the norm of vector

    # 90° anticlockwise rotation matrix
    R_matrix = np.array([[0, -1],
                         [1,  0]])

    vector_tx = 2670*(vector_t/norm)  # new unit X vector with unit 1µm
    vector_ty = R_matrix.dot(vector_tx)  # rotation to get unit Y vector

    # translation matrix for coordinate system
    T = np.array([[1, 0, -new_zero[0]],
                  [0, 1, -new_zero[1]],
                  [0, 0, 1]])

    # rotation matrix for coordinate system
    Mr = np.array([[vector_tx[0, 0], vector_ty[0, 0], 0],
                   [vector_tx[1, 0], vector_ty[1, 0], 0],
                   [0, 0, 1]])

    Mr_invs = np.linalg.inv(Mr)
    STW = Mr_invs.dot(T)
    WTS = np.linalg.inv(STW)

    return STW, WTS  # output type {ndarray}


def get_new_pos(matrix, point):
    # input type:
    # matrix {ndarray}, point {list}

    r = np.zeros([3, 1])

    # make the point into homogeneous coordinate system
    point.append(1)
    p = np.array(point).reshape((3, 1))

    r = matrix.dot(p)
    output = [int(r[0, 0]), int(r[1, 0])]
    return output


def get_Sharpness_score(image):
    grayImg = image[:, :, 2]
    grayImg = cv2.GaussianBlur(grayImg, (15, 15), 0, 0)
    grad_x = cv2.Sobel(grayImg, -1, 1, 0, ksize=5)
    grad_y = cv2.Sobel(grayImg, -1, 0, 1, ksize=5)
    grad = cv2.addWeighted(grad_x, 0.5, grad_y, 0.5, 0)
    return grad.var()
