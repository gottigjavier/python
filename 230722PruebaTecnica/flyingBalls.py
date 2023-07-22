# Se arroja una pelota al aire y con otra pelota se intentará interceptar la primera
# Los datos iniciales deben ser leídos desde un archivo "input.txt" con el siguiente formato:
# 1 0 0 10 0 0 -2
# 3 0 0 0 0 0 1
# donde los valores (integer) de cada línea correponden a cada pelota y cada valor
# separado por espacio tiene la siguiente distribución: 
# radio(1), coordenadas de posisión del centro de lapelota (3) y vector velocidad (3):
# R x y z vx vy vz

# Si las pelotas se tocan se debe generar un archivo de salida "output.txt" con el texto "YES" 
# y las coordenadas del punto de contacto.
# Si no se tocan, el texto será "NO" y la distancia mínima que hubo entre ellas
# Todos lo datos numéricos de salida tienen que tener cinco decimales.
# Ninguna magnitud absoluta debería exceder el número 10000.





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
# Esas coordenadas están a una distancia ball1["R"] de centro de ball1 con dirección vector_b1_b2
# y se obtienen despejando de los cosenos directores de vector_b1_b2.
def ball1_edge(cos_vector):
    vector_ball1_edge = [R1*cos_vector[0], R1*cos_vector[1], R1*cos_vector[2]]
    return vector_ball1_edge

# El tiempo se toma cada 0.5s. Se calcula el movimiento de ambas bolas en ese tiempo.
# Time limit? For the flight of the balls? For the computation process? It is decided to take the positions reading time every 0.5 s.
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

# Las coordenadas del punto de colision serán en un punto del vector a una distancia del radio de (p.ej) ball1


def check_collision(pos1, mov1, pos2, mov2):
    count = 0
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
            count = count + 1
            print("Iteración: ", count)
            print("Posición de ball1: ", ball1_new_position)
            print("Posición de ball2: ", ball2_new_position)
            print("vector_b1_b2 dentro del while: ", vector_b1b2)
            print("Distancia entre centros: ", distance_between_centers)
            print("Mínima distancia entre bordes: ", distance_between_centers - RADII)
        else:
            message ="NO\n"
            data_out = '{:.5f}'.format(distance_between_centers - RADII)
            it_moves_away = True
            break
    if not it_moves_away:
        print("vector_b1_b2 fuera del while: ", vector_b1b2)
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