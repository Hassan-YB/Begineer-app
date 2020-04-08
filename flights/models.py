from django.db import models
Airport_Choices=(
                ("Karachi-Jinnah Intl. (KHI)","Karachi-Jinnah Intl. (KHI)"),
                ("Bahawalpur(BHV)","Bahawalpur(BHV)"),
                ("Chitral(CJL)","Chitral(CJL)"),
                ("Dalbandin(DBA)","Dalbandin(DBA)"),
                ("Dera Ghazi Khan Intl(DEA)","Dera Ghazi Khan Intl(DEA)"),
                ("Dera Ismail khan(DSK)","Dera Ismail khan(DSK)"),
                ("Faislabad Intl(LYP)","Faislabad Intl(LYP)"),
                ("Gilgit(GIL)","Gilgit(GIL)"),
                ("Gwadar Intl.(GWD)","Gwadar Intl.(GWD)"),
                ("Islamabad Intl(ISB)","Islamabad Intl(ISB)"),
                ("Lahore Intl (LHE)","Lahore Intl (LHE)"),
                ("Moenjodaro(MJD)","Moenjodaro(MJD)"),
                ("Multan Intl.(MUX)","Multan Intl.(MUX)"),
                ("Nawabshah Airport(WNS)","Nawabshah Airport(WNS)"),
                ("Panjgur(PJG)","Panjgur(PJG)"),
                ("Peshawar Intl(PEW)","Peshawar Intl(PEW)"),
                ("Quetta Intl(UET)","Quetta Intl(UET)"),
                ("Rahim Yar khan(RYK)","Rahim Yar khan(RYK)"),
                ("Sialkot Intl(SKT)","Sialkot Intl(SKT)"),
                ("Skardu Intl(SKT)","Skardu Intl(SKT)"),
                ("Sukkur(SKZ)","Sukkur(SKZ)"),
                ("Turbat Intl(TUK)","Turbat Intl(TUK)"),
                ("Zhob(PZH)","Zhob(PZH)"),
                ("Select","Select"),
                )
Cabin_choices=(
        ("Select","Select"),
        ("Economy","Economy"),
        ("Executive Economy","Executive Economy"),
        ("Business","Business")
        )
Class_type=(
    ("Select","Select"),
    ("Return","Return"),
    ("Oneway","Oneway"),
    )

class Airport(models.Model):
    Name=models.CharField(max_length=50)

    def __str__(self):
        return self.Name

class Pilot(models.Model):
    Name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.Name

class Crew(models.Model):
    Name=models.CharField(max_length=50)

    def __str__(self):
        return self.Name


class Flight(models.Model):
    Starting_airport=models.ForeignKey(Airport, on_delete = models.CASCADE , related_name="Starting_airport")
    Destination_airport=models.ForeignKey(Airport, on_delete = models.CASCADE ,related_name="Destination_airport")
    pilot=models.ForeignKey(Pilot, on_delete = models.CASCADE ,related_name="pilot")
    crew=models.ForeignKey(Crew, on_delete = models.CASCADE ,related_name="crew")
    Starting_time=models.DateTimeField()
    Destination_time=models.DateTimeField()
    Passengers_limit=models.IntegerField(default=0)

    def __str__(self):
        start=self.Starting_airport
        end=self.Destination_airport
        To=" To "
        all=str(start)+str(To)+str(end)
        return all

class Passenger(models.Model):
    flight=models.ForeignKey(Flight,on_delete=models.CASCADE,related_name="Passenger_flight",null=True)
    Name=models.CharField(max_length=50)
    Surname=models.CharField(max_length=50)

    def __str__(self):
        return str(self.Name)+str(" ")+str(self.Surname)
   

class Domestic(models.Model):
    
    Type=models.CharField(default='Select',max_length=100,choices=Class_type)
    From=models.CharField(
       max_length=200,
       choices=Airport_Choices,
       default='Select')
    To=models.CharField(
        max_length=200,
        choices=Airport_Choices,
        default='Select')
    Starting_date=models.DateTimeField(null=True)
    Destination_date=models.DateTimeField(null=True)
    Cabin=models.CharField(
        max_length=200,
        choices=Cabin_choices,
        default='Select')
    
    def __str__(self):
        return str(self.From)+str(" To ")+str(self.To)

class International(models.Model):
    
    Type=models.CharField(default='Select',max_length=100,choices=Class_type)
    From=models.CharField(default='From: Airport & City',max_length=100)
    To=models.CharField(default='To: Airport & City',max_length=100)
    Starting_date=models.DateTimeField(null=True)
    Destination_date=models.DateTimeField(null=True)
    Cabin=models.CharField(
        max_length=200,
        choices=Cabin_choices,
        default='Select')
    
    def __str__(self):
        return str(self.From)+str(" To ")+str(self.To)


        





