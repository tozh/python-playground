import numpy as np
import matplotlib.pyplot as plt
from point2D import Point2D
import csv


class CreatePoints:
    def __init__(self, **kwargs):
        self.point_list = []
        self.point_x_list = []
        self.point_y_list = []
        if 'filepath' in kwargs.keys():
            with open(kwargs['filepath'], newline='') as file:
                csvreader = csv.reader(file, delimiter=',')
                for entry in csvreader:
                    point = Point2D(float(entry[0]), float(entry[1]))
                    self.point_list.append(point)
                    self.point_x_list.append(point.x)
                    self.point_y_list.append(point.y)
                file.close()
            self.point_x_list = np.asarray(self.point_x_list)
            self.point_y_list = np.asarray(self.point_y_list)

        elif 'num' in kwargs.keys():
            self.point_x_list = np.random.randn(kwargs['num'])
            self.point_y_list = np.random.randn(kwargs['num'])
            for _x, _y in zip(self.point_x_list, self.point_y_list):
                point = Point2D(_x, _y)
                self.point_list.append(point)

    def __len__(self):
        return len(self.point_list)

    def draw_points(self):
        plt.title('Points')
        plt.scatter(self.point_x_list, self.point_y_list, alpha=0.5, s=10, marker='o')
        plt.show()

    def write_to_csv(self, filename):
        with open(filename, 'w', newline='') as file:
            csvwriter = csv.writer(file, delimiter=',')
            for point in self.point_list:
                csvwriter.writerow([point.x, point.y])
            file.close()

if __name__ == '__main__':
    points = CreatePoints(filepath='points.csv')
    # points.write_to_csv('myPoints.csv')
    points.draw_points()









