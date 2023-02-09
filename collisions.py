import vector_math
import math

##single ray sphere intersection

def sphere_intersection_point(ray, sphere):
    difference_ray_to_sphere = vector_math.difference_point(ray.pt , sphere.center)

    a = vector_math.dot_vector(ray.dir, ray.dir)
    b = 2 * vector_math.dot_vector(difference_ray_to_sphere, ray.dir)
    c = vector_math.dot_vector(difference_ray_to_sphere, difference_ray_to_sphere) - sphere.radius**2

    dis = (b**2 - 4*a*c)

    if dis < 0:
        return None
    if a == 0:
        return None
    else:
        t = (-b + math.sqrt(dis)) / (2 * a)
        t2 = (-b - math.sqrt(dis)) / (2 * a)

        if t >= 0 and t2 < 0:
            return vector_math.translate_point(ray.pt, (vector_math.scale_vector(ray.dir, t)))
        elif t < 0 and t2 >= 0:
            return vector_math.translate_point(ray.pt, (vector_math.scale_vector(ray.dir, t2)))
        elif t < 0 and t2 < 0:
            return None
        else:
            return vector_math.translate_point(ray.pt, (vector_math.scale_vector(ray.dir, min(t, t2))))

def find_intersection_points(sphere_list, ray):
    intersection_list = []
    for i in sphere_list:
        intersect = sphere_intersection_point(ray, i)
        if intersect is not None:
            intersection_list.append((i, intersect))
    return intersection_list


def sphere_normal_at_point(sphere, point):
    return vector_math.normalize_vector(vector_math.vector_from_to(sphere.center, point))