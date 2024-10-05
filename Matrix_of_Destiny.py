def is_matrix(mat):
    row_lens_set =  set(list(map(len, mat)))
    if len(row_lens_set)==1:
        return True
    else: 
        return False
def req_mat(mat):
    assert is_matrix(mat), "this is not a matrix"


def is_square_matrix(mat):
    req_mat(mat)
    if len(mat)==len(mat[0]):
        return True
    return False

def req_mat_2(mat):
    req_mat(mat) 
    assert is_square_matrix(mat), "this is not a square matrix"

def det_of_2(mat):
    req_mat_2()
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
    req_mat_2(mat)
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


print(det([[2, 4, 1, 4, 3], [6, 3, 1, 9, 10], [2, 3, 1, 3, 23], [1, 3, 5, 6, 3]]))
