# Generated by Django 3.0.4 on 2020-03-31 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0010_auto_20200328_0223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domestic',
            name='Cabin',
            field=models.CharField(choices=[('Select', 'Select'), ('Economy', 'Economy'), ('Executive Economy', 'Executive Economy'), ('Business', 'Business')], default='Select', max_length=200),
        ),
        migrations.AlterField(
            model_name='domestic',
            name='From',
            field=models.CharField(choices=[('Karachi-Jinnah Intl. (KHI)', 'Karachi-Jinnah Intl. (KHI)'), ('Bahawalpur(BHV)', 'Bahawalpur(BHV)'), ('Chitral(CJL)', 'Chitral(CJL)'), ('Dalbandin(DBA)', 'Dalbandin(DBA)'), ('Dera Ghazi Khan Intl(DEA)', 'Dera Ghazi Khan Intl(DEA)'), ('Dera Ismail khan(DSK)', 'Dera Ismail khan(DSK)'), ('Faislabad Intl(LYP)', 'Faislabad Intl(LYP)'), ('Gilgit(GIL)', 'Gilgit(GIL)'), ('Gwadar Intl.(GWD)', 'Gwadar Intl.(GWD)'), ('Islamabad Intl(ISB)', 'Islamabad Intl(ISB)'), ('Lahore Intl (LHE)', 'Lahore Intl (LHE)'), ('Moenjodaro(MJD)', 'Moenjodaro(MJD)'), ('Multan Intl.(MUX)', 'Multan Intl.(MUX)'), ('Nawabshah Airport(WNS)', 'Nawabshah Airport(WNS)'), ('Panjgur(PJG)', 'Panjgur(PJG)'), ('Peshawar Intl(PEW)', 'Peshawar Intl(PEW)'), ('Quetta Intl(UET)', 'Quetta Intl(UET)'), ('Rahim Yar khan(RYK)', 'Rahim Yar khan(RYK)'), ('Sialkot Intl(SKT)', 'Sialkot Intl(SKT)'), ('Skardu Intl(SKT)', 'Skardu Intl(SKT)'), ('Sukkur(SKZ)', 'Sukkur(SKZ)'), ('Turbat Intl(TUK)', 'Turbat Intl(TUK)'), ('Zhob(PZH)', 'Zhob(PZH)'), ('Select', 'Select')], default='Select', max_length=200),
        ),
        migrations.AlterField(
            model_name='domestic',
            name='To',
            field=models.CharField(choices=[('Karachi-Jinnah Intl. (KHI)', 'Karachi-Jinnah Intl. (KHI)'), ('Bahawalpur(BHV)', 'Bahawalpur(BHV)'), ('Chitral(CJL)', 'Chitral(CJL)'), ('Dalbandin(DBA)', 'Dalbandin(DBA)'), ('Dera Ghazi Khan Intl(DEA)', 'Dera Ghazi Khan Intl(DEA)'), ('Dera Ismail khan(DSK)', 'Dera Ismail khan(DSK)'), ('Faislabad Intl(LYP)', 'Faislabad Intl(LYP)'), ('Gilgit(GIL)', 'Gilgit(GIL)'), ('Gwadar Intl.(GWD)', 'Gwadar Intl.(GWD)'), ('Islamabad Intl(ISB)', 'Islamabad Intl(ISB)'), ('Lahore Intl (LHE)', 'Lahore Intl (LHE)'), ('Moenjodaro(MJD)', 'Moenjodaro(MJD)'), ('Multan Intl.(MUX)', 'Multan Intl.(MUX)'), ('Nawabshah Airport(WNS)', 'Nawabshah Airport(WNS)'), ('Panjgur(PJG)', 'Panjgur(PJG)'), ('Peshawar Intl(PEW)', 'Peshawar Intl(PEW)'), ('Quetta Intl(UET)', 'Quetta Intl(UET)'), ('Rahim Yar khan(RYK)', 'Rahim Yar khan(RYK)'), ('Sialkot Intl(SKT)', 'Sialkot Intl(SKT)'), ('Skardu Intl(SKT)', 'Skardu Intl(SKT)'), ('Sukkur(SKZ)', 'Sukkur(SKZ)'), ('Turbat Intl(TUK)', 'Turbat Intl(TUK)'), ('Zhob(PZH)', 'Zhob(PZH)'), ('Select', 'Select')], default='Select', max_length=200),
        ),
        migrations.AlterField(
            model_name='domestic',
            name='Type',
            field=models.CharField(choices=[('Select', 'Select'), ('Return', 'Return'), ('Oneway', 'Oneway')], default='Select', max_length=100),
        ),
        migrations.AlterField(
            model_name='international',
            name='Cabin',
            field=models.CharField(choices=[('Select', 'Select'), ('Economy', 'Economy'), ('Executive Economy', 'Executive Economy'), ('Business', 'Business')], default='Select', max_length=200),
        ),
        migrations.AlterField(
            model_name='international',
            name='Type',
            field=models.CharField(choices=[('Select', 'Select'), ('Return', 'Return'), ('Oneway', 'Oneway')], default='Select', max_length=100),
        ),
    ]
