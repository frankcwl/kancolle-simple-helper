# kancolle-simple-helper

舰队collection简易自动化脚本

## 功能特性

- 自动点击出击中的阵型、罗盘、可选分歧点，跳过结算、掉落界面
- 添加、查看、修改不同地图的阵型、夜战、撤退配置
- 配置基地航空队
- **大破自动撤退不稳定，强烈建议同时使用[poi](https://github.com/poooi/poi)、[kc3改](https://github.com/KC3Kai/KC3Kai)等砍口垒工具的大破提示**
- **不支持自动反复出击，只支持点击*出击开始*后完成当次出击**

## 使用方法

### 手动安装

1. 调整游戏窗口大小为 1200x720
2. 安装python3.10+，并安装依赖库
    ```bash
    pip install -r requirements.txt
    ```
3. 运行脚本
    ```bash
    python main.py
    ```

### 使用打包好的exe文件

1. 调整游戏窗口大小为 1200x720
2. 从release中下载最新的zip文件并解压
3. 运行`kancolle-simple-helper.exe`