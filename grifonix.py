import time
import sys

radnice = (0)
penize = (0)
vybaveni = (0)
lovec = (0)
vlci = (0)
hlava = (0)


jmeno = input("Zadej své jméno: ")
print(f"Ahoj {jmeno} vítej ve hře Grifonix!")
time.sleep(0.75)
print("Chceš začít hrát?")
time.sleep(0.57)
print("1. Ano!")
time.sleep(0.5)
print("2. Ne!")

start = int(input(""))

if start == 2:
    print("Tak proč to zapínáš!?")

elif start == 1:

#Domov
    time.sleep(1.5)
    print(f"Probouzíš se ve své posteli a slyšíš jak tě otec volá ke snídani.")

    time.sleep(1)
    print("Co uděláš?")
    time.sleep(0.5)
    print("1. Jít na snídani.")
    time.sleep(0.5)
    print("2. Obléct se.")
    rozhodnuti_1 = int(input(""))

    if rozhodnuti_1 == 1:
        time.sleep(0.5)
        print("Ty idiote, přece nemůžeš jít na snídani nahatej!")
        time.sleep(1)
        print("Oblékl jsi se a jdeš na snídani.")
    elif rozhodnuti_1 == 2:
        print("Oblékl jsi se a jdeš na snídani.")
    time.sleep(1)

    print("Promluvíš si s otcem a ten ti řekne, že máš jít na radnici za starostou.")
    time.sleep(1.5)
    print("Nasnídal jsi se, oblékl a vyšel jsi z domu.")
    time.sleep(1)

    while True:
        print("Kam dál?")
        time.sleep(0.5)
        print("1. Jít do lesa.")
        time.sleep(0.5)
        print("2. Jít do Vesnice.")
        rozhodnuti_2 = int(input(""))
        time.sleep(1)

#Les
        if rozhodnuti_2 == 1:
            while True:                    
                if radnice > 0:
                    print("Došel jsi do lesa.")                   
                else:
                    print("Došel jsi do lesa, to je sice super, ale žádná radnice tu není ty idiote!")
                time.sleep(0.5)
                print("Kam dál?")
                time.sleep(0.5)
                if vybaveni == 0:
                    print("1. Jít do hlouběji do lesa.")
                    time.sleep(0.5)
                else:
                    print("1. Jít na lov Grifonixe.")
                    time.sleep(0.5)
                if lovec >0:
                    print("2. Jít na lov vlků.")
                else:                
                    print("2. Jít k vlkům.")
                time.sleep(0.5)
                print("3. Jít zpátky k domu.")
                rozhodnuti_3 = int(input(""))
    #Grifonix            
                if rozhodnuti_3 == 1:
                    if vybaveni == 0:
                        time.sleep(1)
                        print("Gratuluji zabil tě Grifonix!")
                        sys.exit()
                    else:
                        print("Po dlouhém souboji se ti podařilo Grifonixovi useknout hlavu!!!")
                        time.sleep(1.5)
                        print("Dones hlavu starostovi, aby jsi dokázal, že jsi Grifonixe zabil.")
                        time.sleep(1.5)
                        hlava += 1
                        break    
    #Vlci
                elif rozhodnuti_3 == 2:
                    if lovec > 0:
                        time.sleep(1)
                        print("Zabil jsi vlky a získal z nich kůži!")
                        vlci += 1
                        time.sleep(1)
                        break
                    else:    
                        time.sleep(1)
                        print("Gratuluji zabili tě vlci!")
                        sys.exit()
    #Zpět
                if rozhodnuti_3 == 3:
                    time. sleep(0.5)
                    print("Došel jsi zpátky k domovu.")
                    break

#Vesnice                    
        elif rozhodnuti_2 == 2:
            while True:
                print("Kam dál?")
                time.sleep(0.5)
                print("1. Jít do obchodu.")
                time.sleep(0.5)
                print("2. Jít do radnice.")
                time.sleep(0.5)
                print("3. Jít zpátky k domu.")
                if radnice > 0:
                    time.sleep(0.5)
                    print("4. Jít k lovcovi.")
                rozhodnuti_4 = int(input(""))

