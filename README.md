# python
pythonで作成した数学,物理系のgif,mp4動画,およびソースコードです.(2019/11/14最終アップロード)
手元で動かす場合にはnumpy,matplotlibが必要です.また,mp4の出力にはffmpeg,gifの出力にはImageMagickかmatplotlibが必要です.

mp4で出力する場合
```bash
import ffmpeg 
ani.save("hoge.mp4",writer="ffmpeg")
```
gifで出力する場合
```bash
ani.save("hoge.gif",writer="imagemagick")
```
imagemagickがない場合は
```bash
ani.save("hoge.gif",writer="pillow")
```
でもできます.

# 1. dx/dt=sin(x)の初期値による解曲線の変化
```bash
python diff_sin.py
```
 オイラー法によって解を計算しています.
 安定点と不安定点によってジャンプ的な変化をします.
![diff_sin](https://user-images.githubusercontent.com/55901554/68840613-6aba1680-0706-11ea-8228-c47fd5fa15b4.gif)
 
# 2.モンテカルロ法による円周率の算出
```bash
python MonteCarlo.py
```
　機械学習のほうのモンテカルロ法ではないです.プロット数が多い(1000くらい)と実行に時間が20分近くかかりますのでご注意ください.
 
  ![Monte](https://user-images.githubusercontent.com/55901554/68839989-25e1b000-0705-11ea-8ac9-c9219154aa2f.gif)
 
# 3.x^n+y^n=1のnによる変化
```bash
python circle.py
```
　円が長方形に近づいていく様子です.
![circle](https://user-images.githubusercontent.com/55901554/68840700-93daa700-0706-11ea-9e78-6013a5522fb7.gif)

# 4.強誘電体,常誘電体のヒステリシスループ
```bash
python hysteresis.py
```

強誘電体


![hysteresis_fer](https://user-images.githubusercontent.com/55901554/74263745-c1091680-4d42-11ea-8af8-5bf6fd2b1377.gif)


常誘電体

![hysteresis_para](https://user-images.githubusercontent.com/55901554/74263806-d8e09a80-4d42-11ea-9ee7-ac259159893d.gif)


　学生実験の発表で使用した,強誘電体と常誘電体のヒステリシスループのシミュレーションです.強誘電体のほうは本来シグモイド関数のような遷移をするので関数の形は厳密に正しくはないです.
 
 
 # 5.確率感染モデルとロジスティック方程式
 ```bash
python MonteCarlo.py
```
隣接している個体に確率で感染するような環境で,その個体数がロジスティック方程式と呼ばれる方程式の解に沿って増加する様子をシミュレーションしています.
 matplotlib,numpy,tqdmが必要です.<br>
 あとでgithub.ioにてp5.jsを使ってwebシミュレーションができるようにする予定...
