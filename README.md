# ros2_tutorial

ROS 2（Jazzy）入門練習：一個 `ament_python` 套件，內含最基本的 publisher / subscriber 節點。

這個 repo 是整個 colcon workspace（`src/` 進版控，`build/`、`install/`、`log/` 不進）。

## 內容

| 檔案 | 說明 |
|---|---|
| `src/ros2_tutorial/ros2_tutorial/talker.py` | `talker` 節點：每 0.5 秒在 `chatter` topic 發佈一則 `std_msgs/String`（`Hello, world! N`） |
| `src/ros2_tutorial/ros2_tutorial/listener.py` | `listener` 節點：訂閱 `chatter` 並把收到的訊息印到 log |
| `src/ros2_tutorial/package.xml` / `setup.py` | 套件描述；相依 `rclpy`、`std_msgs` |
| `src/ros2_tutorial/test/` | ament 產生的 copyright / flake8 / pep257 測試 |

## 建置與執行

```bash
source /opt/ros/jazzy/setup.bash
colcon build --symlink-install
source install/setup.bash

# 終端機 1
ros2 run ros2_tutorial talker

# 終端機 2（listener 尚未加進 setup.py 的 entry_points，先直接用模組執行）
python3 -m ros2_tutorial.listener
```

要讓 `ros2 run ros2_tutorial listener` 可用，在 `setup.py` 的 `console_scripts` 加上
`'listener = ros2_tutorial.listener:main'` 後重新 `colcon build`。
