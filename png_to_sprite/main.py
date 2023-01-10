import imageio.v2 as iio
def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb
img=iio.imread("s.png")
u_offset = 0
v_offset = 0
print("int sprite_name["+str(img.shape[0]*img.shape[1])+"] = {")
for c in img:
    v_offset=0
    for p in c:
        R = p[0]+0
        G = p[1]+0
        B = p[2]+0
        print("0x"+str(rgb_to_hex((R,G,B))+","))
        v_offset+=1
    u_offset+=1
print("};")
print("uLCD.BLIT(3+u, 15+v, "+str(img.shape[1])+", "+str(img.shape[0])+", colors);")
