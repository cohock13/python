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

 初期値が安定点と不安定点によってジャンプ的な変化をします.
(gif)

# 2.モンテカルロ法による円周率の算出
　機械学習のほうのモンテカルロ法ではないです.
 
# 3.x^n+y^n=1のnによる変化
　円が長方形に近づいていく様子です.
 (gif)
