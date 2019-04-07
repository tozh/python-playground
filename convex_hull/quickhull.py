from create_points import CreatePoints
from point2D import Point2D
import numpy as np
import matplotlib.pyplot as plt
import random


class QuickHull:
    def __init__(self, _points):
        self.points = _points
        self.point_list = _points.point_list
        self.hull = []
        self.sorted_hull = []

    @staticmethod
    def cross_product(p1, p2, point):
        '''
        (p1 -> p2) is a line, judge if point on the right side of (p1->p2)
        make a vector cross product: (p1 -> p2) x (p1 -> point)
        if the cross product's 3rd dimension < 0: right side
        if > 0: left side
        else: point on the line (p1 -> p2)
        time O(1)
        :param p1:
        :param p2:
        :param point:
        :return: (p1 -> p2) x (p1 -> point)'s 3rd dimension
        '''

        vector_p1_p2 = (p2.x - p1.x, p2.y - p1.y)
        vector_p1_point = (point.x - p1.x, point.y - p1.y)
        return vector_p1_p2[0] * vector_p1_point[1] - vector_p1_p2[1]*vector_p1_point[0]

    def find_hull(self, point_list, p1, p2):
        if len(point_list) == 0:
            return
        else:
            farthest_point = point_list[0]
            farthest_dist = self.cross_product(p1, p2, farthest_point)
            for point in point_list:
                # find the farthest point
                cp = self.cross_product(p1, p2, point)
                if cp < farthest_dist:
                    farthest_point = point
                    farthest_dist = cp
            self.hull.append(farthest_point)  # add this farthest point to the hull

            rightside_p1_fp = []  # the points on the right side of (p1 -> farthest_point)
            rightside_fp_p2 = []  # the points on the right side of (farthest_point -> p2)
            for point in point_list:
                if self.cross_product(p1, farthest_point, point) < 0:
                    rightside_p1_fp.append(point)
                elif self.cross_product(farthest_point, p2, point) < 0:
                    rightside_fp_p2.append(point)

            self.find_hull(rightside_p1_fp, p1, farthest_point)
            self.find_hull(rightside_fp_p2, farthest_point, p2)
        return


    def quick_hull(self):
        '''
        time O(nlogn)
        :return:
        '''
        l = Point2D(100, 0)
        r = Point2D(-100, 0)
        # find the most right and left point
        for point in self.point_list:
            l = point if point < l else l
            r = point if point > r else r
        self.hull.append(l)
        self.hull.append(r)
        self.left = l
        self.right = r

        rightside_l_r = []  #  the points on the right side of (l -> r)
        rightside_r_l = []  #  the points on the right side of (r -> l)

        for point in self.point_list:
            # seperate point_list to rightside_l_r and rightside_r_l
            cp = self.cross_product(l, r, point)
            if cp > 0:
                # on the right side of (r->l)
                rightside_r_l.append(point)
            elif cp < 0:
                # on the right side of (l->r)
                rightside_l_r.append(point)

        self.find_hull(rightside_l_r, l, r)
        length = len(self.hull)

        l_to_r = self.hull[2:]
        list.sort(l_to_r)

        self.find_hull(rightside_r_l, r, l)

        r_to_l = self.hull[length:]
        list.sort(r_to_l, reverse=True)

        self.sorted_hull = [self.left] + l_to_r + [self.right] + r_to_l + [self.left]

        return self.hull

    def is_in_hull(self, point):
        '''
        if point inside the hull, cross_product(p1, p2, point) should > 0
        time: O(h)
        :param point:
        :return:
        '''
        for i in range(len(self.sorted_hull)-1):
            if self.cross_product(self.sorted_hull[i], self.sorted_hull[i+1], point) < 0:
                return False
        return True

    def draw_hull(self):
        x = [point.x for point in self.sorted_hull]
        y = [point.y for point in self.sorted_hull]
        _x = np.asarray(x)
        _y = np.asarray(y)

        point = Point2D(2, 3)
        print(self.is_in_hull(point))
        p_x = np.asarray([point.x])
        p_y = np.asarray([point.y])
        plt.scatter(p_x, p_y, color='red', s=2, alpha=1)

        plt.title('Points and Convex Hull')
        plt.scatter(self.points.point_x_list, self.points.point_y_list, alpha=0.5, s=2, marker='o')
        plt.plot(_x, _y, color='g', linewidth=0.2)
        plt.show()

if __name__ == '__main__':
    points = CreatePoints(num=1000)
    points.write_to_csv('points.csv')
    qh = QuickHull(points)
    qh.quick_hull()
    qh.is_in_hull(Point2D(2, 3))
    qh.draw_hull()









