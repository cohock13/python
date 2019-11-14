# python
pythonで作成した数学,物理系のgif,mp4動画,およびソースコードです.(2019/11/14最終アップロード)
手元で動かす場合にはnumpy,matplotlibが必要です.また,mp4の出力にはffmpeg,gifの出力にはImageMagickが必要です.

ffmpegで出力する場合
```bash
import ffmpeg 
ani.save("hoge.mp4",writer="ffmpeg")
```
gifで出力する場合
```bash
ani.save("hoge.gif",writer="ImageMagick")
```
# 1. dx/dt=sin(x)の初期値による解曲線の変化
```bash
python diff_sin.py
```
 オイラー法によって解を計算しています.
 初期値が安定点と不安定点によってジャンプ的な変化をします.
 
 ![diff_sin](https://user-images.githubusercontent.com/55901554/68840383-fd0dea80-0705-11ea-8ea2-d6da088bb33b.gif)

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
 (gif)
