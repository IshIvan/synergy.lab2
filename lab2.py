from graphics import *


def lab2():
    width = 500
    height = 500
    win = GraphWin('lab2', width, height)
    # win.setCoords(0, 0, 4, 4)
    Rmin = 1.0
    Rmax = 3.0
    stepSize = 0.01
    x0 = 0.5
    iterationNumber = 50
    r = Rmin
    while r < Rmax:
        x = x0
        array_x = [x0]
        last_delta = 0.01
        for i in range(0, iterationNumber):
            last_x = x
            x = (1 + r) * x - r * x * x
            # if (x - last_x) * last_delta < 0:
            #     cond = True
            #     for point_x in array_x:
            #         if abs(point_x - last_x) < 0.01:
            #             cond = False
            #             break
            #     if cond:
            #         print(len(array_x))
            #         if len(array_x) > 10:
            #             print(array_x)
            #             return
                    # array_x.append(last_x)
                    # print((x - last_x))
                # print((last_delta))
                # print('tes')
            # last_delta = x - last_x

        # array_x.pop(0)
        # for point_x in array_x:
        #     point = Point(r, point_x)
        #     point.draw(win)
            point = Point(width * (r - 1) / 2, height - x * height)
            point.draw(win)
        r += stepSize

    win.getMouse()
    win.close()


lab2()
