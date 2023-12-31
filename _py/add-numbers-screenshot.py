
imgPath = '/Users/sergiogonzalez/Desktop/hipertipo/tools/fontra-docs/images/fontra-workspace_edit-2.png'

w, h = imageSize(imgPath)

c = 196/256, 19/256, 83/256

r = 20

size(w, h)

image(imgPath, (0, 0))

points = {
    '1' : [(588, 410)], # canvas
    '2' : [(778, 750)], # navigation
    '3' : [(618, 750)], # tools
    '4' : [(111, 770), (1282, 770)], # panels
    '5' : [(988, 580)], # contextual menu
}

fill(*c)
font('/Users/sergiogonzalez/Desktop/hipertipo/fonts/roboto-flex/fonts/RobotoFlex[GRAD,XOPQ,XTRA,YOPQ,YTAS,YTDE,YTFI,YTLC,YTUC,opsz,slnt,wdth,wght].ttf')
fontSize(22)

for k, v in points.items():
    for x, y in v:
        oval(x-r, y-r, r*2, r*2)
        with savedState():
            fill(1)
            text(k, (x, y-7), align='center')
            
imgPath2 = imgPath.replace('.png', '_dots.png')
saveImage(imgPath2)
