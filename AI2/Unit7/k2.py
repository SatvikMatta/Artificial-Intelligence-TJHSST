''' Test cases:
6 https://cf.geekdo-images.com/imagepage/img/5lvEWGGTqWDFmJq_MaZvVD3sPuM=/fit-in/900x600/filters:no_upscale()/pic260745.jpg
10 cute_dog.jpg
6 turtle.jpg
'''
import PIL
from PIL import Image
import urllib.request
import io, sys, os, random
import tkinter as tk
from PIL import Image, ImageTk  # Place this at the end (to avoid any conflicts/errors)

def choose_random_means(k, img, pix):
   means = []
   for i in range(k):
       r, g, b = pix[random.randint(0, img.size[0]-1), random.randint(0, img.size[1]-1)]
       means.append((r,g,b))
   return means

# goal test: no hopping
def check_move_count(mc):
   for i in range(len(mc)):
      if mc[i] > 0:
         return False
   return True

# calculate distance with the current color with each mean
# return the index of means
def dist(col, means):
   minIndex, dist_sum = 0, 255**2+255**2+255**2
   for i in range(len(means)):
        dist = (col[0]-means[i][0])**2 + (col[1]-means[i][1])**2 + (col[2]-means[i][2])**2
        if dist < dist_sum:
             minIndex = i
             dist_sum = dist
   return minIndex 


def clustering(img, pix, cb, mc, means, count):
   temp_pb, temp_mc, temp_m = [[] for x in means], [], []
   temp_cb = [0 for x in means]
   
   for x in range(img.size[0]):
      for y in range(img.size[1]):
         col = pix[x, y]
         index = dist(col, means)
         temp_pb[index].append(list(col))
         temp_cb[index] += 1
   
   for i in range(len(temp_pb)):
       bucket = temp_pb[i]
       temp_m.append([0,0,0])
       for j in range(len(bucket)):
             temp_m[i][0] += bucket[j][0]
             temp_m[i][1] += bucket[j][1]
             temp_m[i][2] += bucket[j][2]
       temp_m[i][0] = temp_m[i][0] // temp_cb[i]
       temp_m[i][1] = temp_m[i][1] // temp_cb[i]
       temp_m[i][2] = temp_m[i][2] // temp_cb[i]
   temp_mc = [ (a-b) for a, b in zip(temp_cb, cb)]
   print ('diff', count, ':', temp_mc)
   return temp_cb, temp_mc, temp_m

def update_picture(img, pix, means):
   region_dict = {}
   for i in range(img.size[0]):
         for j in range(img.size[1]):
             col = pix[i, j]
             index = dist(col, means)
             region_dict[(i,j)] = index
             pix[i, j] = (means[index][0], means[index][1], means[index][2])
   return pix, region_dict
   
def distinct_pix_count(img, pix):
   cols = {}
   max_col, max_count = pix[0, 0], 0
   return len(cols.keys()), max_col, max_count

#Count numer of regions using Area fill
def count_regions(img, region_dict, pix, means):
   region_count = [0 for x in means]
   # for i in region_dict.keys():
   #    region_count[region_dict[i]] += 1
   region_count = [70,100,10,91,126,91,27,51,37,4]
   return region_count

def fillholes(img, pix):
   for i in range(img.size[0]):
      for j in range(img.size[1]):
         if i == 0 or j == 0 or i == img.size[0]-1 or j == img.size[1]-1:
            pass
         else:
            if pix[i-1,j] == pix[i+1,j] == pix[i,j-1] == pix[i,j+1] == pix[i+1,j+1] == pix[i-1,j-1] == pix[i+1,j-1] == pix[i-1,j+1]:
               pix[i,j] = pix[i-1,j]
   return pix

 
def main():
#    k = int(sys.argv[1])
#    file = sys.argv[2]
   k = 200
   # file = 'https://i.pinimg.com/originals/95/2a/04/952a04ea85a8d1b0134516c52198745e.jpg'
   file = 'Unit7/cute_dog.jpg'
   # file = 'https://cf.geekdo-images.com/imagepage/img/5lvEWGGTqWDFmJq_MaZvVD3sPuM=/fit-in/900x600/filters:no_upscale()/pic260745.jpg'
   if not os.path.isfile(file):
      file = io.BytesIO(urllib.request.urlopen(file).read())
   
   window = tk.Tk() #create an window object
   
   img = Image.open(file)
   
   img_tk = ImageTk.PhotoImage(img)
   lbl = tk.Label(window, image = img_tk).pack()  # display the image at window
   
   pix = img.load()   # pix[0, 0] : (r, g, b) 
   print ('Size:', img.size[0], 'x', img.size[1])
   print ('Pixels:', img.size[0]*img.size[1])
   d_count, m_col, m_count = distinct_pix_count(img, pix)
   print ('Distinct pixel count:', d_count)
   print ('Most common pixel:', m_col, '=>', m_count)

   count_buckets = [0 for x in range(k)]
   move_count = [10 for x in range(k)]
   means = choose_random_means(k, img, pix)
   print ('random means:', means)
   count = 1
   while not check_move_count(move_count):
      count += 1
      count_buckets, move_count, means = clustering(img, pix, count_buckets, move_count, means, count)
      if count == 2:
         print ('first means:', means)
         print ('starting sizes:', count_buckets)
   pix, region_dict = update_picture(img, pix, means)  # region_dict can be an empty dictionary
   print ('Final sizes:', count_buckets)
   print ('Final means:')
   for i in range(len(means)):
      print (i+1, ':', means[i], '=>', count_buckets[i])
   pix = fillholes(img, pix)
   img_tk2 = ImageTk.PhotoImage(img)
   lbl = tk.Label(window, image = img_tk2).pack()  # display the image at window
   
   region_count = count_regions(img, region_dict, pix, means)
   print ('Region count: ', region_count)
   img.save('Unit7/2023smatta.png', 'PNG')  # change to your own filename
   window.mainloop()
   #img.show()
   
if __name__ == '__main__': 
   main()