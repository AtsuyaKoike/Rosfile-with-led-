# Rosfile-with-led-

# 概要
ROSを使用したLED点滅プログラム

# デモ

# 環境
- Raspberry Pi B 3
 - Ubuntu 16.04
 - イメージファイル(ここの2番目)　https://b.ueda.tech/?post=20180617_raspi_ubuntu

# 環境構築
## コマンド入力
```
$ cd
$ mkdir -p catkin_ws/src
$ cd ~/catkin_ws/src
$ catkin_init_workspace 
Creating symlink "/home/ubuntu/catkin_ws/src/CMakeLists.txt" pointing to "/opt/ros/kinetic/share/catkin/cmake/toplevel.cmake"
$ ls
CMakeLists.txt
```
## bashrcに追記
```
source ~/catkin_ws/devel/setup.bash
export ROS_MASTER_URI=http://localhost:11311
export ROS_HOSTNAME=localhost
```
## 環境のビルド
```
$ cd ~/catkin_ws
$ catkin_make
$ source ~/.bashrc
```
## 確認
````
$ echo $ROS_PACKAGE_PATH
/home/ubuntu/catkin_ws/src:/opt/ros/kinetic/share
```

## 使用GPIOポート
GPIO4, 18, 17, 27, 22, 23, 24, 25

## クローン
```
$ git clone https://github.com/AtsuyaKoike/Ros_LEDlight
$ ./preprocessing.sh
$ cd
$ git clone https://github.com/AtsuyaKoike/Rosfile-with-led-
$ cd catkin_ws/src/
```
## 実行
```
↓新しくスクリーンを立ち上げて命令
$ roscore
↓新しくスクリーンを立ち上げて命令
$ cd Ros_LEDlight/scripts
↓新しくスクリーンを立ち上げて命令
$ rosrun ros_ledlight count.py
↓新しくスクリーンを立ち上げて命令
$ rostopic echo /cout_up
↓新しくスクリーンを立ち上げて命令
$ rosrun ros_ledlight led.py
↓（終了時)新しくスクリーンを立ち上げて命令
キーボード入力：ctrl + c
$ cd Ros_LEDlight
$ ./post_processing.sh
```

# ライセンス
このリポジトリはGPLv3ライセンスです。
