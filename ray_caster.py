import commandline
import data
import sys
import cast

def create_sphere_list():
    inputfile = sys.argv[1]
    sph_in = open(inputfile, 'r')
    s_list = []
    for line in sph_in:
        s_data = line.split()
        try:
            x_point = float(s_data[0])
            y_point = float(s_data[1])
            z_point = float(s_data[2])
            radius = float(s_data[3])
            red = float(s_data[4])
            green = float(s_data[5])
            blue = float(s_data[6])
            ambient = float(s_data[7])
            diffuse = float(s_data[8])
            specular = float(s_data[9])
            roughness = float(s_data[10])
            sphere = data.Sphere(data.Point(x_point,y_point,z_point),radius, data.Color(red,green,blue),data.Finish(ambient,diffuse,specular,roughness))
            s_list.append(sphere)

        except IndexError:
            print('skipping line for IndexError')

        except TypeError:
            print('skipping line for Type error')
    return s_list

def main():
    s = create_sphere_list()
    args = commandline.process_args()
    eye = args[0]
    light = args[1]
    amb = args[2]
    view = args[3]
    cast.cast_all_rays(args[3][0], view[1], view[2], view[3], view[4], view[5], eye, s, amb, light)
    print('got here')


if __name__ == '__main__':
    main()