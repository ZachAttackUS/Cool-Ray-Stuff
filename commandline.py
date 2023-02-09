import data
import sys


def process_args():
    view = (-10, 10, -7.5, 7.5, 512, 384)
    light = data.Light(data.Point(-100.0, 100.0, -100.0), data.Color(1.5,1.5,1.5))
    eye = data.Point(0,0,-14)
    ambient_color = data.Color(1.0,1.0,1.0)
    i = 2
    while i < len(sys.argv):
        arglist = sys.argv[i]
        if arglist == '-eye':
            try:
                x = float(sys.argv[i + 1])
                y = float(sys.argv[i + 2])
                z = float(sys.argv[i + 3])
                eye = data.Point(x, y, z)
            except IndexError:
                print('malformed Parameters 1')
            except ValueError:
                print('malformed Parameters')
            i = i + 4

        if arglist == '-view':
            try:
                min_x = int(sys.argv[i + 1])
                max_x = int(sys.argv[i + 2])
                min_y = int(sys.argv[i + 3])
                max_y = int(sys.argv[i + 4])
                width = int(sys.argv[i + 5])
                height = int(sys.argv[i + 6])
                view = (min_x, max_x, min_y, max_y, width, height)
            except IndexError:
                print('malformed Parameters 2')

            i = i + 7
        if arglist == '-light':
            try:
                x_light = float(sys.argv[i + 1])
                y_light = float(sys.argv[i + 2])
                z_light = float(sys.argv[i + 3])
                r_light = float(sys.argv[i + 4])
                g_light = float(sys.argv[i + 5])
                b_light = float(sys.argv[i + 6])
                light = data.Light(data.Point(x_light, y_light, z_light), data.Color(r_light,g_light, b_light))
            except IndexError:
                print('malformed Parameters 3')

            i = i + 7
        if arglist == '-ambient':
            try:
                r_ambient = float(sys.argv[i + 1])
                g_ambient = float(sys.argv[i + 2])
                b_ambient = float(sys.argv[i + 3])
                ambient_color = data.Color(r_ambient, g_ambient, b_ambient)
                print(r_ambient, g_ambient, b_ambient)
            except IndexError:
                print('malformed Parameters 4')
            except ValueError:
                print('ValueError')
            i = i + 4

    return [eye, light, ambient_color, view]




