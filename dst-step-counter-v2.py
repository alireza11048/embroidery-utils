import sys 

# at least one input element is required
if len(sys.argv) != 2:
    print("usage: dst-step-counter address_of_the_dst_file.dst")
    exit()


f = open(sys.argv[1], 'rb') 
data = f.read()
hdata = bytearray(data)

res = []
stich_count = 0

i = 0
while i < (len(hdata) - 512):
    resx = 0
    tmpx = hdata[i + 512]
    i += 1
    
    resy = 0
    tmpy = hdata[i + 512]
    i += 1
    
    resc = 0
    tmpc = hdata[i + 512]
    i += 1
    
    if (tmpx  & 0x1) == 1 :
        resx +=1
    if (tmpx & 0x2) == 2 :
        resx -=1
    if (tmpx & 0x4) == 4 :
        resx +=9
    if (tmpx & 0x8) == 8 :
        resx -=9
    if (tmpy & 0x1) == 1 :
        resx +=3
    if (tmpy & 0x2) == 2 :
        resx -=3
    if (tmpy & 0x4) == 4 :
        resx +=27
    if (tmpy & 0x8) == 8 :
        resx -=27
    if (tmpc & 4) == 4 :
        resx +=81
    if (tmpc & 8) == 8 :
        resx -=81
    if (tmpx & 0x10) == 0x10 :
        resy +=9
    if (tmpx & 0x20) == 0x20 :
        resy -=9
    if (tmpx & 0x40) == 0x40 :
        resy +=1
    if (tmpx & 0x80) == 0x80 :
        resy -=1
    if (tmpy & 0x10) == 0x10 :
        resy +=27
    if (tmpy & 0x20) == 0x20 :
        resy -=27
    if (tmpy & 0x40) == 0x40 :
        resy +=3
    if (tmpy & 0x80) == 0x80 :
        resy -=3
    if (tmpc & 0x10) == 0x10 :
        resy +=81
    if (tmpc & 0x20) == 0x20 :
        resy -=81
        
    resc = tmpc & 0xf3
    
    res.append([resx, resy, resc])
    stich_count += 1

stepx_sum = 0
stepy_sum = 0
dirx_sum = 0
diry_sum = 0
for i in  range(0, stich_count):
    stepx_sum += abs(res[i][0])
    stepy_sum += abs(res[i][1])
    if i != 0:
        current_st = res[i][0]
        past_st = res[i - 1][0]
        if current_st == 0:
            current_st = 1
        if past_st == 0:
            past_st = 1
        if (current_st * past_st) < 0:
            dirx_sum += 1

        current_st = res[i][1]
        past_st = res[i - 1][1]
        if current_st == 0:
            current_st = 1
        if past_st == 0:
            past_st = 1
        if (current_st * past_st) < 0:
            diry_sum += 1

print("sum_x: " + str(stepx_sum))
print("sum_y: " + str(stepy_sum))
print("dir_x: " + str(dirx_sum))
print("dir_y: " + str(diry_sum))
f.close()

