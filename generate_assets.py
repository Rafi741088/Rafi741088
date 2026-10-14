"""
Generate the animated GitHub profile banner and divider assets.
Dependency: Pillow (pip install Pillow)
Run: python generate_assets.py
"""
from PIL import Image, ImageDraw, ImageFont
import math, os, random

OUT = os.path.join(os.path.dirname(__file__), "assets")
os.makedirs(OUT, exist_ok=True)
W, H, FRAMES = 1600, 400, 36
random.seed(741088)

def get_font(size, bold=False):
    paths = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
    ]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

nodes = [(random.randint(880,1510),random.randint(45,350)) for _ in range(27)]
edges = set()
for i,(x,y) in enumerate(nodes):
    for _,j in sorted((math.hypot(x-x2,y-y2),j) for j,(x2,y2) in enumerate(nodes) if j!=i)[:3]:
        edges.add((min(i,j),max(i,j)))
particles = [(random.uniform(0,W),random.uniform(0,H),random.uniform(1,3),random.random()*math.tau) for _ in range(70)]

def render(fi, static=False):
    t=0 if static else fi/FRAMES
    im=Image.new("RGB",(W,H),"#050816")
    px=im.load()
    for y in range(H):
        for x in range(W):
            g=max(0,1-math.sqrt(((x-1230)/760)**2+((y-200)/330)**2))
            g2=max(0,1-math.sqrt(((x-1490)/430)**2+((y-40)/360)**2))
            px[x,y]=(int(5+6*g+2*g2),int(8+19*g+9*g2),int(22+47*g+28*g2))
    d=ImageDraw.Draw(im,"RGBA")
    for x in range(0,W,48): d.line((x,0,x,H),fill=(40,105,180,22))
    for y in range(0,H,40): d.line((0,y,W,y),fill=(40,105,180,18))
    shade=Image.new("RGBA",(W,H),(0,0,0,0)); sd=ImageDraw.Draw(shade)
    for x in range(900):
        sd.line((x,0,x,H),fill=(5,8,22,int(145*(1-x/900)**1.6)))
    im=Image.alpha_composite(im.convert("RGBA"),shade); d=ImageDraw.Draw(im,"RGBA")
    for a,b in edges:
        x1,y1=nodes[a]; x2,y2=nodes[b]
        d.line((x1,y1,x2,y2),fill=(0,180,255,50))
        if not static:
            p=(t*1.6+a*.137)%1
            x,y=x1+(x2-x1)*p,y1+(y2-y1)*p
            d.ellipse((x-3,y-3,x+3,y+3),fill=(0,225,255,220))
    for i,(x,y) in enumerate(nodes):
        pulse=0 if static else (math.sin(t*math.tau*2+i*.7)+1)/2
        r=2.5+pulse*2.2
        d.ellipse((x-r-5,y-r-5,x+r+5,y+r+5),fill=(0,150,255,20+int(pulse*35)))
        d.ellipse((x-r,y-r,x+r,y+r),fill=(25,205,255,160+int(pulse*80)))
    for x0,y0,s,ph in particles:
        x=(x0+(0 if static else t*90+math.sin(ph+t*math.tau)*18))%W
        y=(y0+(0 if static else math.cos(ph+t*math.tau)*12))%H
        d.ellipse((x-s,y-s,x+s,y+s),fill=(90,220,255,110))
    if not static:
        sx=int((t*1.7%1)*W); d.line((sx,0,sx,H),fill=(0,217,255,50),width=2)
        d.line((sx+2,0,sx+2,H),fill=(0,217,255,15),width=7)
    title=get_font(49,True); sub=get_font(23,True); tag=get_font(20); micro=get_font(13,True)
    d.rounded_rectangle((72,58,280,86),radius=12,fill=(0,217,255,18),outline=(0,217,255,105))
    d.text((87,64),"AI  /  SOFTWARE",font=micro,fill=(72,224,255,245))
    d.text((70,105),"ABIDUR RAHMAN RAFI",font=title,fill=(248,250,252,255))
    d.rounded_rectangle((72,174,690,220),radius=8,fill=(12,24,48,180),outline=(37,99,235,130))
    d.text((91,184),"AI ENGINEER  •  FULL-STACK DEVELOPER",font=sub,fill=(70,220,255,255))
    d.text((73,245),"Building intelligent digital experiences.",font=tag,fill=(194,207,226,245))
    d.rounded_rectangle((72,286,695,289),radius=2,fill=(37,99,235,85))
    sx=72 if static else int(72+(t*1.9%1)*620)
    d.rounded_rectangle((sx,285,min(sx+105,695),290),radius=2,fill=(0,217,255,235))
    cx,cy=1265,200
    for r,a in [(112,50),(82,42),(52,35)]: d.ellipse((cx-r,cy-r,cx+r,cy+r),outline=(0,190,255,a))
    ang=0 if static else t*math.tau
    ox,oy=cx+math.cos(ang)*112,cy+math.sin(ang)*48
    d.ellipse((ox-6,oy-6,ox+6,oy+6),fill=(0,230,255,230))
    d.ellipse((cx-20,cy-20,cx+20,cy+20),fill=(16,80,145,220),outline=(0,217,255,230),width=2)
    d.text((cx-12,cy-12),"AI",font=get_font(16,True),fill=(230,250,255,255))
    d.rounded_rectangle((1320,325,1518,354),radius=10,fill=(5,12,28,200),outline=(0,217,255,85))
    d.ellipse((1333,336,1343,346),fill=(0,220,170,235))
    d.text((1352,333),"BUILDING / LEARNING",font=micro,fill=(190,220,240,235))
    return im.convert("RGB")

render(0,True).save(os.path.join(OUT,"github-banner.png"),optimize=True)
frames=[render(i) for i in range(FRAMES)]
frames[0].save(os.path.join(OUT,"github-banner.gif"),save_all=True,append_images=frames[1:],duration=110,loop=0,optimize=True,disposal=2)
dw,dh=1200,28; div=[]
for i in range(24):
    im=Image.new("RGBA",(dw,dh),(5,8,22,0)); d=ImageDraw.Draw(im,"RGBA")
    d.line((0,dh//2,dw,dh//2),fill=(37,99,235,85),width=1); x=int(i/24*dw)
    for off,a,w in [(-18,25,11),(-8,55,7),(0,220,2),(9,45,5)]:
        d.line((max(0,x+off-75),dh//2,min(dw,x+off+75),dh//2),fill=(0,217,255,a),width=w)
    div.append(im)
div[0].save(os.path.join(OUT,"section-divider.gif"),save_all=True,append_images=div[1:],duration=85,loop=0,optimize=True,disposal=2)
