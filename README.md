# camera4
#　gamma_camera.py

トラックバーから返ってくる値によってgammaの値が変わり,gammaとルックアップテーブルを用いてガンマ変換を行った.

    createTrackbarでトラックバーを作る.

    gamma = cv2.getTrackbarPos("gamma", "title") * 0.1 #トラックバーから値を得る
        if gamma == 0:#0の時は強制的に0.1にする
            gamma = 0.1
            cv2.setTrackbarPos("gamma", "title", 1) #トラックバーの位置を決める
    
    # ガンマ補正用ルックアップテーブル
    look_up_table = np.zeros((256, 1), dtype = 'uint8')
    for i in range(len(look_up_table)):
        look_up_table[i][0] = (len(look_up_table)-1) * pow(float(i) / (len(look_up_table)-1), 1.0 / gamma)
    
    # ルックアップテーブルによるガンマ補正
    gamma_correction_image = cv2.LUT(frame, look_up_table)

・使い方
ウィンドウ上部のトラックバーを変えることによって明るさを調整する.

・依存ライブラリ
numpy, opencv

・バージョン
python3.6

・参考文献 
https://qiita.com/Kazuhito/items/c43e96ab16f400a35721

プログラムの
#ガンマ値設定用のトラックバーを用意
から
gamma_correction_image = cv2.LUT(frame, look_up_table)
まで引用

・リンク
https://youtu.be/aRB0xBi0G8c

#　filter_camera.py
    
平均値フィルタを用いて,取得した動画をぼかす.平均値フィルタに用いる値はトラックバーから受け取るものとする.

    cv2.createTrackbar("filter", "title", 1, 50, myfunc)    #トラックバーの動く範囲を１から5０にする
    fil = cv2.getTrackbarPos("filter", "title") #トラックバーから値を受け取る
    
    blur = cv2.blur(frame,(fil,fil)) #平均値フィルタを用いる
・使い方
ウィンドウ上部のトラックバーを変えることによって画面をぼかす.

・依存ライブラリ
numpy, opencv

・バージョン
python3.6

・参考文献
http://labs.eecs.tottori-u.ac.jp/sd/Member/oyamada/OpenCV/html/py_tutorials/py_imgproc/py_filtering/py_filtering.html

平均の
blur = cv2.blur(img,(5,5))
の文を引用

・リンク

#　color_camera.py

トラックバーの値によって色空間が変わる処理を実装した.

    v2.createTrackbar("v", "title", 0, 10, myfunc) #トラックバーの動く範囲を０から１０にする
    v = cv2.getTrackbarPos("v", "title")    #トラックバーから値を受け取る
    
    if(v==0):
        i = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #BGR空間からGRAY空間へ変換
    elif(v==1):
        i = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  #BGR空間からHSV空間へ変換
    elif(v==2):
        i = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)  #RGB空間からHSV空間へ変換
    elif(v==3):
        i = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)  #BGR空間からHLS空間へ変換
    elif(v==4):
        i = cv2.cvtColor(frame, cv2.COLOR_RGB2HLS)  #RGB空間からHLS空間へ変換
    elif(v==5):
        i = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA) #BGR空間からBGRA空間へ変換
    elif(v==6):
        i = cv2.cvtColor(frame, cv2.COLOR_RGB2BGRA) #RGB空間からBGRA空間へ変換
    elif(v==7):
        i = cv2.cvtColor(frame, cv2.COLOR_RGB2Luv)  #RGB空間からLuv空間へ変換
    elif(v==8):
        i = cv2.cvtColor(frame, cv2.COLOR_RGB2Lab)  #RGB空間からLab空間へ変換
    elif(v==9):
        i = cv2.cvtColor(frame, cv2.COLOR_RGB2XYZ)  #RGB空間からXYZ空間へ変換
    elif(v==10):
        i = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY) #RGB空間からGRAY空間へ変換
    
・使い方
ウィンドウ上部のトラックバーを変えることによって,各色空間に切り替わる
・依存ライブラリ
numpy, opencv

・バージョン
python3.6

・参考文献
http://imagingsolution.blog.fc2.com/blog-entry-242.html

各変換式を引用

・リンク
