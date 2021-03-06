# knnMatch 함수로부터 올바른 매칭점 찾기 (match_good_knn.py)
# https://bkshin.tistory.com/entry/OpenCV - 29. 올바른 매칭점 찾기?category=1148027

import cv2
import numpy as np

# image1 = cv2.imread('./data/test_images/SE-8d001dac-f7a0-4699-b59c-d26f49b3abc5.jpeg')
# imge2 = cv2.imread('./data/images/SE-07b4562c-5779-4530-8d52-3f7dfb37f002.jpeg')
# image2 = cv2.imread('./data/test_images/SE-8d001dac-f7a0-4699-b59c-d26f49b3abc5 복사본.jpeg')
#
# test_img1 = "./data/test_images/17.jpg"
# test_img2 = "./data/test_images/1701.jpg"


def knn_match_fun(img1, img2):
    try:
        gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

        # ORB로 서술자 추출 ---①
        detector = cv2.ORB_create()
        kp1, desc1 = detector.detectAndCompute(gray1, None)
        kp2, desc2 = detector.detectAndCompute(gray2, None)
        # BF-Hamming 생성 ---②
        matcher = cv2.BFMatcher(cv2.NORM_HAMMING2)
        # knnMatch, k=2 ---③
        matches = matcher.knnMatch(desc1, desc2, 2)

        # 첫번재 이웃의 거리가 두 번째 이웃 거리의 75% 이내인 것만 추출---⑤
        ratio = 0.75
        good_matches = [first for first, second in matches \
                        if first.distance < second.distance * ratio]
        # good_match_percent = 'matches:%d/%d' % (len(good_matches), len(matches))
        good_match_percent = float(len(good_matches)) / float(len(matches))
        # print(good_match_percent)

        return good_match_percent

    except:
        # print(0)
        return 0

# knn_match_fun(image1, image1)

# knn_match_fun(test_img1, test_img2)











#
# # 좋은 매칭만 그리기
# res = cv2.drawMatches(image1, kp1, image2, kp2, good_matches, None, \
#                     flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)
# # 결과 출력
# cv2.imshow('Matching', res)
# cv2.waitKey()
# cv2.destroyAllWindows()
