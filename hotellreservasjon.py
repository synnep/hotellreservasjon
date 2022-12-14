class Hotell:
    """
    Klasse for å lage hotell-objekt.

    Parametre:
        Rom (int): antall rom på hotellet
    """

    def __init__(self, rom):
        self.rom = int(rom)
        self.register = []  # ENDRE NAVN TIL REGISTER??
        self.kapasitet = int(rom)
        self.sengPerRom = 4
        self.maksAntGjester = rom*self.sengPerRom
        self.antGjester = 0

    def reservasjon(self):
        """
        Metode som utfører reservasjon av et rom.

        Bruker inputs for å få verdier til parametre for kundeklassen, og lager en kunde.
        Kunden tar et rom, så de kapasitet skal bli 1 mindre
        """
        print("")
        navn = input("Skriv inn navn: ")
        postnummer = input("Skriv inn postnummer: ")
        email = input("Skriv inn email: ")
        for i in range(len(self.register)):
            if navn == self.register[i].navn and email == self.register[i].email:
                print("Kunden har allerede en reservasjon!")
                return "Dobbelbook"
        gjest = int(input("Skriv inn antallet gjester du bestiller for: "))
        if gjest > self.sengPerRom:  # hvis mindre enn 0
            print(
                f"Det er {self.sengPerRom} per rom, så da må du reservere flere ulike rom.")
            return "For mange gjester per rom"
        netter = int(input("Skriv inn antall netter: "))
        kunden = Kunde(navn, postnummer, email, gjest, netter)

        self.kapasitet -= 1
        self.register.append(kunden)

        print("\n-------<RESERVASJON>------")
        print(f" Kunde ( {kunden} ) med:")
        print(f" Navn: {navn}, Email: {email}, Postnummer: {postnummer}")
        print(f" Bestiller for {gjest} personer, for {netter} netter.")
        print("---------------------------")
        print(f" Gjenstående kapasitet: {self.kapasitet}")
        print(f" Register: {self.register}")
        print("---------------------------")

        # self.sendRegning()

    def sjekkLedigRom(self):
        """
        Sjekker antall ledige rom på hotellet.
        Finner også antall ledige sengeplasser.
            Hvis et rom et tatt, men ikke alle sengeplasser, telles fortsatt 
            disse sengeplassene. 
        Printer verdierne til ledige rom og ledige sengeplasser.
        """
        if self.kapasitet == 0:
            print("Det er ingen ledige rom på hotellet.")
            print("Bedre lykke på vårt fantastiske hotell neste gang.")
        else:
            print(f"Det er {self.kapasitet} ledige rom på hotellet.")
            ledigSengeplass = self.maksAntGjester - self.antGjester
            print(f"Dette tilsvarer {ledigSengeplass} ledige sengeplasser.")
        variabel = input("Tilbake til meny (tast m): ")
        if(variabel == 'm'):
            meny == True


class Kunde:
    """
    Klasse for å lage kunde-objekter.

    Parametre:
        Navn (str)
        Postnummer (str)
        Email (str)
        Rabattkode (str)
    """

    # Inisialiseringskoden. Definerer noen parametre til kundeobjektet
    def __init__(self, navn, postnummer, email, gjestKunde, netter):
        self.navn = navn
        self.postnummer = postnummer
        self.email = email
        self.gjestKunde = gjestKunde
        self.antallNetter = netter

    # OPPGAVE I: TENGER KANSKJE OPPDATERING SENERE

    def visInfo(self):
        print("\n*-*KUNDE*-*")
        print(f"\tNavn: {self.navn}")
        print(f"\tEmail: {self.email}")
        print(f"\tRabattkode: {self.rabattkode}")
        print(f"\tAntall gjester: {self.gjestKunde}")

    def endreReservasjon(self, navn, email):
        print("Hei!")


sjosiden = Hotell(10)

while True:
    print("")
    print("---------------------------------------")
    print("Velkommen til Sjøsiden Hotell!")
    print("---------------------------------------")
    print("")
    print("Skriv 'r' for å reservere")
    print("Skriv 'l' for å sjekke ledige rom")
    print("Skriv 'e' for å endre reservasjon")
    print("Skriv 'o' for å oppdatere kundeinformasjon")
    print("Skriv 'p' for å printe ut kundeinformasjon")
    print("Skriv 'd' for å avslutte")
    valg = input("Skriv handlingen du vil gjøre: ")

    if valg == 'r':
        sjosiden.reservasjon()
    if valg == 'l':
        sjosiden.sjekkLedigRom()
    if valg == 'e':
        Kunde.endreReservasjon()
    '''
    if valg == 'o':
        Kunde.oppdaterKundeInfo()
    '''

    if valg == 'p':
        Kunde.visInfo()
    if valg == 'd':
        break
