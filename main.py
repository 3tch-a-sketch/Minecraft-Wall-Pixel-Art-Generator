import pil


gravel = (142, 137, 136) # RGB
sand = (210, 204, 148)

start = cv2.imread("test.png")


cv2.imshow("start", cv2.resize(start,(0,0), fx=3,fy=3))
cv2.waitKey(0)
cv2.destroyAllWindows()