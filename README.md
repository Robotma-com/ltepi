# ltepi

[![GitHub release](https://img.shields.io/github/release/Robotma-com/ltepi.svg)](https://github.com/Robotma-com/ltepi/releases/latest)
[![License BSD3](https://img.shields.io/github/license/Robotma-com/ltepi.svg)](http://opensource.org/licenses/BSD-3-Clause)

LTEPiを利用するためのPythonライブラリです。

# LTEPiって何？
RaspberryPi B+やRaspberryPi 2 Model Bに取り付けが可能なLTE通信モジュールを搭載した基板です。

![LTEPi on RPiB+](http://lte4iot.com/wp-content/uploads/2015/05/LTEPi01.png)

# 対応ハードウェア
1. Raspberry Pi B+
1. Raspberry Pi2 Model B

# 対応OS
Raspbian 4.1以降

# インストール方法
[ltepi-service](https://github.com/Robotma-com/ltepi-service)とともにインストールする必要があります。以下のコマンドを入力すると、ltepi-serviceとともにこのモジュールもインストールされます。
Raspberry Piをインターネットに接続できる状態にして実行してください。

```
$ curl https://raw.githubusercontent.com/Robotma-com/ltepi-service/master/install.sh | sudo bash
```

特定のバージョンを利用する場合は、以下のようにバージョンを指定することができます。
```
$ VERSION=2.0.0
$ curl https://raw.githubusercontent.com/Robotma-com/ltepi-service/${VERSION}/install.sh | sudo bash
```

# アンインストール
[ltepi-service](https://github.com/Robotma-com/ltepi-service)とともにアンインストールします。
ホームディレクトリーに移りアンインストールのスクリプトを実施してください。
```
$ cd ~
$ sudo /opt/inn-farm/ltepi/bin/uninstall.sh
```

# Pythonライブラリーの利用
ltepiをimportしてください。

```
import ltepi
telno = ltepi.getTelno()
```

# モジュールリリース時の注意
1. [`install.sh`](install.sh)内の`VERSION=`にあるバージョンを修正してコミットする
1. 履歴を追記、修正してコミットする
1. （もし必要があれば）パッケージング
```
$ ./install.sh pack
```

# 履歴
* 0.9.5
  - GitHub公開
  - License情報追加
  - インストールスクリプトとアンインストールスクリプトを追加
  - `getAntenna()`のtypo修正

* 0.9.4
  - 初版、lte4iot.comにて公開
