from PIL import Image
import numpy as np

im = Image.open("puzzle-trouble-hard.jpg")

width, height = im.size

col = 16
row = 16

init_order = []

order = np.array([['0000', '0001', '0002', '0003', '0004', '0005', '0006', '0007', '0008', '0009', '0010', '0011', '0012', '0013', '0014', '0015', '0015'],
                  ['0100', '0101', '0102', '0103', '0104', '0105', '0106', '0107', '0108', '0109', '0110', '0111', '0112', '0113', '0114', '0115', '0115'],
                  ['0200', '0201', '0202', '0203', '0204', '0205', '0206', '0207', '0208', '0209', '0210', '0211', '0212', '0213', '0214', '0215', '0215'],
                  ['0300', '0301', '0302', '0303', '0304', '0305', '0306', '0307', '0308', '0309', '0310', '0311', '0312', '0313', '0314', '0315', '0315'],
                  ['0400', '0401', '0402', '0403', '0404', '0405', '0406', '0407', '0408', '0409', '0410', '0411', '0412', '0413', '0414', '0415', '0415'],
                  ['0500', '0501', '0502', '0503', '0504', '0505', '0506', '0507', '0508', '0509', '0510', '0511', '0512', '0513', '0514', '0515', '0515'],
                  ['0600', '0601', '0602', '0603', '0604', '0605', '0606', '0607', '0608', '0609', '0610', '0611', '0612', '0613', '0614', '0615', '0615'],
                  ['0700', '0701', '0702', '0703', '0704', '0705', '0706', '0707', '0708', '0709', '0710', '0711', '0712', '0713', '0714', '0715', '0715'],
                  ['0800', '0801', '0802', '0803', '0804', '0805', '0806', '0807', '0808', '0809', '0810', '0811', '0812', '0813', '0814', '0815', '0815'],
                  ['0900', '0901', '0902', '0903', '0904', '0905', '0906', '0907', '0908', '0909', '0910', '0911', '0912', '0913', '0914', '0915', '0915'],
                  ['1000', '1001', '1002', '1003', '1004', '1005', '1006', '1007', '1008', '1009', '1010', '1011', '1012', '1013', '1014', '1015', '1015'],
                  ['1100', '1101', '1102', '1103', '1104', '1105', '1106', '1107', '1108', '1109', '1110', '1111', '1112', '1113', '1114', '1115', '1115'],
                  ['1200', '1201', '1202', '1203', '1204', '1205', '1206', '1207', '1208', '1209', '1210', '1211', '1212', '1213', '1214', '1215', '1215'],
                  ['1300', '1301', '1302', '1303', '1304', '1305', '1306', '1307', '1308', '1309', '1310', '1311', '1312', '1313', '1314', '1315', '1315'],
                  ['1400', '1401', '1402', '1403', '1404', '1405', '1406', '1407', '1408', '1409', '1410', '1411', '1412', '1413', '1414', '1415', '1415'],
                  ['1500', '1501', '1502', '1503', '1504', '1505', '1506', '1507', '1508', '1509', '1510', '1511', '1512', '1513', '1514', '1515', '1515']])

def proper(n):
    o = int(n[:2])
    a = int(n[2:])
    return o*16 + a

proper_vec = np.vectorize(proper)

iorder = proper_vec(order)

order = iorder 

# Convert each piece to the HSV color space and calculate average hue
hues = []
for i in range(row):
    for j in range(col):
        piece = im.crop((j*(width/col), i*(height/row), j*(width/col) + (width/col), i*(height/row) + (height/row)))
        piece_hsv = piece.convert('HSV')
        piece_np = np.array(piece_hsv)
        hue_avg = np.mean(piece_np[:,:,0])
        hues.append(("{:02d}".format(i) + "{:02d}".format(j), hue_avg, piece))

# Sort the pieces based on their average hue value
hues_sorted = sorted(hues, key=lambda x: x[1], reverse=True)
#print(hues_sorted[:][:][:][1])

# Reconstruct the final image using the sorted pieces
final_image = Image.new(mode='RGB', size=(col * width // col, row * height // row))

#for idx, hue, piece in hues_sorted:
#    r = idx // col
#    c = idx % col
#    x = c * (width // col)
#    y = r * (height // row)
#    #print(r,c)
#    #final_image.paste(init_order[order[r, c]], (x, y))
#    final_image.paste(piece, (x, y))
import copy
new_order = np.empty((row, col), dtype='<U4')
#new_order = copy.deepcopy(order)
# Iterate through the sorted pieces
for idx, (index, hue, piece) in enumerate(hues_sorted):
    # Calculate the row and column indices for pasting
    r = idx // col
    c = idx % col
    
    # Calculate the x and y coordinates for pasting
    x = c * (im.width // col)
    y = r * (im.height // row)
    
    # Paste the piece onto the final image
    final_image.paste(piece, (x, y))
    #print(index, r, c)
    #print(type(index))
    # Format the index as a string with leading zeros
    index_str = f"{index:04}"
    new_order[r, c] = index_str
    #print(index_str, new_order[r,c])
    #print(new_order)
    # Update the new_order string

print(new_order)


final_image.save('output_sorted_by_hue.png')

