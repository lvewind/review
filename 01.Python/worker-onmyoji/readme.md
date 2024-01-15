1.目录结构

Hiworker

    app 应用实现
        click  游戏内的点击操作
        data    程序内部数据定义
        detect  游戏内检测
        get_client_data     游戏数据ocr
        play    游戏玩法逻辑
        scheduler   游戏任务调度
        signal  程序信号定义
        view    程序界面
        __init__.py
        main.py 主程序
        start.py    程序初始化
    bin 可执行文件目录
    build 编译缓存
    config 应用配置目录
    data 应用数据
        backup  备份目录(用于安卓模拟器)
        coordinate  游戏坐标数据
        image   游戏截图
        log 日志
        net 深度学习网络
        user    数据库以及用户定义的游戏内数据
    dist 编译结果
    hiworker 框架
        capture     截图模块
        darknet     深度学习模块
        data    数据处理模块
        db  数据库封装
        emulator    模拟器控制模块
        image_detection 图像目标检测模块
        json    JSON文件扩展模块
        ocr     光学识别模块
        random  随机库封装
        sandbox 沙箱控制模块
        signal  框架信号
        storage 数据存取模块
        table_widget    表格操作模块
        text_to_speech 语音合成模块
        thread  多线程拓展
        ui  框架常用UI
        win32   windows系统相关操作模块
        wmi 系统网络模块
    test 测试文件夹
    tools 开发辅助工具
    Build.py 编译脚本
    Launch.py 程序入口文件
    Pipfile 库管理文件
    Pipfile.lock 依赖管理文件
    version.txt windows版本号文件
    


    
        
