#import csv
import yaml

#{'hero': {'hp': 34, 'sp': 8, 'level': 4}, 'orc': {'hp': 12, 'sp': 0, 'level': 2}}

print yaml.dump({'model': 'main.event', 'pk': 1,'feilds': {'type': 'Build-It-Night', 'resources':[1,2]}})

'''
in_file  = open('csv_file.csv', "r")
out_file = open('yaml_file.yaml', "w")
items = []

def convert_to_yaml(line, counter):
    item = {
        'id': counter,
        'title_english': line[0],
        'title_russian': line[1]
    }
    items.append(item)

try:
    reader = csv.reader(in_file)
    next(reader) # skip headers
    for counter, line in enumerate(reader):
        convert_to_yaml(line, counter)
    out_file.write( yaml.dump(items, default_flow_style=False,allow_unicode=True) )

finally:
    in_file.close()
    out_file.close()
'''

#- model: main.event
#  pk: 1
#  fields:
#    type: Build-It-Night
#    title: PXE Boot
#    location: GOL 2300
#    start_date_time: 2017-08-13 04:37:26+00:00
#    end_date_time: 2017-08-13 06:37:27+00:00
#    description: "PXE boot is awesome!\r\n\r\nYay new line"
#    stream_url: ''
#    resources: [1, 2]