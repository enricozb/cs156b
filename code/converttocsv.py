# Relies on data being stored at project root e.g. /data/mu/all.dta
# Run this file from inside /code.

import csv

def convert(sort_order, name):
    writr = csv.writer(open('../data/'+sort_order+'/'+name+'.csv', 'wb'))

    data = open('../data/'+sort_order+'/'+name+'.dta', 'r')

    while True:
        s = data.readline()
        if not s:
            break
        writr.writerow(s.split())

    data.close()

convert('mu', 'all')
convert('um', 'all')
