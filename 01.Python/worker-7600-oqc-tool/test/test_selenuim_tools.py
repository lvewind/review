from msedge.selenium_tools import Edge, EdgeOptions
import os
import time

if __name__ == '__main__':
    cwd = os.getcwd()
    print(cwd)
    # 上文第2步解压驱动所在绝对路径
    driver_url = os.path.join(os.path.abspath(os.getcwd()), "../bin", "msedgedriver.exe")
    print(driver_url)
    options = EdgeOptions()
    # 使用谷歌内核
    options.use_chromium = True
    # 浏览器可执行文件绝对路径 - 手动指定使用的浏览器位置
    # options.binary_location = r"C:\Users\lenovo\AppData\Local\Microsoft\Edge SxS\Application\msedge.exe"
    # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
    # options.add_argument("--headless")
    # 谷歌文档提到需要加上这个属性来规避bug
    # options.add_argument("disable-gpu")
    # 隐私模式
    # options.add_argument("-inprivate")
    # 如果上文2步设置了环境变量可不传executable_path，port：驱动默认端口号，可不传
    browser = Edge(executable_path=driver_url, options=options)
    browser.get("https://www.runoob.com/")
    # 保存截图到项目相对路径
    browser.save_screenshot('bing.png')
    el = browser.find_element_by_id("cate10")
    print(el.text)
    browser.get("https://www.bing.com/")
    time.sleep(10)

    # print('done')

