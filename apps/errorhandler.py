def writelog(error):
    log = "./log.txt"
    f = open(log,"a")
    f.write(error+"\n")
    f.close()
    return

