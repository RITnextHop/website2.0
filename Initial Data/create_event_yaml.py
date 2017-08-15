import csv

def WriteToFile(file, data, pk):
    event = "-model: main.event\n\tpk: {}\n\tfields:\n\t\ttype: {}\n\t\ttile: {}\n\t\tlocation: {}\n\t\tstart_date_time: {}\n\t\tend_date_time: {}:00\n\t\tdescription: \"{}\"\n\t\tstream_url: ''\n\t\tresources: []\n\n".format(pk,data[0],data[1],data[2],data[3],data[4],data[5])
    #print(event)
    file.write(event)

write_file = open('event_data.yml', 'w')

data = []
pk = 1

with open('Events.csv', 'r') as csvfile:
        read_file = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in read_file:
            for item in row:
                data.append(item)
            WriteToFile(write_file,data,pk)
            data = []
            pk = pk+1