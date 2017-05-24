def process_day(file_name):
    data = open(file_name)

    for line in data:
        line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[1]
        amount = words[2]

        print "Delivered {} {}s for total of ${}".format(count, melon, amount)
    data.close()    



files = ["um-deliveries-20140519.txt", "um-deliveries-20140520.txt", "um-deliveries-20140521.txt"]

for i in (0, len(files) - 1): 
    print "Day %s" % (i + 1)
    process_day(files[i])
