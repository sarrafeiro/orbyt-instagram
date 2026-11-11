import sys, glob
from PIL import Image
pasta, out = sys.argv[1], sys.argv[2]
fs = sorted(glob.glob(pasta+'/[0-9][0-9].png')) or sorted(glob.glob(pasta+'/*.png'))
ims = [Image.open(f).convert('RGB') for f in fs]
w = 270; h = int(ims[0].height*w/ims[0].width)
cols = min(5, len(ims)); rows = (len(ims)+cols-1)//cols
sheet = Image.new('RGB', (cols*w+(cols+1)*8, rows*h+(rows+1)*8), (120,120,120))
for k, im in enumerate(ims):
    sheet.paste(im.resize((w,h)), (8+(k%cols)*(w+8), 8+(k//cols)*(h+8)))
sheet.save(out, quality=88)
