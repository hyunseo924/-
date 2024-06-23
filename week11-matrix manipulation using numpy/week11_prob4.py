#4
import numpy as np
import struct
import matplotlib.pyplot as plt
class bin_img_processing:
    def __init__(self,fn):   
        #4-a
        with open(fn,'rb') as f:
            chunk=f.read(4)
            header_signeature=struct.unpack('<i',chunk)[0]
            chunk=f.read(2)
            row_size=struct.unpack('<h',chunk)[0]
            chunk=f.read(2)
            column_size=struct.unpack('<h',chunk)[0]
            chunk=f.read(4)
            size_per_pixel=struct.unpack('<i',chunk)[0]
            #Data 읽기
            data=np.zeros((row_size,column_size))
            for rr in range(row_size):
                for cc in range(column_size):
                    chunk=f.read(size_per_pixel)
                    data[rr,cc]=struct.unpack('<i',chunk)[0]
            #footer 읽기
            chunk=f.read(4)
            footer=struct.unpack('<i',chunk)[0]
            print(f"header_singeature: {header_signeature}\nrow size: {row_size}\ncolunm size: {column_size}\nsize per pixel: {size_per_pixel}\n\n")
            print(f"data:\n{data}\nfooter:\n{footer}")
        #4-b
        self.header_signeature=header_signeature
        self.row_size=row_size
        self.column_size=column_size
        self.data=data
        self.size_per_pixel=size_per_pixel
        self.footer=footer

    #4-c
    def Display_image(self):
        plt.figure()
        plt.title('Display image')
        plt.axis('off')
        plt.imshow(self.data, cmap='gray')
        plt.show()
        plt.close()
            
    def Show_array(self):
        print(f"data:\n{self.data}")
        
    def Normalize_pixel(self):
        min_value=np.min(self.data)
        max_value=np.max(self.data)
        new_data=np.zeros(self.data.shape)
        new_data=np.where(True,(self.data-min_value)/(max_value-min_value),0)
        self.new_data=new_data
        plt.figure()
        plt.title('Normalized Image')
        plt.axis('off')
        plt.imshow(self.new_data,cmap='gray',)
        plt.show()
        plt.close()
    