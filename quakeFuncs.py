from urllib.request import *
from json import *
from datetime import *
from operator import *

class Earthquake:
    
    def __init__(self, place, mag, longitude, latitude, time):
        self.place = place
        self.mag = mag
        self.longitude = longitude
        self.latitude = latitude
        self.time = time

    def __eq__(self, other):
        return self.place == other.place and \
               self.mag == other.mag and \
               self.longitude == other.longitude and \
               self.latitude == other.latitude and \
               self.time == other.time

    def __repr__(self):
        return self.place+' '+str(self.mag)+' '+str(self.longitude) + \
               ' '+str(self.latitude)+' '+str(time)

def read_quakes_from_file(filename):
    inFile = open(filename,'r')
    quakes = []
    for line in inFile:
        data = line.split()
        place = ' '.join(data[4:])
        quakes.append(Earthquake(place,float(data[0]),float(data[1]), \
                                 float(data[2]),int(data[3])))
    inFile.close()
    return quakes
        
def time_to_str(time): #realTime = time_to_str(objList[4])
   ''' Converts integer seconds since epoch to a string.
       time - an int '''
   return datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')

def display_data(objList):
    print('Earthquakes:')
    print('------------')
    for i in range(len(objList)):
        print('(%.2f) %40s at %s (%8.3f, %6.3f)' % \
              (objList[i].mag,objList[i].place,\
               time_to_str(objList[i].time), \
               objList[i].longitude, \
               objList[i].latitude))

#FILTERING FUNCTIONS:
  
def filter_by_mag(quakes,low,high):
   filtered = []
   for i in range(len(quakes)):
       if low <= quakes[i].mag <= high:
           filtered.append(quakes[i])
   return filtered

def filter_by_place(quakes,word):
   filtered = []
   for i in range(len(quakes)):
       if word in quakes[i].place.lower(): #case insensitive
           filtered.append(quakes[i])
   return filtered

#JSON FUNCTIONS: 

def get_json(url):
   ''' Function to get a json dictionary from a website.
       url - a string'''
   with urlopen(url) as response:
      html = response.read()
   htmlstr = html.decode("utf-8")
   return loads(htmlstr)

def quake_from_feature(feature):
    newQuake = Earthquake(feature['properties']['place'], \
                     float(feature['properties']['mag']), \
                     float(feature['geometry']['coordinates'][0]), \
                     float(feature['geometry']['coordinates'][1]),
                     int(feature['properties']['time']*0.001))
    return newQuake

def quitting(quakes,filename):
    outFile = open(filename, 'w')
    for line in quakes:
        revQuake = revert_quakes(line)
        outFile.write(' '.join(revQuake)+'\n')
    outFile.close()

def revert_quakes(quake):
    reverted = []
    reverted.append(str(quake.mag))
    reverted.append(str(quake.longitude))
    reverted.append(str(quake.latitude))
    reverted.append(str(quake.time))
    reverted.append(quake.place)
    return reverted
