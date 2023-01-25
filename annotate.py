import os
import cv2
import shutil
import numpy as np

def on_mouse(event, x, y, flags, param):
    global ix, iy, lx, ly, rx, ry, cx, cy, points, flag
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points)<4:
            
            ix, iy = x, y
            save_x, save_y = float(x/500), float(y/500)
            points.append((save_x,save_y))
            flag = True
    elif event == cv2.EVENT_RBUTTONDOWN:
        if len(points)>0:
            points.pop()
            flag = False
    elif event == cv2.EVENT_MOUSEMOVE:
        if flag:
            cx, cy = x, y

def main(path):
    global ix, iy, lx, ly, rx, ry, cx, cy, points, flag
    ix, iy, lx, ly, rx, ry, cx, cy = -1, -1, -1, -1, -1, -1, -1, -1
    points = []
    flag = False
    terminate_flag = False
    os.makedirs('./annotated_files', exist_ok=True)
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", on_mouse)

    for file in os.listdir(path):
        if terminate_flag:
            break
        if file.endswith(".jpg") or file.endswith(".png"):
            img = cv2.imread(os.path.join(path, file))
            img = cv2.resize(img, (500,500))
            annotation_file = os.path.join(path, file.split(".")[0]+".txt")
            if os.path.exists(annotation_file):
                with open(annotation_file, 'r') as f:
                    points = [tuple(map(float, line.strip().split())) for line in f]
            while True:
                for point in points:
                    point = (int(point[0]*500), int(point[1]*500))
                    cv2.circle(img, point, 3, (0,0,255), -1)
                    
                if flag:
                    point = (int(point[0]*500), int(point[1]*500))
                    cv2.circle(img, (cx,cy), 3, (0,0,255), -1)
                cv2.imshow("image", img)
                k = cv2.waitKey(1)
                if k == ord('s'):
                    with open(annotation_file, 'w') as f:
                        if len(points) != 4:
                            continue

                        for point in points:
                            f.write(f"{point[0]} {point[1]}\n")
                    txt_filename = file.split(".")[0]+".txt"

                    shutil.move(annotation_file, f"./annotated_files/{txt_filename}")
                    shutil.move(os.path.join(path, file), f"./annotated_files/{file}")
                    points=[]
                    break
                elif k == ord('e'):
                    cv2.destroyAllWindows()
                    terminate_flag = True
                    break
                img = cv2.imread(os.path.join(path, file))
                img = cv2.resize(img, (500,500))
                #points = []
                flag = False
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main("train_val/")
