import cv2
import os

# 1つ目の画像フォルダのパス
folder1_path = 'C:/Users/****/Desktop/Image_Check/hikaku1/'
# 2つ目の画像フォルダのパス
folder2_path = 'C:/Users/****/Desktop/Image_Check/hikaku2/'
# 差分画像の保存先
result_path = 'C:/Users/****/Desktop/Image_Check/kekka/'

# フォルダ内の画像のリストを取得
images1 = [f for f in os.listdir(folder1_path) if f.endswith('.jpg')]
images2 = [f for f in os.listdir(folder2_path) if f.endswith('.jpg')]

# 同名の画像が両方のフォルダにあるかチェック
for image in images1:
    if image in images2:
        # 2つの画像を読み込み
        img1 = cv2.imread(folder1_path + image)
        img2 = cv2.imread(folder2_path + image)

        # 画像の差分を計算
        diff = cv2.absdiff(img1, img2)
        
        # 差分をグレースケールに変換
        diff_gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

        # 閾値処理を行い、差分部分を抽出
        threshold = cv2.threshold(diff_gray, 0, 255, cv2.THRESH_BINARY)[1]

        # 結果を保存または表示
        cv2.imshow('diff', threshold)
        cv2.imwrite(result_path + image , threshold)