#Obchod                   
                if rozhodnuti_4 == 1:
                    while True:
                        time.sleep(1)
                        print("Došel jsi do obchodu, co dál?")
                        time.sleep(0.5)
                        print("1. Koupit profesionální vybavení.")
                        time.sleep(0.5)
                        print("2. Jít zpátky.")
                        rozhodnuti_5 = int(input(""))
                        time.sleep(0.5)
    #Koupit vybavení                    
                        if rozhodnuti_5 == 1:
                            if penize > 0:
                                print("Koupil jsi profesionální vybavení.")
                                time.sleep(1)
                                vybaveni += 1
                                break
                            else:
                                print("Nemáš peníze ubožáku!")
                                time.sleep(1)
                                break
    #Zpět
                        elif rozhodnuti_5 == 2:
                            print("Došel jsi zpátky.")
                            time.sleep(1)
                            break

#Radnice                    
                elif rozhodnuti_4 == 2:
                    while True:
                        time.sleep(1)
                        print("Došel jsi do radnice, co dál?")
                        time.sleep(1)
                        print("1. Jít na záchod.")
                        time.sleep(0.5)
                        print("2. Jít si promluvit se starostou.")
                        time.sleep(0.5)
                        print("3. Jít zpátky.")
                        rozhodnuti_6 =int(input(""))
                        time.sleep(1)
    #Záchod                    
                        if rozhodnuti_6 == 1:
                            print("Došel jsi na záchod.")
                            time.sleep(1)
                            print("S úsměvem na tváři jsi si sedl na pisoár a začal trůnit.")
                            time.sleep(2.5)
                            print("Kdo už tak vysmátý nebyl, byl starosta.")
                            time.sleep(2.5)
                            print("Ten vešel dovnitř zrovna, když jsi vykonával tuto aktivitu.")
                            time.sleep(2.5)
                            print("Starosta tě vykázal z vesnice na vždy.")
                            time.sleep(2.5)                               
                            print("Gratuluji, tohle je ten nejdebilnější konec, kterého jsi mohl dosáhnout!")
                            time.sleep(5)
                            sys.exit()
    #Starosta                    
                        elif rozhodnuti_6 == 2:                                
                            if hlava == 0:
                                print("Došel jsi za starostou.")
                                time.sleep(1)
                                print("Starosta ti sdělil, že v lese se objevil velmi nebezpečný tvor zvaný Grifonix.")
                                time.sleep(2.5)
                                print("Také ti sdělil, že už je starý a chystá se jít do důchodu.")
                                time.sleep(2.5)
                                print("*Grifonix je nebezpečný, už zabil 3 nevinné kolemjdoucí!*")
                                time.sleep(2.5)
                                print("*Pokud zabiješ Grifonixe, přenechám ti svoji pozici starosty!*")
                                time.sleep(2.5)
                                print("*Jdi k lovcovi, ten ti řekne více informací.*")
                                radnice += 1
                                time.sleep(3)
                                break
                            else: 
                                print("*Ty jsi to dokázal!*")
                                time.sleep(1)
                                print(f"*NOVÝM STAROSTOU SE STÁVÁ {jmeno}!*")
                                time.sleep(1.5)
                                print("Neuvěřitelné, ty jsi dokončil tuhle hru. Děkuji za hraní této hry a užij si práci starosty!")
                                time.sleep(5)
                                sys.exit()
    #Zpět
                        elif rozhodnuti_6 == 3:
                            break
    #Zpět            
                elif rozhodnuti_4 == 3:
                    time.sleep(1)
                    break

#Lovec
                elif rozhodnuti_4 == 4:
                    while True:
                        if lovec == 0:
                            time.sleep(1)
                            print(f"*Ahoj {jmeno}, mé jmeno je Petr Včelka a jsem místní lovec.*")
                            time.sleep(2.5)
                            print(f"*Určitě tu jsi kvůli Grifonixovi.*")
                            time.sleep(1.5)
                            print(f"*Grifonix je  obří zvíře, jehož tělo je pokryto ostrými šupinami a vyzbrojeno mohutnými tlapami.*")
                            time.sleep(3.5)
                            print("*Aby jsi Grifonixe porazil, budeš potřebovat profesionální loveckou výbavu.*")
                            time.sleep(3)
                            print("*Tato výbava je hodně drahá, ale dám ti na ni peníze, pokud mi doneseš vlčí kůži.*")
                            time.sleep(2.5)
                            print("*Vlky najdeš v lese, dám ti vybavení, které budeš potřebovat na to, aby jsi vlky zabil.*")
                            time.sleep(3)
                            lovec += 1
                            break
                        else:
                            time.sleep(1)
                            if vlci == 0:
                                print("Nemáš vlčí kůži idiote!")
                                time.sleep(1)
                                break
                            else:
                                print("*Věděl jsem, že to zvládneš, tady jsou tvé peníze.*")
                                penize += 1
                                time.sleep(2)
                                break
                    



                                
                            

                                
                                


