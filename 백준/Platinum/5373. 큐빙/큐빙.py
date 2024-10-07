import sys
input = sys.stdin.readline

u_side = [['w' for _ in range(3)] for _ in range(3)]
d_side = [['y' for _ in range(3)] for _ in range(3)]
f_side = [['r' for _ in range(3)] for _ in range(3)]
b_side = [['o' for _ in range(3)] for _ in range(3)]
l_side = [['g' for _ in range(3)] for _ in range(3)]
r_side = [['b' for _ in range(3)] for _ in range(3)]

def rotate_face_cw(face):
    temp = [row[:] for row in face]
    for i in range(3):
        for j in range(3):
            face[j][2 - i] = temp[i][j]

def rotate_face_ccw(face):
    temp = [row[:] for row in face]
    for i in range(3):
        for j in range(3):
            face[2 - j][i] = temp[i][j]

def rotate_u_plus():
    rotate_face_cw(u_side)
    f1, f2, f3 = f_side[0]

    for i in range(3):
        f_side[0][i] = r_side[0][i]

    for i in range(3):
        r_side[0][i] = b_side[0][i]

    for i in range(3):
        b_side[0][i] = l_side[0][i]

    l_side[0][0] = f1
    l_side[0][1] = f2
    l_side[0][2] = f3

def rotate_u_minus():
    rotate_face_ccw(u_side)
    f1, f2, f3 = f_side[0]

    for i in range(3):
        f_side[0][i] = l_side[0][i]

    for i in range(3):
        l_side[0][i] = b_side[0][i]

    for i in range(3):
        b_side[0][i] = r_side[0][i]

    r_side[0][0] = f1
    r_side[0][1] = f2
    r_side[0][2] = f3

def rotate_d_plus():
    rotate_face_cw(d_side)
    f1, f2, f3 = f_side[2]

    for i in range(3):
        f_side[2][i] = l_side[2][i]

    for i in range(3):
        l_side[2][i] = b_side[2][i]

    for i in range(3):
        b_side[2][i] = r_side[2][i]

    r_side[2][0] = f1
    r_side[2][1] = f2
    r_side[2][2] = f3

def rotate_d_minus():
    rotate_face_ccw(d_side)
    f1, f2, f3 = f_side[2]

    for i in range(3):
        f_side[2][i] = r_side[2][i]

    for i in range(3):
        r_side[2][i] = b_side[2][i]

    for i in range(3):
        b_side[2][i] = l_side[2][i]

    l_side[2][0] = f1
    l_side[2][1] = f2
    l_side[2][2] = f3

def rotate_f_plus():
    rotate_face_cw(f_side)
    u1, u2, u3 = u_side[2]

    for i in range(3):
        u_side[2][i] = l_side[2 - i][2]

    for i in range(3):
        l_side[i][2] = d_side[0][i]

    for i in range(3):
        d_side[0][i] = r_side[2 - i][0]

    r_side[0][0] = u1
    r_side[1][0] = u2
    r_side[2][0] = u3

def rotate_f_minus():
    rotate_face_ccw(f_side)
    u1, u2, u3 = u_side[2]

    for i in range(3):
        u_side[2][i] = r_side[i][0]

    for i in range(3):
        r_side[i][0] = d_side[0][2 - i]

    for i in range(3):
        d_side[0][i] = l_side[i][2]

    l_side[0][2] = u3
    l_side[1][2] = u2
    l_side[2][2] = u1

def rotate_b_plus():
    rotate_face_cw(b_side)
    u1, u2, u3 = u_side[0]

    for i in range(3):
        u_side[0][i] = r_side[i][2]

    for i in range(3):
        r_side[i][2] = d_side[2][2 - i]

    for i in range(3):
        d_side[2][i] = l_side[i][0]

    l_side[0][0] = u3
    l_side[1][0] = u2
    l_side[2][0] = u1    

def rotate_b_minus():
    rotate_face_ccw(b_side)
    u1, u2, u3 = u_side[0]

    for i in range(3):
        u_side[0][i] = l_side[2 - i][0]

    for i in range(3):
        l_side[i][0] = d_side[2][i]
    
    for i in range(3):
        d_side[2][i] = r_side[2 - i][2]

    r_side[0][2] = u1
    r_side[1][2] = u2
    r_side[2][2] = u3

def rotate_r_plus():
    rotate_face_cw(r_side)
    u1, u2, u3 = u_side[0][2], u_side[1][2], u_side[2][2]

    for i in range(3):
        u_side[i][2] = f_side[i][2]

    for i in range(3):
        f_side[i][2] = d_side[i][2]

    for i in range(3):
        d_side[i][2] = b_side[2 - i][0]
    
    b_side[0][0] = u3
    b_side[1][0] = u2
    b_side[2][0] = u1

def rotate_r_minus():
    rotate_face_ccw(r_side)
    u1, u2, u3 = u_side[0][2], u_side[1][2], u_side[2][2]

    for i in range(3):
        u_side[i][2] = b_side[2 - i][0]

    for i in range(3):
        b_side[i][0] = d_side[2 - i][2]

    for i in range(3):
        d_side[i][2] = f_side[i][2]

    f_side[0][2] = u1
    f_side[1][2] = u2
    f_side[2][2] = u3

def rotate_l_plus():
    rotate_face_cw(l_side)
    u1, u2, u3 = u_side[0][0], u_side[1][0], u_side[2][0]

    for i in range(3):
        u_side[i][0] = b_side[2 - i][2]

    for i in range(3):
        b_side[i][2] = d_side[2 - i][0]

    for i in range(3):
        d_side[i][0] = f_side[i][0]
    
    f_side[0][0] = u1
    f_side[1][0] = u2
    f_side[2][0] = u3

def rotate_l_minus():
    rotate_face_ccw(l_side)
    u1, u2, u3 = u_side[0][0], u_side[1][0], u_side[2][0]

    for i in range(3):
        u_side[i][0] = f_side[i][0]

    for i in range(3):
        f_side[i][0] = d_side[i][0]
    
    for i in range(3):
        d_side[i][0] = b_side[2 - i][2]

    b_side[0][2] = u3
    b_side[1][2] = u2
    b_side[2][2] = u1

rotate_functions = {
    'U+': rotate_u_plus,
    'U-': rotate_u_minus,
    'D+': rotate_d_plus,
    'D-': rotate_d_minus,
    'F+': rotate_f_plus,
    'F-': rotate_f_minus,
    'B+': rotate_b_plus,
    'B-': rotate_b_minus,
    'L+': rotate_l_plus,
    'L-': rotate_l_minus,
    'R+': rotate_r_plus,
    'R-': rotate_r_minus,
}

n = int(input())

for id in range(n):
    rotate_count = int(input())
    rotate_type_list = list(map(str, input().rstrip().split()))

    for rotate_type in rotate_type_list:
        rotate_functions[rotate_type]()

    for r in u_side:
        print(''.join(r))

    u_side = [['w' for _ in range(3)] for _ in range(3)]
    d_side = [['y' for _ in range(3)] for _ in range(3)]
    f_side = [['r' for _ in range(3)] for _ in range(3)]
    b_side = [['o' for _ in range(3)] for _ in range(3)]
    l_side = [['g' for _ in range(3)] for _ in range(3)]
    r_side = [['b' for _ in range(3)] for _ in range(3)]