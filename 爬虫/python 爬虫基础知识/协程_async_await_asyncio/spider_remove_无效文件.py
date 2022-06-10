import os

base_path = "F:\\爱套图"

print(len(os.listdir(base_path)))
num = 0
for i in os.listdir(base_path):
    img_dir = os.path.join(base_path,i)
    img_dir = os.listdir(img_dir)
    # for ii in img_dir:
    #     img_path = os.path.join(base_path,i,ii)
    #     if os.path.getsize(img_path) < 500:
    #         os.remove(img_path)
    #         print(img_path)
            # num+=1
    if not img_dir:
        os.rmdir(os.path.join(base_path,i))
        # print(os.path.join(base_path,i))
# print(num)