import numpy as np
import cv2

class figure():
    x=0
    y=0
    pt1 = [x, y]
    pt2 = [x, y]
    pt3 = [x, y]
    pt4 = [x, y]
    pt5 = [x, y]
    pt6 = [x, y]

    def drawtriangle(self, pt1, pt2, pt3):
        self.pt1=pt1
        self.pt2=pt2
        self.pt3=pt3
        triangle_cnt = np.array([self.pt1, self.pt2, self.pt3])
        cv2.drawContours(img, [triangle_cnt], 0, (110, 55, 255), -1)

    def drawromb(self, pt1, pt2, pt3, pt4):
        self.pt1=pt1
        self.pt2=pt2
        self.pt3=pt3
        self.pt4=pt4
        romb_cnt = np.array([self.pt1, self.pt2, self.pt3, self.pt4])
        cv2.drawContours(img, [romb_cnt], 0, (130, 220, 255), -1)

    def drawhecsagon(self, pt1, pt2, pt3, pt4, pt5, pt6):
        self.pt1=pt1
        self.pt2=pt2
        self.pt3=pt3
        self.pt4=pt4
        self.pt5=pt5
        self.pt6=pt6
        hecsagon_cnt = np.array([self.pt1, self.pt2, self.pt3, self.pt4, self.pt5, self.pt6])
        cv2.drawContours(img, [hecsagon_cnt], 0, (250, 20, 255), -1)

    def circle(self, center_coordinatesc, radius, color, thickness):
        self.center_coordinatesc = center_coordinatesc
        self.radius = radius
        self.color = color
        self.thickness = thickness
        cv2.circle(img, center_coordinatesc, radius, color, thickness)

    def drawsquare(self, pt1, pt2, pt3, pt4):
        self.pt1=pt1
        self.pt2=pt2
        self.pt3=pt3
        self.pt4=pt4
        romb_cnt = np.array([self.pt1, self.pt2, self.pt3, self.pt4])
        cv2.drawContours(img, [romb_cnt], 0, (0, 255, 0), -1)





if __name__ == '__main__':

    img = np.zeros((256, 256, 3), np.uint8)

    figure.drawtriangle(figure, [10, 20], [30, 30], [50, 70])
    figure.drawromb(figure, [100, 100], [140, 125], [140, 150], [100, 125])
    figure.drawhecsagon(figure, [150, 25], [180, 40], [180, 60], [150, 75], [120, 60], [120, 40])
    figure.circle(figure, (80, 200), 20, (255, 0, 0), -1)
    figure.drawsquare(figure, [200,200], [230,200], [230, 230], [200, 230])

    cv2.rectangle(img, (100, 100), (140, 150), (0, 255, 0), 1)


    cv2.imshow("Image", img)
    cv2.waitKey()