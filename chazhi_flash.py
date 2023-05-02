datadir = 'D:/workingscripts/model-HW/predata/LTNGmodel/result/may/result/'
files = [f for f in os.listdir(datadir) if f.endswith('.txt')]
for filename in files:
    tf = open(os.path.join(datadir, filename))
#    print(data)
    lats = []
    lons = []
    vs = []
    for aline in tf:    
        datalist = aline.split()
#    print(datalist)
        lat = float(datalist[2])
#        print(lat)
        lon = float(datalist[3])
#        print(lon)
        v = float(datalist[4])
#        print(v)
        lats.append(lat)
        lons.append(lon)
        vs.append(v)
    lon = array(lons)
    lat = array(lats)  
    v = array(vs)
    glon = arange(108.2, 118, 0.1)
    glat = arange(19.00, 26.40, 0.1)
    ynum=len(glat)
    xnum=len(glon)
    gv = griddata((lon, lat), v, xi=(glon, glat), method='inside_count')[0]
    count=[]
    for i in range(0,ynum):
        for j in range(0,xnum):
            count.append(gv[i,j])  ##每一个格点内出现的次数
    flashes=array(count)
    x0=108.2
    y0=19
    xdelt=0.1
    ydelt=0.1
    area=gridarea(x0,xdelt,ynum,y0,ydelt,xnum,islonlat=True,allcell=False,earth_radius=6371)
    gridsqu=reshape(area,7252)
    singgrid=flashes/gridsqu
#print(singgrid)
    df=DataFrame(singgrid)
#df=DataFrame(gridsqu)
###print(df)
#    df.to_csv('D:/workingscripts/model-HW/predata/LTNGmodel/0529/test00h.csv')
    output_filename = os.path.splitext(filename)[0] + "_processed.csv"
    df.to_csv(os.path.join(datadir, output_filename))
