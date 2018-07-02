# camera4
gamma_camera.py
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
# ガンマ値設定用のトラックバー用意(小数点を扱えないため、10倍の値で準備)
から
gamma_correction_image = cv2.LUT(frame, look_up_table)
まで引用

・リンク
https://youtu.be/aRB0xBi0G8c

filter_camera.py

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

