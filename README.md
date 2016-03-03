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

# バージョンアップ方法

[ltepi-serviceのバージョンアップ方法](https://github.com/Robotma-com/ltepi-service#バージョンアップ方法)に記載の方法でバージョンアップを行ってください。

# インストール方法

[ltepi-serviceのインストール方法](https://github.com/Robotma-com/ltepi-service#インストール方法)に従ってインストールを行ってください。その際に本モジュールも同時にインストールされます。

# アンインストール方法

[ltepi-serviceのアンインストール方法](https://github.com/Robotma-com/ltepi-service#アンインストール方法)に従ってアンインストールを行ってください。その際に本モジュールも同時にアンインストールされます。

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

# モジュール確認時の注意
```
$ VERSION=このプロジェクトのバージョン
$ LTEPI_SERVICE_VERSION=ltepi-serviceのバージョン
$ cd /tmp
$ mkdir ltepi-${VERSION}; cd ltepi-${VERSION}; tar zxf ~/ltepi-${VERSION}.tgz; cd /tmp
$ mkdir ltepi-service-${LTEPI_SERVICE_VERSION}; cd ltepi-service-${LTEPI_SERVICE_VERSION}
$ tar zxf ~/ltepi-service-${LTEPI_SERVICE_VERSION}.tgz
$ sudo CANDY_RED=0 SRC_DIR=$(pwd) DEBUG=1 ./install.sh
```


# 履歴
* 0.10.0
  - 以下のAPIを追加
    - `unsetSelectsim()` ... SIM優先モードを解除する
    - `getSimSelected()` ... SIM優先モードかどうかを返す

* 0.9.5
  - GitHub公開
  - License情報追加
  - インストールスクリプトとアンインストールスクリプトを追加
  - `getAntenna()`のtypo修正

* 0.9.4
  - 初版、lte4iot.comにて公開
