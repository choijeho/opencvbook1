import cv2

# 이하 교재 부분 - 카메라는 resize 되나, 파일은 resize 안된다고 했음.
# cap = cv2.VideoCapture(0)                   # 카메라 0번 장치 연결
# width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)   # 프레임 폭 값 구하기
# height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # 프레임 높이 값 구하기
# print("Original width: %d, height:%d" % (width, height) ) 
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)      # 프레임 폭을 320으로 설정 
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)     # 프레임 높이를 240으로 설정
# width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)   # 재지정한 프레임 폭 값 구하기
# height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) # 재지정한 프레임 폭 값 구하기
# print("Resized width: %d, height:%d" % (width, height) )
# 이상 교재 부분

# 이하  인터넷 검색 참조 - 파일도 resize 가능함.
video_file='../img/big_buck.avi'
cap=cv2.VideoCapture(video_file)
if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            img=cv2.resize(img, (320, 240))
            cv2.imshow('camera', img)            
            if cv2.waitKey(1) != -1:
                break
        else:
            print('no frame!')
            break
else:
    print("can't open camera!")
cap.release()
cv2.destroyAllWindows()
