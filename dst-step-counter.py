import pyembroidery
import sys


# at least one input element is required
if len(sys.argv) != 2:
    print("usage: dst-step-counter address_of_the_dst_file.dst")
    exit()


# decoding the dst file
emb_pattern = pyembroidery.read_dst(sys.argv[1])

print("name: " + emb_pattern.extras["name"])
print("Stich Count: " + emb_pattern.extras["ST"])
print("Color: " + emb_pattern.extras["CO"])
print("+X: " + emb_pattern.extras["+X"])
print("-X: " + emb_pattern.extras["-X"])
print("+Y: " + emb_pattern.extras["+Y"])
print("-Y: " + emb_pattern.extras["-Y"])

stepx_sum = 0
stepy_sum = 0
dirx_sum = 0
diry_sum = 0

for i in  range(0, emb_pattern.count_stitches()):
    stepx_sum += abs(emb_pattern.stitches[i][0])
    stepy_sum += abs(emb_pattern.stitches[i][1])
    if i != 0:
        current_st = emb_pattern.stitches[i][0]
        past_st = emb_pattern.stitches[i - 1][0]
        if current_st == 0:
            current_st = 1
        if past_st == 0:
            past_st = 1
        if (current_st * past_st) < 0:
            dirx_sum += 1

        current_st = emb_pattern.stitches[i][1]
        past_st = emb_pattern.stitches[i - 1][1]
        if current_st == 0:
            current_st = 1
        if past_st == 0:
            past_st = 1
        if (current_st * past_st) < 0:
            diry_sum += 1

print("=================")
print("sum_x: " + str(stepx_sum))
print("sum_y: " + str(stepy_sum))
print("dir_x: " + str(dirx_sum))
print("dir_y: " + str(diry_sum))



