import subprocess
import sys

def install_libraries():
    # 需要安装的库列表
    libraries = [
        "requests",
        "pandas",
        "tkinter",  # 通常Python自带，但有些环境可能需要单独安装
        "python-binance",  # 包含binance.client和binance.enums
        "logging"   # Python标准库，通常不需要安装
    ]
    
    # 标准库列表（不需要安装）
    standard_libraries = [
        "collections",
        "time",
        "datetime",
        "os",
        "importlib",
        "math",
        "threading",
        "logging"
    ]
    
    print("开始检查并安装所需库...\n")
    
    # 安装需要的库
    for lib in libraries:
        try:
            # 尝试导入库来检查是否已安装
            __import__(lib)
            print(f"库 '{lib}' 已安装，跳过...")
        except ImportError:
            print(f"库 '{lib}' 未安装，正在安装...")
            # 使用pip安装库
            subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
            print(f"库 '{lib}' 安装完成\n")
    
    # 提示标准库无需安装
    print("\n以下库是Python标准库，无需单独安装：")
    for std_lib in standard_libraries:
        print(f"- {std_lib}")
    
    print("\n所有必要的库检查和安装已完成！")

if __name__ == "__main__":
    install_libraries()
    input("按回车键退出...")
    