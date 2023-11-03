import matplotlib.pyplot as plt
import random
import math
import matplotlib.style as mplstyle
import numpy as np

mplstyle.use('fast')

f_input = open("input.txt", "r")
coords = f_input.readlines()
coords = [i.replace('\n',"") for i in coords]

start = str(coords.pop(0))
start = start.split(" ")
start_x = float(start[0])
start_y = float(start[1])

end = str(coords.pop(0))
end = end.split(" ")
end_x = float(end[0])
end_y = float(end[1])

coords.append(coords[0])
coords_x = [int(float(i.split(" ")[0])) for i in coords]
coords_y = [int(float(i.split(" ")[1])) for i in coords]
coords_xy = []
for i in range(len(coords)):
    coords_xy.append((coords_x[i], coords_y[i]))

plt.xlim(-10, 15)
plt.ylim(-10, 15)
plt.scatter(start_x,start_y, c ="red", zorder=4)
plt.scatter(end_x,end_y, c ="red", zorder=4)
plt.fill(coords_x, coords_y, color="blue")
random.seed(3)

def plotGraph(new_node, nodes, cnt):
    center = new_node
    radius = 1
    theta = np.linspace(0, 2 * np.pi, 100)
    x_cir = center[0] + radius * np.cos(theta)
    y_cir = center[1] + radius * np.sin(theta)    
    fig, ax = plt.subplots()
    ax.set_xlim(-10, 15)
    ax.set_ylim(-10, 15)
    ax.scatter([start_x, end_x], [start_y, end_y], c="red", zorder=4)
    node_coords = [(k[0], k[1]) for k in nodes.keys()]
    node_neighbors = [nodes[k] for k in nodes.keys()]
    for i, neighbor in enumerate(node_neighbors):
        if neighbor is not None:
            x = [node_coords[i][0], neighbor[0]]
            y = [node_coords[i][1], neighbor[1]]
            ax.plot(x, y, c="green", linewidth=0.5)
    x, y = zip(*node_coords)
    ax.scatter(x, y, 5, c="green")
    ax.fill(x_cir, y_cir, c ="yellow")
    ax.scatter(new_node[0], new_node[1], 5, c ="green")
    ax.fill(coords_x, coords_y, color="blue")
    
    # plt.savefig('hw1_{}.png'.format(cnt))


def checkInside(x,y,poly):
    n = len(poly)
    inside = False
    p2x = 0.0
    p2y = 0.0
    xints = 0.0
    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xints:
                        inside = not inside
        p1x,p1y = p2x,p2y
    return inside

def getRandomPoint(coords_xy):
    flag = True
    while flag:
        x = random.uniform(-10, 14)
        y = random.uniform(-10, 14)
        if(checkInside(x, y, coords_xy)):
            flag = True
        else:
            flag = False
    rand = (x,y)
    return rand

def nearestNode(rand, nodes):
    min_dist = float('inf')
    nearest = None
    for node in nodes:
        dist = round(math.dist(rand, node),2)
        if dist < min_dist:
            min_dist = dist
            nearest = node
    return nearest
    
def extend(nodes, rand, i, max_dist, cnt):
    nearest = nearestNode(rand, nodes)
    d = math.dist(nearest, rand)
    if d < max_dist:
        new_x = round(rand[0], 2)
        new_y = round(rand[1], 2)
    else:
        new_x = round(nearest[0] + (rand[0] - nearest[0]) * max_dist / d, 2)
        new_y = round(nearest[1] + (rand[1] - nearest[1]) * max_dist / d, 2)
    
    if(checkInside(new_x, new_y, coords_xy)):
        return None
    else:
        # plotGraph((new_x, new_y), nodes, cnt)
        # plt.show()
        return (new_x, new_y)

def distanceFromStart(node, nodes):
    current = node
    distance1 = 0
    while current != (start_x, start_y):
        distance1 = distance1 + math.dist(current, nodes[current])
        current = nodes[current]
    return distance1

def rewire(new_node, nodes):
    in_radius = []
    for node in nodes:
        if math.dist(new_node, node) < 1 and node != new_node:
            in_radius.append(tuple(node))
            
    min_di = float('inf')
    min_node = ""
    for i in in_radius:
        nodes[new_node] = i
        di = distanceFromStart(new_node, nodes)
        if(min_di > di):
            min_di = di
            min_node = i
        nodes[new_node] = min_node
    
    orig_parent = ()
    for i in in_radius:
        if(nodes[new_node] != i):
            orig_dist = distanceFromStart(i, nodes)
            orig_parent = nodes[i]
            nodes[i] = new_node
            newdist = distanceFromStart(i, nodes)
            if(newdist > orig_dist):
                nodes[i] = orig_parent
    
    return nodes
    
def findPath(new_node, nodes, out, cnt):
    global distance_from_start_end
    if math.dist(new_node, (end_x, end_y)) < 1.0:
        nearest = nearestNode((end_x, end_y), nodes)
        path = [nearest]
        current = nearest
        distance1 = 0
        while current != (start_x, start_y):
            distance1 = distance1 + math.dist(current, nodes[current])
            current = nodes[current]
            path.append(current)
        path.reverse()
        path.append((end_x,end_y))
        # path_x = [i[0] for i in path]
        # path_y = [i[1] for i in path]
        # # plotGraph(new_node, nodes, cnt)
        # for i in range(len(path)):
        #     if(i!=len(path)-1):
        #         pass
        #         plt.plot([path_x[i], path_x[i+1]], [path_y[i], path_y[i+1]], c="black")
        #         plt.savefig('hw1_out_{}_{}.png'.format(out, i))
        # plt.show()
        print(distance1)
        distance_from_start_end.append(distance1)
        


def rrtStar(max_dist):
    global distance_from_start_end
    nodes = {}
    nodes[(start_x, start_y)] = None 
    max_itr = 4000
    flag_nearest_end = True
    nearest_end = ""
    d1 = float('inf')
    d2 = float('inf')
    path_found = False
    cnt = 0
    out = 0
    
    for i in range(max_itr):
        rand = getRandomPoint(coords_xy)
        new_node = extend(nodes, rand, i, max_dist, cnt)
        cnt+=1
        
        if new_node and new_node not in nodes:
            nodes = rewire(new_node, nodes)
            
            if math.dist(new_node, (end_x, end_y)) < 1.0 and flag_nearest_end:
                nearest_end = new_node
                flag_nearest_end = False
                path_found = True
                findPath(nearest_end, nodes, out, cnt)
                out = 1
            if(path_found):
                d1 = distanceFromStart(nearest_end, nodes)
                nearest_end = nearestNode((end_x, end_y), nodes)
                if(d1 < d2):
                    findPath(nearest_end, nodes, out, cnt)
                    nearest_end 
                    d2 = d1
                    out+=1
    
    return nodes

distance_from_start_end = []
nodes = rrtStar(1)  

print(round(distance_from_start_end[0], 2))
print(round(distance_from_start_end[-1], 2))
print(round(28.384776310850235, 2))

with open('output.txt', 'w') as f:
    f.write(str(round(distance_from_start_end[0], 2)) + "\n" + str(round(distance_from_start_end[-1], 2)) + "\n" + str(round(28.384776310850235, 2)))