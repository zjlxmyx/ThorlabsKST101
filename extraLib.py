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

def get_scan_pos(leftdown,rightdown,rightup,leftup): # position format: [x, y]  (it is 2 dimension)
    x1 = max(leftdown[0], leftup[0])
    x2 = min(rightdown[0], rightup[0])
    y1 = max(leftdown[1], rightdown[1])
    y2 = min(leftup[1], rightup[1])

    x_array = np.arange((x1+127875), (x2-127875), 214500, 'int')
    y_array = np.arange((y1+94875), (y2-94875), 148500, 'int')

    return x_array, y_array

def Estimate_z_pos(p, leftdown,rightdown,rightup,leftup):
    # p: [x, y] position to estimated, 4 corners position format: [x, y, z]  (it is 3 dimension)
    ratio_down = (p[0]-leftdown[0])/(rightdown[0]-leftdown[0])
    y_e1 = ratio_down*(rightdown[1]-leftdown[1])+leftdown[1]
    z_e1 = ratio_down*(rightdown[2]-leftdown[2])+leftdown[2]

    ratio_up = (p[0]-leftup[0])/(rightup[0]-leftup[0])
    y_e2 = ratio_up*(rightup[1]-leftup[1])+leftup[1]
    z_e2 = ratio_up*(rightup[2]-leftup[2])+leftup[2]

    z = ((p[1]-y_e1)/(y_e2-y_e1))*(z_e2-z_e1)+z_e1

    return int(z)





#
# a=[0,0]
# b=[3150675,0]
# c=[3141600,3373425]
# d=[-56100,3220800]
# x,y = get_scan_pos(a,b,c,d)
# p = len(x)*len(y)
# print(x)
# print(y)
# print('there are ' + str(p) + ' photos should be captured')
# print('it will takes ' + str(p*15/60) +' mins')


a=[0,0,3446390]
b=[3150675,0,3418884]
c=[3141600,3373425,3490590]
d=[-56100,3220800,3548622]

x_array, y_array = get_scan_pos(a[0:2], b[0:2], c[0:2], d[0:2])

for x in x_array:
    for y in y_array:
       z = Estimate_z_pos([x, y], a, b, c, d)
       print(x, y, z)