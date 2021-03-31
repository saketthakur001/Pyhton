from moviepy.editor import *

clip = VideoFileClip(r'D:\naruto\TEST.mp4')

# clip = clip.subclip(0, 15)

# clip = clip.cutout(3, 10)

# clip.ipython_display(width = 360)

# getting only first 5 seconds 
clip = clip.subclip(0, 5) 
    
# getting only first 5 seconds  
clip = clip.subclip(0, 10)  
  
# cutting out some part from the clip 
clip = clip.cutout(3, 7) 
  
# showing  clip  
clip.ipython_display(width = 360)  