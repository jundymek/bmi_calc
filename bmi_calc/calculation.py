

class BmiCalculator():

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        self.bmi = weight / ((height / 100)**2)

    def count_bmi(self):
        return self.bmi

    def bmi_message(self):
        if self.bmi < 18.5:
            return('Niedowaga jest wbrew pozorom bardzo niebezpieczna. Może ona\
                prowadzić do wszelakich zaburzeń funkcjonowania organizmu (np.\
                pracy serca), zaburzeń hormonalnych, wystąpienia poronień u\
                kobiet w ciąży, przewlekłego niedoboru witamin i składników\
                mineralnych, co często wywołuje nieodwracalne zmiany w\
                organizmie. Przyczynami najczęściej są nadmierne odchudzanie,\
                anoreksja, bulimia lub często też nowotwór. Objawami, prócz\
                wychudzenia najczęściej są ospałość, zmniejszona odporność, zła\
                kondycja włosów i paznokci. Przy niedowadze niekiedy występuje\
                anemia, osłabienie kości, osteoporoza.', 'niedowaga', 'red',
                   'not-ok')
        elif self.bmi >= 18.5 and self.bmi <= 25:
            return('Świadczy o prawidłowej masie ciała. Oznacza to, że nie ma \
                potrzeby zmiany stylu życia, czy odżywiania się.', 'waga\
                prawidłowa', 'green', 'ok')
        elif self.bmi > 25 and self.bmi <= 30:
            return('Osoby, które uzyskały ten wynik nie muszą się jeszcze \
                zanadto martwić, lecz powinny to potraktować jako sygnał \
                ostrzegawczy, który sugeruje zmianę stylu życia, ograniczenie \
                cukrów i tłuszczy.', 'nadwaga', 'orange', 'not-ok')
        elif self.bmi > 30 and self.bmi <= 35:
            return('Wynik ten mówi o zwiększonym ryzyku wystąpienia chorób\
                typowych dla otyłości.', 'otyłość I stopnia', 'red', 'not-ok')
        elif self.bmi > 35 and self.bmi <= 40:
            return('W przedziale tym znacząco wzrasta ryzyko wystąpienia chorób\
                związanych z otyłością.', 'otyłość II stopnia', 'red', 'not-ok')
        elif self.bmi > 40:
            return('Osoby, które uzyskały ten wynik powinny jak najszybciej udać\
                się do lekarza. W tym przedziale występuje bardzo duże zagrożenie\
                życia. Taką otyłość leczy się specjalnie dobranymi ćwiczeniami,\
                dietą i lekami. W przypadkach, kiedy to nie wystarczy potrzebna\
                jest operacja chirurgiczna.', 'otyłość III stopnia', 'red',
                   'not-ok')