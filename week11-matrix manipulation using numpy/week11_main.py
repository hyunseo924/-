import numpy as np
#1번
#a
A=np.array([[1,2,3],[4,5,6],[7,8,9]])
#b
print("#b \nsize:{0} \ndata type: {1} \nnumber of bytes: {2}".format(A.size,A.dtype,A.size*A.itemsize))
#c
print("#c value of center element: {}".format(A[1][1]))
#d
print("#d",A[:,A.shape[1]-1])
#e
print("#e",A[A.shape[0]-1,:])
#f
print("#f")
#A2=A[A.shape[0]-1,:]
#A2[0]=777
"""slicing never creates a new space in a memory"""
A2=A[-1].copy()
print(f"A2:\n{A2}")
A2[0]=777
print("A:\n{0} \nA2:\n{1}".format(A,A2))
#g
print("#g")
A=np.append(A,[[10,11,12]],0)
print(A)
#h
print("#h")
# B=A[0:3][0:2]
# B[0]=777
# print("A:\n{0} \nB: \n{1}".format(A,B))
"""slicing never creates a new space in a memory"""
B=A[0:3,0:2].copy()
B[0]=777
print("A:\n{0} \nB: \n{1}".format(A,B))
#i
C=np.random.rand(8,8)
C *= 255
C=C.astype(np.uint8)
print("#i\n",C)
#j
print("#j\nshape: {0}, max: {1} min: {2}".format(C.shape,np.max(C),np.min(C)))
#k
D=np.zeros(C.shape)
print(f"#k\n D:\n{D}")
#l
idx=np.where(C>=128)
D[idx]=C[idx]
print(f"#l\nD:\n{D}")
#m
D= np.where(C>=128,C,0.0)
print(f"#m\nD:\n{D}")
#%%
#2
#a
v2=np.array([[3,5,-2],[5,-1,0],[2,4,-3]])
u2=np.where(v2>0,v2,0)
print(f"#2-a\nu2: \n{u2}")
#b
def thres(v2,standard_value=0):
    return np.where(v2>standard_value,v2,0)
print(f"#2-b,c \n{thres(v2,0)}")
#%%
#3-a
from PIL import Image
import matplotlib.pyplot as plt
img=Image.open('chest_xray.jpg')
ori_image=np.array(img)
print(f"size:{ori_image.size}\nmin value:{np.min(ori_image)}\nmax value:{np.max(ori_image)}")
rev_image=np.zeros(ori_image.shape)
rev_image=np.where(True,np.max(ori_image)-ori_image,0)
#다른 방법
#idx=np.nonzero(rev_image+1)
#rev_image[idx]=np.max(ori_image)-ori_image[idx]
#3-b
thres_image=np.zeros(ori_image.shape)
thres_image=thres(ori_image,np.mean(ori_image))
#검증
# index=np.where(ori_image<np.mean(ori_image))
# index1=np.where(thres_image==0)
# if np.array_equal(index, index1):
#     if np.array_equal(ori_image[np.where(ori_image>np.mean(ori_image))],thres_image[thres_image!=0]):
#         print("Yes")
#     else: print("no")
# else: print("NO")
plt.subplot(3,1,1)
plt.title('Original Image')
plt.imshow(ori_image, cmap ='gray')
plt.axis('off')
plt.subplot(3, 1, 2)
plt.title('Reversed Image')
plt.imshow(rev_image, cmap='gray')
plt.axis('off')
plt.subplot(3, 1, 3)
plt.title('Thresholded Image')
plt.imshow(thres_image, cmap='gray')
plt.axis('off')

plt.tight_layout()  #레이아웃 자동 조정
plt.show()
#%%
#4
import struct
from week11_prob4 import bin_img_processing    
#4-d
from week11_prob4 import bin_img_processing 
A=bin_img_processing('cat.bin')
A.Display_image()
A.Show_array()
A.Normalize_pixel()
with open('normalized image.bin','wb') as f:
    #[nr,cc] = A.new_data.shape
    for rr in A.new_data:
        for cc in rr:
            bdata = struct.pack('<f',cc)
            f.write(bdata)
#%%