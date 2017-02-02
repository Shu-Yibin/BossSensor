# -*- coding:utf-8 -*-
#import sys
#sys.path.append('/usr/local/Cellar/opencv3/3.2.0/lib/python2.7/site-packages')

import cv2

from boss_train import Model
from image_show import show_image


if __name__ == '__main__':
    
    i = 1
    j = 1
    
    cap = cv2.VideoCapture(0)
    cascade_path = "/Users/ABin/anaconda/pkgs/opencv3-3.1.0-py35_0/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
    model = Model()
    model.load()
    while True:
        _, frame = cap.read()
        # show the result
        cv2.imshow('Sensor',frame)
        # グレースケール変換
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # カスケード分類器の特徴量を取得する
        cascade = cv2.CascadeClassifier(cascade_path)

        # 物体認識（顔認識）の実行
        facerect = cascade.detectMultiScale(frame_gray, scaleFactor=1.2, minNeighbors=3, minSize=(10, 10))
        #facerect = cascade.detectMultiScale(frame_gray, scaleFactor=1.01, minNeighbors=3, minSize=(3, 3))
        if len(facerect) > 0:
            print('face detected')
            color = (255, 255, 255)  # 白
            for rect in facerect:
                # 検出した顔を囲む矩形の作成

                x, y = rect[0:2]
                width, height = rect[2:4]
                
                image = frame[y - 10: y + height, x: x + width]
                
                key = cv2.waitKey(10)
                if key == ord('b'):     # 当按下"s"键时，将保存当前画面
                    i_str = str(i)
                    i = i+1
                    filepath = './data/boss/screenshot'+i_str+'.jpg'
                    cv2.imwrite(filepath, image)
                elif key == ord('o'):     # 当按下"s"键时，将保存当前画面
                    j_str = str(j)
                    j = j+1
                    filepath = './data/other/screenshot'+j_str+'.jpg'
                    cv2.imwrite(filepath, image)
                result = model.predict(image)
                print(result)
                if result == 0:  # boss
                    print('Boss is approaching')
                    #color = (255, 0, 0)
 #                   show_image()
                else:
                    color = (255, 255, 255)  # 白
                    print('Not boss')
                cv2.rectangle(frame, tuple(rect[0:2]), tuple(rect[0:2] + rect[2:4]), color, thickness=2)
                # show the result
                cv2.imshow('Sensor',frame)
        key = cv2.waitKey(10)
        
        if key == ord('q'):   # 当按下"q"键时，将退出循环
            break
                



        #10msecキー入力待ち
        k = cv2.waitKey(100)
        #Escキーを押されたら終了
        if k == 27:
            break

    #キャプチャを終了
    cap.release()
    cv2.destroyAllWindows()
