# ltepi
LTEPiを利用するためのPythonライブラリです。

# LTEPiとは
RaspberryPi B+やRaspberryPi 2 Model Bに取り付けが可能なLTE通信モジュールを搭載した基板です。

![LTEPi on RPiB+](http://lte4iot.com/wp-content/uploads/2015/05/LTEPi01.png)

# 対応OS
Raspbian

# インストール方法
[ltepi-setup](https://github.com/Robotma-com/ltepi-setup)とともにインストールする必要があります。以下のコマンドを入力すると、ltepi-setupとともにこのモジュールもインストールされます。
Raspberry Piをインターネットに接続できる状態にして実行してください。

```
$ curl https://raw.githubusercontent.com/Robotma-com/ltepi-setup/master/setup | sudo bash
```

# モジュールリリース時の注意
1. [`setup`](setup)内の`VERSION=`にあるバージョンを修正してコミットする
1. 履歴を追記、修正してコミットする

# 履歴
* 0.9.5
  - GitHub公開
  - License情報追加
  - インストールスクリプトを追加
  - 0.9.4と実行コードは同一となっており、特に違いはありません

* 0.9.4
  - 初版、lte4iot.comにて公開
