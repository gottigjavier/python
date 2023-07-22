# Open input.txt if it exists and is in the correct format
try:
    with open("input.txt", "r") as input_file:
        ball1 = [int(x) for x in input_file.readline().split(" ")]
        ball2 = [int(x) for x in input_file.readline().split(" ")]
except:
    message = "Error reading input file."
    output_file = open("output.txt", "w")
    output_file.write(message)
    output_file.close()
    print(message)
    exit()

MAX_ABS_VALUE= 10000
R1 = ball1[0]

if max(ball1) > MAX_ABS_VALUE or max(ball2) > MAX_ABS_VALUE:
    message = "Error: at least one of the values exceeds the maximum allowed (10000)."
    output_file = open("output.txt", "w")
    output_file.write(message)
    output_file.close()
    print(message)
    exit()

ball1_position = [ball1[1], ball1[2], ball1[3]]
ball2_position = [ball2[1], ball2[2], ball2[3]]
ball1_mov = [ball1[4], ball1[5], ball1[6]]
ball2_mov = [ball2[4], ball2[5], ball2[6]]



# RADII == minimum center distance or collision distance
RADII = ball1[0] + ball2[0]

# vector_b1_b2() creates a vector pointing to ball2 from ball1.
def vector_b1_b2(balla, ballb):
    return [ballb[0] - balla[0], ballb[1] - balla[1], ballb[2] - balla[2]]
    
# The module_vector_b1_b2 is the distance between the centers of ball1 and ball2.
def module_vector_b1_b2(vector):
    dist = (vector[0]**2 + vector[1]**2 + vector[2]**2)**(1/2)
    return dist

# Direction cosines of vector_b1_b2
def cos_vector_b1_b2(vector, module):
    alpha = vector[0]/module
    beta = vector[1]/module
    gamma = vector[2]/module
    return [alpha, beta, gamma]

# Coordinates of the edge of ball1 in the direction of ball2. It is a point of vector_b1_b2 with radius ball1[0]
def ball1_edge(cos_vector):
    vector_ball1_edge = [R1*cos_vector[0], R1*cos_vector[1], R1*cos_vector[2]]
    return vector_ball1_edge

# Time limit? For the flight of the balls? For the computation process?: ambiguous. It is decided to take the positions reading time every 0.5 s.
def mov_half_s(v):
    v = v/2
    return v

def vector_addition(vec1, vec2):
    return [vec1[0] + vec2[0], vec1[1] + vec2[1], vec1[2] + vec2[2]]

def new_position(ball, move):
    ballx = ball[0] + mov_half_s(move[0])
    bally = ball[1] + mov_half_s(move[1])
    ballz = ball[2] + mov_half_s(move[2])
    return [ballx, bally, ballz]

def check_collision(pos1, mov1, pos2, mov2):
    prev_position1= pos1
    prev_position2= pos2
    vector_b1b2 = vector_b1_b2(pos1, pos2)
    distance_between_centers = module_vector_b1_b2(vector_b1b2)
    post_distance_between_centers = MAX_ABS_VALUE
    while distance_between_centers > RADII:
        if post_distance_between_centers > distance_between_centers:
            it_moves_away = False
            post_distance_between_centers = distance_between_centers
            ball1_new_position = new_position(prev_position1, mov1)
            ball2_new_position = new_position(prev_position2, mov2)
            vector_b1b2 = vector_b1_b2(ball1_new_position, ball2_new_position)
            distance_between_centers = module_vector_b1_b2(vector_b1b2)
            prev_position1 = ball1_new_position
            prev_position2 = ball2_new_position
        else:
            message ="NO\n"
            data_out = '{:.5f}'.format(distance_between_centers - RADII)
            it_moves_away = True
            break
    if not it_moves_away:
        director_cosines = cos_vector_b1_b2(vector_b1b2, distance_between_centers)
        contact_point = vector_addition(ball1_edge(director_cosines), ball1_new_position)
        data = ['{:.5f}'.format(punt_contac) for punt_contac in contact_point]
        data_out = " ".join(data)
        message ="YES\n"
    output_file = open("output.txt", "w")
    output_file.write(message)
    output_file.write(data_out)
    output_file.close()

check_collision(ball1_position, ball1_mov, ball2_position, ball2_mov)