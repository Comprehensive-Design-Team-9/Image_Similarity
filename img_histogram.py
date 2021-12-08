import cv2
from matplotlib import pyplot as plt
# img = cv2.imread('./test_images/SE-8d001dac-f7a0-4699-b59c-d26f49b3abc5 복사본.jpeg')
# color = ('b','g','r')
# for i,col in enumerate(color):
#     histr = cv2.calcHist([img],[i],None,[256],[0,256])
#     plt.plot(histr,color = col)
#     plt.xlim([0,256])
# plt.show()


# hist_blue = cv2.calcHist([img],[0],None,[256],[0,256])
# hist_green = cv2.calcHist([img],[1],None,[256],[0,256])
# hist_red = cv2.calcHist([img],[2],None,[256],[0,256])
# hist_bgr = [hist_blue, hist_green, hist_red]
# col = ["b","g","r"]
# for i in hist_bgr:
#     plt.plot(i, color="")
#     plt.xlim([0,256])
# plt.show()