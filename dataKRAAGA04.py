import csv

#uT = "el diablo"
#uC = "Machine Gun Kelly"
#uP = "Machine Gun Kelly"
#uL = "English"
#uR = "2019"
#uG = "hip-hop"
#uS = "rap"
#uTp = "rapping struggles"
#uM = "hype"
#uD = "synthesizer"
#uIs = 8
#uLyr = 7
#uVoc = 5
#uMel = 8
#uRhy = 8
#uDdr = 6
#uTmp = 8
#genre is the fifth column

songList = []
songList = [row for row in csv.reader(open("pySongLibS19.tsv", encoding='utf-8'), delimiter="\t")]

del songList[0]
del songList[0]

for a in range(len(songList)):
    songList[a][4] = int(songList[a][4])
for b in range(len(songList)):
    songList[b][10] = int(songList[b][10])
for c in range(len(songList)):
    songList[c][11] = int(songList[c][11])
for d in range(len(songList)):
    songList[d][12] = int(songList[d][12])
for e in range(len(songList)):
    songList[e][13] = int(songList[e][13])
for f in range(len(songList)):
    songList[f][14] = int(songList[f][14])
for g in range(len(songList)):
    songList[g][15] = int(songList[g][15])
for h in range(len(songList)):
    songList[h][16] = int(songList[h][16])

print("""Hey there!

This program will take a song you already know,
analyse it, and give you a song that is similar 
to that one you put in.

To do this, we are going to ask you 17 questions about
a song you like.

Are you ready?""")

start = input("Your answer (Y or N) >>> ")

if start == ("Yes") or ("Y") or ("yes") or ("y"):
    print("Alright! Lets get started.")
    print(" ")
    uT = input("""What is the name of the song?
    Your answer >>> """)
    print(" ")
    uC = input("""Who is the creator of the song?
    (so who wrote the lyrics of the song)
    Your answer >>> """)
    print(" ")
    uP = input("""Who is the performer of the song?
    (so who is singing the song?)
    Your answer >>> """)
    print(" ")
    uL = input("""What is the language of this song?
    Your answer >>> """)
    print(" ")
    uR = input("""What year was the song recorded?
    Your answer >>> """)
    print(" ")
    uG = input("""What is the genre of the song?
    (if hip-hop, type as "hip-hop")
    Your answer >>> """)
    print(" ")
    uS = input("""What is the sub-genre of the song?
    Your answer >>> """)
    print(" ")
    uTp = input("""What is the topic of the song?
    (describe what the song is about, using one word renders
    better results)
    Your answer >>> """)
    print(" ")
    uM = input("""What is the mood of the song?
    (what is the "feeling" of the song, what are the songs
    "vibes"?)
    Your answer >>> """)
    print(" ")
    uD = input("""What is the dominant instument of the song?
    (what is the most powerful or notable instument of the
    song?)
    Your answer >>> """)
    print(" ")
    print(" ")
    print("""***On the rest of the questions you are going to be asked to rate***
    ***aspects of the song on a scale of 0-10.***
    ***0 being the worse and 10 being the best***
    ***Keep this in mind while you are answering the questions***""")
    print(" ")
    print(" ")
    uIs = (int(input("""Rate on a scale from 0-10 the instrumental
    skill of the song.
    (how well does the artist play the instrument?)
    Your answer >>> """)))
    print(" ")
    uLyr = (int(input("""Rate on a scale from 0-10 the lyrics of the song.
    (how good are the lyrics of the song?)
    (if their are no lyrics, type null)
    Your answer >>> """)))
    print(" ")
    uVoc = (int(input("""Rate on a scale from 0-10 the vocals of the song.
    (how well does the performer sing or rap the song?)
    (if their are no vocals, type null)
    Your answer >>> """)))
    print(" ")
    uMel = (int(input("""Rate on a scale from 0-10 the melody of the song.
    (how good is the melody of the song?)
    Your answer >>> """)))
    print(" ")
    uRhy = (int(input("""Rate on a scale from 0-10 the rythem of the song.
    (how good is the rythem of the song?)
    Your answer >>> """)))
    print(" ")
    uDdr = (int(input("""Rate on a scale from 0-10 how much does the song.
    wants to make you dance?
    Your answer >>> """)))
    print(" ")
    uTmp = (int(input("""Rate on a scale from 0-10 the tempo of the song.
    (how good is the tempo of the song?)
    Your answer >>> """)))
    print(" ")

    uSongList = [uT, uC, uP, uL, uR, uG, uS, uTp, uM, uD, uIs, uLyr, uVoc, uMel, uRhy, uDdr, uTmp]
    m1 = []

    for song in range(len(songList)):
        if songList[song][5] == uG:
            print("*")
            m1.append(songList[song])

