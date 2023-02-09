import cast
import data


color1 = data.Color(1.0,0.0,0.0)
color2 = data.Color(0.0,0.0,1.0)
sphere1 = data.Sphere(data.Point(1.0, 1.0, 0.0), 2.0, color2, data.Finish(0.2, 0.4, 0.5, 0.05))
sphere2 = data.Sphere(data.Point(0.5, 1.5, -3.0), 0.5, color1, data.Finish(0.4, 0.4, 0.5, 0.05))
sphere_list = [sphere1, sphere2]
cast.cast_all_rays(-10, 10, -7.5, 7.5, 512, 384, data.Point(0, 0.0, -14), sphere_list, data.Color(1.0, 1.0, 1.0),
                   data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5, 1.5, 1.5)))
