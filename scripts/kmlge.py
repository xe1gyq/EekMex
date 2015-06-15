#!/usr/bin/python
 
#~ warning !: the script will draw beachball and creates the kml file to plot them in googleearth. All created element
#~ will be placed in the same directory as the one containing this script. The kml file and the beachballs have to
#~ stay in the same directory.
 
from lxml import etree      #will manage the identation of the kml script
from pykml.factory import KML_ElementMaker as KML #import pykml library
import numpy as np
import datetime as date
 
def beachball(data):
    """function to draw beachball using obspy library"""
    import matplotlib.pyplot as plt
    from obspy.imaging.beachball import Beachball
 
    strike,dip,rake=data[:,9],data[:,10],data[:,11]
    event=data[:,0]                 #index to identify the beachball created
 
    for j in range(len(strike)):
        beach = Beachball([strike[j],dip[j],rake[j]],outfile=str(int(event[j])),\
            facecolor='black',edgecolor='black') #create and save beachball in a outfile in the directory where the .py file is
 
data=np.loadtxt('eekmexprekml.log',\
    skiprows=1) #import your data. (table format: index yyyy mm dd hr mn ss lat lon strike dip rake) the first row isn't used

temperature = data[:,11]
pressure = data[:,10]
altitude = data[:,9]
latitude = data[:,7]
longitude = data[:,8]
yyyy,mm,dd=data[:,3],data[:,2],data[:,1]
hr,mn,ss = data[:,4],data[:,5],data[:,6]
index=data[:,0]
 
#beachball(data)         #call beachball function   --> put in comment this line if you don't want to draw again all beachballs
 
###############################################################################################################################
# create a document element with multiple label style
kmlobj = KML.kml(
    KML.Document(
    )
)  
 
for j in range(len(yyyy)):  #create the ref icons we will use
    kmlobj.Document.append(    
        KML.Style(            
            KML.IconStyle(
                KML.Icon(
                    KML.href('%s.png'%str(int(index[j]))),
                    KML.scale(0.6),   #scale the beachball in googleEarth
                ),
                KML.heading(0.0),
            ),
        id='beach_ball_%i'%j    #gives the icon a ref that will be used later
        ),
    )
 
# add images to the document element
for i in range(len(yyyy)):
    datum = str(date.date(int(yyyy[i]),int(mm[i]),int(dd[i])))
    ev_time = str(date.time(int(hr[i]),int(mn[i]),int(ss[i])))
    alt = str(altitude[i])
    press = str(pressure[i])
    temp = str(temperature[i])
 
    kmlobj.Document.append(
        KML.Placemark(
            #~ KML.name('%s'%str(int(index[i]))),   #uncomment this to add a name to the placemark (will always appear in GoogleEarth)
            KML.ExtendedData(                       #I add information about the earthquake, it appears in a table ('info' : value)
                KML.Data(                          
                    KML.value('%s'%datum),          #add value of the specific info
                name ='date'                        #name of'info' you add.
                ),
                KML.Data(
                    KML.value('%s'%ev_time),        #add value of the specific info
                name ='time'                        #name of 'info' you add.
                ),                                     #more data can be added, following the same structure (line 65-68)
                KML.Data(
                    KML.value('%s'%alt),        #add value of the specific info
                name ='altitude'                        #name of 'info' you add.
                ),                                     #more data can be added, following the same structure (line 65-68)
                KML.Data(
                    KML.value('%s'%press),        #add value of the specific info
                name ='pressure'                        #name of 'info' you add.
                ),                                     #more data can be added, following the same structure (line 65-68)
                KML.Data(
                    KML.value('%s'%temp),        #add value of the specific info
                name ='temperature'                        #name of 'info' you add.
                ),                                     #more data can be added, following the same structure (line 65-68)
            ),
            KML.styleUrl('#EekMex %i'%i),       #get the correct beachball in the directory as marker
            KML.Point(
                KML.coordinates(longitude[i],',',latitude[i]),
            ),
 
        ),
    )
 
print etree.tostring(etree.ElementTree(kmlobj),pretty_print=True)
outfile= file('eekmex.kml','w') #save the kml structure code
outfile.write(etree.tostring(kmlobj, pretty_print=True))
