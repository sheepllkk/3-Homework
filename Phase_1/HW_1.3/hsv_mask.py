import cv2
import numpy as np

def main():
    # 1. 读取图片
    img_path = 'balls.jpg'  
    img = cv2.imread(img_path)
    
    if img is None:
        print("报错：找不到图片，请检查 balls.jpg 是否在当前文件夹！")
        return

    # 2. 将色彩空间从 BGR 转换到 HSV
    hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 3. 定义颜色的 H:色调, S:饱和度, V:明度阈值范围
    # 蓝色的范围比较好定
    lower_blue = np.array([100, 50, 50])
    upper_blue = np.array([130, 255, 255])
    
    # 红色在 HSV 圆柱体中红色跨越了 0 和 180 的边界，所以需要两段
    lower_red1 = np.array([0, 50, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([160, 50, 50])
    upper_red2 = np.array([180, 255, 255])

    # 4. 根据阈值提取二值化掩膜 
    # cv2.inRange 会把在范围内的颜色变成纯白，范围外的变成纯黑
    mask_blue = cv2.inRange(hsv_img, lower_blue, upper_blue)
    
    # 把两段红色的掩膜加起来
    mask_red1 = cv2.inRange(hsv_img, lower_red1, upper_red1)
    mask_red2 = cv2.inRange(hsv_img, lower_red2, upper_red2)
    mask_red = cv2.bitwise_or(mask_red1, mask_red2)

    # 5. 计算掩膜中白色像素点的总数
    # cv2.countNonZero() 函数用来数有多少个白色的像素点
    blue_pixels = cv2.countNonZero(mask_blue)
    red_pixels = cv2.countNonZero(mask_red)

    # 6. 打印对比结果
    print(f"蓝色球的像素点数量: {blue_pixels}")
    print(f"红色球的像素点数量: {red_pixels}")
    
    if red_pixels > blue_pixels:
        print("结论：图像中【红色球】的占比更大！")
    elif blue_pixels > red_pixels:
        print("结论：图像中【蓝色球】的占比更大！")
    else:
        print("结论：两个球一样大！")

    # 展示黑白掩膜效果
    cv2.imshow('Original Image', img)
    cv2.imshow('Blue Mask', mask_blue)
    cv2.imshow('Red Mask', mask_red)
    print("按键盘上的任意键关闭图片窗口...")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
