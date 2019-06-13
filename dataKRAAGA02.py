import csv

uT = "el diablo"
uC = "Machine Gun Kelly"
uP = "Machine Gun Kelly"
uL = "English"
uRec = "2019"
uGn = "hip-hop"
uSg = "rap"
uTop = "rapping struggles"
uMd = "hype"
uDi = "synthesizer"

uIs = 8
uLyr = 7
uVoc = 5
uMel = 8
uRhy = 8
uDdr = 6
uTmp = 8

songList = []
songList = [row for row in csv.reader(open("pySongLibS19.tsv", encoding='utf-8'), delimiter="\t")]

del songList[0]
del songList[0]

for song in range(len(songList)):
    songList[song][4] = int(songList[song][4])
    for song in range(len(songList)):
        songList[song][10] = int(songList[song][10])
        for song in range(len(songList)):
            songList[song][11] = int(songList[song][11])
            for song in range(len(songList)):
                songList[song][12] = int(songList[song][12])
                for song in range(len(songList)):
                    songList[song][13] = int(songList[song][13])
                    for song in range(len(songList)):
                        songList[song][14] = int(songList[song][14])
                        for song in range(len(songList)):
                             songList[song][15] = int(songList[song][15])
                             for song in range(len(songList)):
                                songList[song][16] = int(songList[song][16])