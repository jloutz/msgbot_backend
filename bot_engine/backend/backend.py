import sqlite3

class NuernbergBackend():

    def __init__(self) -> None:
        self.datastorage={}
        self.kategorien=["familien","kinder","zuwanderer","senioren","stadtteil","ZAB","praktisches"]
        for kategorie in self.kategorien:
            self.datastorage[kategorie]={}
        self.datastorage["familien"]["bereiche"]=["Patenschaften rund um Geburt","Elternbegleiter und Brückenbauer","Patenschaften für Kinder seelisch erkrankter Eltern","Ämter und Behördenbegleiter"]
        self.datastorage["kinder"]["bereiche"]=["Grosse für Kleine","Mentoring und Lernpaten","Kinderpaten","Kulturfreunde","Kleine Entdecker"]
        self.datastorage["zuwanderer"]["bereiche"]=["Sprach und Kulturvermittler","Patenschaften für Zuwanderer und Geflüchtete","Flüchtlingshilfe","Engagementbegleiter"]
        self.datastorage["senioren"]["bereiche"]=["Wohnraumberatung","3000 Schritte"]
        self.datastorage["stadtteil"]["bereiche"]=["Für den Stadtteil"]
        self.datastorage["ZAB"]["bereiche"]=["Engagementberater","Büroteam"]
        self.datastorage["praktisches"]["bereiche"]=["Handwerker","Bücherdienst","Gartengruppe"]
        for kategorie in self.kategorien:
            for bereich in self.datastorage[kategorie]["bereiche"]:
                self.datastorage[kategorie][bereich]={}
                self.datastorage[kategorie][bereich]["name"]=bereich
                self.datastorage[kategorie][bereich]["kurzbeschreibung"]=""
                self.datastorage[kategorie][bereich]["langbeschreibung"]=""

        self.datastorage["zuwanderer"]["Sprach und Kulturvermittler"]["kurzbeschreibung"]="Die Sprachvermittler vom Zentrum Aktiver Bürger bieten Unterstützung bei Anmeldungen und Elterngesprächen in Kindergärten, Horten und Schulen."
        self.datastorage["zuwanderer"]["Sprach und Kulturvermittler"]["langbeschreibung"]=""" Die Sprachvermittler beherrschen Deutsch und mindestens eine andere Sprache flüssig. Sie übersetzen nicht nur Wort für Wort, sondern sind ein wichtiger Brückenbauer zwischen den Kulturen. Geflüchteten helfen sie dabei, den Alltag besser zu verstehen.

Die stadtweite Koordination erfolgt durch einen hauptamtlichen Ansprechpartner. Fortbildungen und Austausch unterstützen das Engagement der ZAB-Sprachvermittler.

Unser Kultur- und Sprachvermittler-Team ist wichtiger Baustein für die Integration von Flüchtlingen und Asylbewerbern in die Nürnberger Stadtgesellschaft.
Wir übersetzen derzeit in folgende Sprachen

albanisch, amharisch, arabisch, aramäisch, assyrisch, bosnisch, bulgarisch, dari, englisch, farsi, französisch, griechisch, hindi, italienisch, kroatisch, kurdisch, mazedonisch, paschtu, polnisch, portugiesisch, punjabi, rumänisch, russisch, serbisch, sorani, slowenisch, spanisch, tschetschenisch, tigrinia, türkisch, turkmenisch, ungarisch, ukrainisch, urudu, vietnamesisch, weißrussisch. "
"""
        self.datastorage["zuwanderer"]["Patenschaften für Zuwanderer und Geflüchtete"]["kurzbeschreibung"]="Ein sicheres Umfeld und das Gefühl, in der neuen Heimat angenommen zu sein, sind wichtige Schutzfaktoren für zugewanderte Familien – gerade wenn vieles noch fremd und beängstigend ist. "
        self.datastorage["zuwanderer"]["Patenschaften für Zuwanderer und Geflüchtete"]["langbeschreibung"]="""Nach akuten Hilfen in Notunterkünften, Helferkreisen, u.ä. wird an vielen Stellen deutlich, dass geflüchtete Familien Unterstützung benötigen. Familienpatinnen und Paten können an dieser Stelle ihre vielfältigen Ressourcen einbringen, um Integration zu fördern.
Die Familie entlasten

Je nach Einzelfall können Entlastungsangebote sein:

    Aktivitäten mit Kindern,
    Unterstützung beim Spracherwerb,
    gemeinsame Freizeitgestaltung,
    Ausflüge,
    kultureller Austausch,
    Identitätsfindung,
    Integration in Vereine,
    Begleitung zu Ämtern,
    Weitergabe von alltagspraktischem Wissen und
    Wohnungssuche.

Ehrenamtliche Familienpatinnen und Paten des ZAB werden durch eine pädagogische Fachkraft vermittelt, begleitet und unterstützt. Durch 1:1 Patenschaften – ein/e Ehrenamtliche/r für eine Familie – ergeben sich neue soziokulturelle Perspektiven für alle Beteiligten. """
        self.datastorage["zuwanderer"]["Flüchtlingshilfe"]["kurzbeschreibung"]="Die Möglichkeiten, sich beim Zentrum Aktiver Bürger ehrenamtlich für Geflüchtete zu engagieren, sind vielfältig. Integration und Teilhabe stehen dabei im Mittelpunkt unserer Arbeit."
        self.datastorage["zuwanderer"]["Flüchtlingshilfe"]["langbeschreibung"]=""" Das ZAB arbeitet eng mit Asylsozialbetreuungen sowie  Organisationen, Vereinen und Initiativen in der Flüchtlingshilfe zusammen. Wir vermitteln Freiwillige in bestehende Projekte oder entwickeln – falls nötig – passende Angebote und eigene Einsatzfelder.
Eigene Projekte und Kooperationsprojekte

Für geflüchtete Familien organisieren wir Patenschaften.

Über unser Projekt "Aktiv im Stadtteil" vermitteln wir in zahlreiche Projekte vor Ort:

    "Café International" im Mehrgenerationenhaus Schweinau
    "Café Creativ" in einer Unterkunft in Schweinau
     Bewerbungstraining in der Villa Leon
     Kinderbetreuung in einer Unterkunft am Aufseßplatz
     Helferkreis Witschelstraße
     Sprachtandemprojekt
"""
        self.datastorage["zuwanderer"]["Engagementbegleiter"]["kurzbeschreibung"]="Engagementbegleiter vom Zentrum Aktiver Bürger (ZAB) unterstützen Menschen mit geringen Deutschkenntnissen bei deren Einstieg ins Ehrenamt. "
        self.datastorage["zuwanderer"]["Engagementbegleiter"]["langbeschreibung"]="""
        Viele Menschen in Nürnberg, die wenig oder kaum deutsch sprechen, möchten sich ehrenamtlich engagieren. So bekommen sie einen wertvollen Kontakt zur deutschen Kultur und Sprache. Jedoch ist für diesen Personenkreis der Einstieg als Ehrenamtlicher in eine Einrichtung oft schwierig. Denn durch die sprachlichen Hürden gestaltet sich die Einarbeitung für die Einrichtungen oft äußerst zeitaufwändig.
Engagementbegleiter als Mittler

Engagementbegleiter des ZAB unterstützen die neuen Freiwilligen bei ihrem Engagement direkt vor Ort, lassen sich von den Mitarbeitern der Einsatzstelle einweisen und vermitteln geduldig zwischen beiden Seiten – bis die neuen Freiwilligen und die Mitarbeiter der Einsatzstelle aufeinander eingespielt sind.

Die Engagementbegleiter müssen keine Fremdsprache beherrschen – Zeit, Geduld und Offenheit für andere Kulturen sind hier wichtiger. Sie erhalten durch ihre Tätigkeit Einblicke in verschiedene Einrichtungen und können sich je nach ihrem Zeit-Kontingent flexibel einbringen.
Aufgaben und Tätigkeiten
Engagementbegleiter

    nehmen Kontakt zu Einsatzstellen auf,
    begleiten die Ehenramtlichen bei Erstgesprächen in der Einsatzstelle,
    unterstützen die Ehrenamtlichen bei den ersten Einsätzen,
    sind Ansprechpartner für die Mitarbeiter in der Einrichtung,
    vermitteln bei Kommunikationsschwierigkeiten.

Anbindung an das ZAB

Das Zentrum Aktiver Bürger betreut die Engagementbegleiter durch eine hauptamtliche Ansprechpartnerin. Wir bieten bedarfsabhängige Fortbildungen und Austauschtreffen mit anderen Engagementbegleitern, Fahrtkostenzuschuss und Versicherungsschutz sowie die persönliche Unterstützung im Einzelfall.
Förderung

Dieses Projekt wird aus Mitteln des Bayerischen Staatsministeriums für Familie, Arbeit und Soziales gefördert."""




class Backend():
    def __init__(self):
        ## name von db Datei
        self.dbfile = "backend/bundesbot.db"

    def eval(self,sql,parameters=(),doprint=False):
        ## benutze eval, um sql auszufüren
        conn = sqlite3.connect(self.dbfile)
        cursor = conn.cursor()
        cursor.execute(sql,parameters)
        res = cursor.fetchall()
        conn.close()
        if doprint:
            print(str(res))
        return res

    def setup(self):
        ## backend datenbank aufsetzten
        conn = sqlite3.connect(self.dbfile)
        print(sqlite3.version)
        cursor = conn.cursor()
        print("SETTING up database")

        ## TODO einkommentieren und fertig implementieren, um db zu erstellen
        cursor.execute("DROP TABLE IF EXISTS bundesbot")
        cursor.execute('''CREATE TABLE bundesbot
                        (name text)''')

        ## TODO einkommentieren und fertig implementieren, um Beispiel daten zu erstellen
        cursor.execute(
          "INSERT INTO bundesbot VALUES ('bla')")
        res = cursor.execute("SELECT count(*) from bundesbot")
        print("DB hat "+str(res.fetchone()[0])+" Einträge")
        conn.commit()
        conn.close()

