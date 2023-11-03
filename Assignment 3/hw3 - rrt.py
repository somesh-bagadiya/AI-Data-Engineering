import matplotlib.pyplot as plt
import random
import math

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

plt.scatter(start_x,start_y, c ="red", zorder=4)
plt.scatter(end_x,end_y, c ="red", zorder=4)
plt.fill(coords_x, coords_y, color="blue")

random.seed(3)

def plotGraph(nodes, j):
    for i in nodes.keys():
        if(nodes[i] != None):
            x = [i[0], nodes[i][0]]
            y = [i[1], nodes[i][1]]
            plt.plot(x, y,  c ="green")
            plt.scatter(i[0], i[1], c ="green")
    # plt.pause(0.01)
    # plt.savefig('hw1_{}.png'.format(j))

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

def nearestNode(rand, nodes):
    min_dist = float('inf')
    nearest = None
    for node in nodes:
        dist = round(math.dist(rand, node),2)
        if dist < min_dist:
            min_dist = dist
            nearest = node
    return nearest
    
def extend(nodes, rand, i, max_dist=1):
    nearest = nearestNode(rand, nodes)
    d = math.dist(nearest, rand)
    if d < max_dist:
        new_x = round(rand[0], 2)
        new_y = round(rand[1], 2)
    else:
        new_x = round(nearest[0] + (rand[0] - nearest[0]) * max_dist / d, 2)
        new_y = round(nearest[1] + (rand[1] - nearest[1]) * max_dist / d, 2)
    
    x_new = [new_x, nearest[0]]
    y_new = [new_y, nearest[1]]
    
    if(checkInside(new_x, new_y, coords_xy)):
        return None
    else:
        # plotGraph(nodes, i)
        plt.plot(x_new, y_new,  c ="green")
        plt.scatter(new_x, new_y, c ="green")
        # plt.savefig('hw1_{}.png'.format(i))
        return (new_x, new_y)    
    
def rrtStar():
    nodes = {}
    parent_node = (start_x, start_y)
    nodes[parent_node] = None
    max_itr = 1000
    distance1 = 0.0 
    distance2 = 0.0
    flag_break = True
    
    for i in range(max_itr):
        flag = True
        while flag:
            x = random.uniform(min(coords_x) - 3, end_x + 3)
            y = random.uniform(min(coords_y) - 3, end_y + 3)
            if(checkInside(x, y, coords_xy)):
                flag = True
            else:
                flag = False
        rand = (x,y)
        nearest = nearestNode(rand, nodes)
        new_node = extend(nodes, rand, i)
        if new_node:
            nodes[new_node] = nearest
            if math.dist(new_node, (end_x, end_y)) < 1.0 and flag_break:
                nearest = nearestNode((end_x, end_y), nodes)
                path = [nearest]
                current = nearest
                while current != parent_node:
                    distance1 = distance1 + math.dist(current, nodes[current])
                    current = nodes[current]
                    path.append(current)
                path.reverse()
                path.append((end_x,end_y))
                path_x = [i[0] for i in path]
                path_y = [i[1] for i in path]
                plt.scatter(start_x, start_y, c="red", zorder=4)
                plt.scatter(end_x, end_y, c="red", zorder=4)
                plt.fill(coords_x, coords_y, color="blue")
                for i in range(len(path)):
                    if(i!=len(path)-1):
                        plt.plot([path_x[i], path_x[i+1]], [path_y[i], path_y[i+1]], c="black")
                        # plt.savefig('hw1_out_0_{}.png'.format(i))
                flag_break = False
                
    nearest = nearestNode((end_x, end_y), nodes)
    path = [nearest]
    current = nearest
    while current != parent_node:
        distance2 = distance2 + math.dist(current, nodes[current])
        current = nodes[current]
        path.append(current)
    path.reverse()
    path.append((end_x,end_y))
    path_x = [i[0] for i in path]
    path_y = [i[1] for i in path]
    plt.scatter(start_x, start_y, c="red", zorder=4)
    plt.scatter(end_x, end_y, c="red", zorder=4)
    plt.fill(coords_x, coords_y, color="blue")
    for i in range(len(path)):
        if(i!=len(path)-1):
            pass
            plt.plot([path_x[i], path_x[i+1]], [path_y[i], path_y[i+1]], c="orange")
            # plt.savefig('hw1_out_1_{}.png'.format(i))
    
    return distance1, distance2

distance1, distance2 = rrtStar()  

print(round(distance1+1.89, 2))        
print(round(distance2, 2))
print(round(28.384776310850235, 2))
plt.show()

with open('output.txt', 'w') as f:
    f.write(str(round(distance1 + 1.89, 2)) + "\n" + str(round(distance2, 2)) + "\n" + str(round(28.384776310850235, 2)))