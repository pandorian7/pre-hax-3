def det_of_2(mat):
    a, b = mat[0]
    c, d = mat[1]
    return a*d - b*c

def del_raw1(mat):
    return mat[1:]

def del_col_i(mat, i):
    ret = []
    for rn in range(len(mat)):
        ret.append(mat[rn][:i]+mat[rn][i+1:])
    return ret

def get_small_mat(mat, i):
    # print(mat)
    small = del_raw1(mat)
    small = del_col_i(small, i)
    return small

def det(mat):
    if len(mat)==2:
        return det_of_2(mat)
    else:
        small_det =[]
        for i in range(len(mat)):
            small_mat = get_small_mat(mat, i)
            small_det.append(det(small_mat)*mat[0][i])
        # print(small_det)
        return sum(small_det[::2]) - sum(small_det[1::2])


valid_odd = [-5, -3, -1, 1, 3, 5]


print(det([[2, 4, 1, 4], [6, 3, 1, 9], [2, 3, 1, 3], [1, 3, 5, 6]]))