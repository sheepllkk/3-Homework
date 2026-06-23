import os
import argparse
import cv2

def main():
    # 1. 使用 argparse 解析命令行参数,接收外部传入的文件夹路径
    parser = argparse.ArgumentParser(description="这是一个批量读取图片信息的脚本")
    # 定义一个接收路径的参数 --dir
    parser.add_argument("--dir", type=str, required=True, help="请输入图片文件夹的相对或绝对路径")
    args = parser.parse_args()

    folder_path = args.dir
    img_info_dict = {}  # 初始化一个空字典Dict，用来存储图片信息

    # 检查用户输入的文件夹存不存在
    if not os.path.exists(folder_path):
        print(f"报错：找不到文件夹 '{folder_path}'，请检查路径是否正确！")
        return

    # 2. 遍历该文件夹内的所有文件
    for filename in os.listdir(folder_path):
        
        # 3. 条件判断：筛选后缀为 .jpg 或 .png 的图片（lower() 用于不区分大小写）
        if filename.lower().endswith(('.jpg', '.png')):
            # 拼接出图片的完整读取路径
            img_path = os.path.join(folder_path, filename)
            
            # 4. 利用 OpenCV 读取图片
            img = cv2.imread(img_path)
            
            # 防错机制：如果图片损坏或读取失败，跳过这张图
            if img is None:
                continue
                
            # 获取图片的分辨率和通道数
            # OpenCV 中 img.shape 返回的顺序是 (高度, 宽度, 通道数)
            height, width, channels = img.shape
            
            # 用字典Dict存储这张图片的信息
            img_info_dict[filename] = {
                "resolution": f"{width}x{height}",
                "channels": channels
            }

    # 5. 遍历字典并打印结果
    print(f"====== 在 '{folder_path}' 目录下提取的图片信息 ======")
    for name, info in img_info_dict.items():
        print(f"文件名: {name} | 分辨率 (宽 x 高): {info['resolution']} | 通道数: {info['channels']}")

if __name__ == "__main__":
    main()
