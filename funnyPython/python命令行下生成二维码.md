# python命令行下生成二维码

1. 参考文章

   > https://mp.weixin.qq.com/s?__biz=MzAwOTQ4MzY1Nw==&mid=2247486632&idx=1&sn=0461d045f10944613a2b549bdd30c3ca&chksm=9b5fa84eac282158330c75a71b5e004b84f0cd3779205eaabefe0dcb68ab650f8a5f6a2e5b17&mpshare=1&scene=23&srcid=0827BbZ9vDjZ468rjfT7z4xD#rd

2. GitHub仓库地址

   > https://github.com/sylnsfar/qrcode

3. my demo

   ```shell
   >myqr https://github.com/comeCU -p C:\User\Administrator\Desktop\my_github.jpg -n hello.png -d C:\Users\Administrator\Desktop -c
   ```

   注：

   - [-p]  源图片路径
   - [-n]  生成二维码图片命名
   - [-d]  生成二维码图片保存路径
   - [-c]  使产生的二维码图片由黑白变为彩色