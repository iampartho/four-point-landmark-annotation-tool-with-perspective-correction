import os
import cv2
import shutil
import numpy as np

folder_name = './annotated_files'
dest_folder = "./finalized"
all_files = os.listdir(folder_name)
img_folder = './train_val'
os.makedirs(dest_folder, exist_ok=True)
terminate_flag = False

for each_file in all_files:
	if each_file.endswith(".jpg") or each_file.endswith(".png"):
		img = cv2.imread(f"{folder_name}/{each_file}")
		h,w,_ = img.shape
		txt_file = each_file.split('.')[0]+".txt"
		with open(f'{folder_name}/{txt_file}', 'r') as f:
		    points = f.read().splitlines()
		    pts1 = [[int(float(each.strip().split()[0])*w), int(float(each.strip().split()[1])*h)] for each in points]
		    pts1 = np.float32(pts1)
		pts2 = np.float32([[0,0],[w-1, 0], [w-1, h-1],[0, h-1]])

		# Apply Perspective Transform Algorithm
		matrix = cv2.getPerspectiveTransform(pts1, pts2)
		result = cv2.warpPerspective(img, matrix, (w, h))
		result = cv2.resize(result, (500,500))
		while True:
			cv2.imshow(each_file, result)
			k = cv2.waitKey(1)
			if k == ord('n'):
				shutil.move(f"{folder_name}/{each_file}", f"{dest_folder}/{each_file}")
				shutil.move(f"{folder_name}/{txt_file}", f"{dest_folder}/{txt_file}")
				cv2.destroyAllWindows()
				break
				
			elif k == ord('r'):
				shutil.move(f"{folder_name}/{each_file}", f"{img_folder}/{each_file}")
				shutil.move(f"{folder_name}/{txt_file}", f"{img_folder}/{txt_file}")
				cv2.destroyAllWindows()
				break
			elif k == ord('e'):
				cv2.destroyAllWindows()
				terminate_flag = True
				break
	elif terminate_flag:
		break
	else:
		continue



