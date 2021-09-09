import cv2


class ForestFireSegmentation:
    def __init__(self, lower=(82, 0, 159), upper=(255, 255, 255), method="lab"):
        self.lower = lower
        self.upper = upper
        self.method = method

    def __change_color_space_masking(self, img):
        if self.method == "hsv":
            img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        elif self.method == "ycrcb":
            img = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
        elif self.method == "lab":
            img = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
        else:
            raise "Input color space method correctly!"

        img = cv2.inRange(img, self.lower, self.upper)

        return img

    def preprocessing_image(self, img):
        img_mask = self.__change_color_space_masking(img)
        img_final = cv2.bitwise_and(img, img, mask=img_mask)
        img_gray = cv2.cvtColor(img_final, cv2.COLOR_BGR2GRAY)
        img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
        _, img_thresh = cv2.threshold(img_blur, 0, 255, cv2.THRESH_BINARY)

        return img_thresh, img_final

    def get_large_of_fire(self, img_final):
        img_contours, _ = cv2.findContours(
            img_final, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
        )
        all_area_contours = []
        for contour in img_contours:
            area = cv2.contourArea(contour)
            all_area_contours.append(area)
        area_countour = sum(all_area_contours)

        return area_countour

    def draw_large_of_fire(self, img_final, img_draw):
        img_contours, _ = cv2.findContours(
            img_final, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
        )
        for contour in img_contours:
            cv2.drawContours(img_draw, [contour], -1, (255, 0, 0), cv2.FILLED)
