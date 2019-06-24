from quakeFuncs import *

def main():
   quakes = read_quakes_from_file('quakes.txt')
   print()
   display_data(quakes)
   while True:
       print()
       print('Options:')
       print('  (s)ort')
       print('  (f)ilter')
       print('  (n)ew quakes')
       print('  (q)uit')
       print()
       choice = input('Choice: ')
       if choice == 's':
           sort = input('Sort by (m)agnitude, (t)ime, (l)ongitude, or l(a)titude? ')
           if sort == 'm':
               quakes = sorted(quakes, key = attrgetter('mag'), reverse = True)
               print()
               display_data(quakes)
           elif sort == 't':
               quakes = sorted(quakes, key = attrgetter('time'), reverse = True)
               print()
               display_data(quakes)  
           elif sort == 'l':
               quakes = sorted(quakes, key = attrgetter('longitude'))
               print()
               display_data(quakes)
           elif sort == 'a':
               quakes = sorted(quakes, key = attrgetter('latitude'))
               print()
               display_data(quakes)
       elif choice == 'f':
           filt = input('Filter by (m)agnitude or (p)lace? ')
           if filt == 'm':
               lower = float(input('Lower bound: '))
               upper = float(input('Upper bound: '))
               print()
               display_data(filter_by_mag(quakes,lower,upper))
           elif filt == 'p':
               string = input('Search for what string? ')
               print()
               display_data(filter_by_place(quakes,string))
       elif choice == 'n':
          dic = get_json('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson')
          new = False
          for feature in dic['features']:
             newQuake = quake_from_feature(feature)
             if not newQuake in quakes:
                new = True
                quakes.append(newQuake)
          if new == True:
             print()
             print('New quakes found!!!')
          print()
          display_data(quakes)
       elif choice == 'q':
           quitting(quakes, 'quakes.txt')
           break

if __name__ == '__main__':
    main()
