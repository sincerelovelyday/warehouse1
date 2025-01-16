
import requests

# 文件的 URL
url = 'https://labfile.oss.aliyuncs.com/courses/40544/log.txt'

# 本地保存文件的路径
local_filename = 'D:/桌面/log.txt'

try:
    # 发送 HTTP GET 请求
    response = requests.get(url, stream=True)

    # 检查请求是否成功
    if response.status_code == 200:
        # 打开本地文件，以二进制写入模式
        with open(local_filename, 'wb') as file:
            # 分块下载文件
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  # 过滤掉保持连接的新块
                    file.write(chunk)
        print(f"文件下载成功，保存为 {local_filename}")
    else:
        print(f"请求失败，状态码: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"请求过程中发生错误: {e}")
f1 = open(local_filename)
l1 = f1.readlines()
f1.close()
