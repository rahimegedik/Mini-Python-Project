import math


def compute_distance (x1, x2, y1, y2):
    d = math.sqrt(((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1)))
    return d