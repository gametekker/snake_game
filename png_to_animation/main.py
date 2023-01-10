import imageio.v2 as iio

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

img=iio.imread("s.png")
u_offset = 0
v_offset = 0
samepixels = []
for c in img:
    for p in c:
        R = p[0]+0
        G = p[1]+0
        B = p[2]+0
        samepixels.append(rgb_to_hex((R,G,B)))
pixel = max(set(samepixels), key=samepixels.count)
print("uLCD.filled_rectangle(u, v, u+10, v+10, 0x"+pixel+");")


pixel = max(set(samepixels), key=samepixels.count)
for c in img:
    v_offset=0
    for p in c:
        R = p[0]+0
        G = p[1]+0
        B = p[2]+0
        if(not (str(rgb_to_hex((R, G, B))).__eq__("000000"))
):
            print("uLCD.pixel(u+"+str(u_offset)+", v+"+str(v_offset)+", 0x"+str(rgb_to_hex((R,G,B)))+");")
        v_offset+=1
    u_offset+=1