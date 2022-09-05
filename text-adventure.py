#Vorgeschichte
name = input("Wie ist dein Name?")
print("Hallo " + name + " ,In diesem Advanture befindest du dich in einem Dschungel und musst dich gegen verschiedene Gefrahren behaupten.")

#Level 1
print ("Ein Löwe erscheint und steht aufeinmal vor dir.")
antwort = input("Löwe angreifen/weg rennen")

if antwort.lower().strip() == "Löwe angreifen":
    print("Schlechte idee, der Löwe zereißt dich. (Du bist Tod)")

elif antwort == "weg rennen":
    print ("Eine gute Entscheidung, du entkommst.")

else:
    print ("Du bist irgendwie aus dieser Situation entkommen, Glückwunsch.")
antwort = input ("Du kommst an einem Fluss vorbei, möchtest du was trinken? (ja/nein)")

if antwort.lower().strip() == "ja":
    print ("Dein durst ist jetzt gestillt.")

else:
    print("Schlechte Entscheidung, du bist nach einigen Stunden umherirren verdurstet. (Du bist Tod)")

#Level 2
antwort = input("Nach einem langen Weg kommst du an eine Abzweigung. Möchtest du nach (links/rechts) gehen?")

#linker weg
if antwort.lower().strip() == "links":
    print("Du kommst in ein Dorf. Möchtest du die Nacht dort verbringen? (ja/nein)")
#nacht dort verbringen
    if antwort.lower().strip() == "ja":
        antwort = input("Die Dorfbewohner bringen dich in ein Haus um dir ein schlafplatz anzubieten. Möchtst du dich dort schlafen legen? (ja/nein)")
#in dem haus schlafen
        if antwort.lower().strip() == "ja":
            print("Die Dorfbewohner schleifen dich Nachts aus dem Bett und verbrennen dich auf dem Scheiterhaufen. (Du bist Tod)")
#nicht im haus schlafen
        elif antwort.lower().strip() == "nein":
            print("Du watest in dem Zimmer bis die Dorfbewohner schlafen, dann kletterst du aus dem Fenster und wirst von den Dorfbewohnern erwischt, welche dich auf dem Markplatz Kreuzigen. (Du bist Tod)")
#nacht nicht dort verbringen
    elif antwort.lower().strip() == "nein":
        print("Du läufst weiter bis du nachts bei einer verlassenen Hütte ankommst. Möchtest du dort schlafen?")
#rechter weg
elif antwort.lower().strip() == "rechts":
    print("Du kommst nachts bei einer verlassenen Hütte an. Möchtest du in dieser schlafen? (ja/nein")
