from django.db import models


class BinanceMinimalSellPriceModel(models.Model):
    price = models.FloatField(verbose_name='everage price for buying', null=True, blank=True)
    buy_price = models.FloatField(verbose_name='buy price', null=True, blank=True)
    buy_amount = models.FloatField(verbose_name='purchased amount', null=True, blank=True)

    class Meta:
        db_table = 'binance_minimal_sell_price'


class BinancePriceStamp(models.Model):
    created = models.DateTimeField(verbose_name='stock exchange price timestamp', null=True, blank=True)
    price = models.FloatField(verbose_name='price rate', null=True, blank=True)

    class Meta:
        db_table = 'binance_price_stamp'


class IndexMinimalSellPriceModel(models.Model):
    price = models.FloatField(verbose_name='everage price for buying', null=True, blank=True)
    buy_price = models.FloatField(verbose_name='buy price', null=True, blank=True)
    buy_amount = models.IntegerField(verbose_name='purchased amount', null=True, blank=True)

    class Meta:
        db_table = 'index_minimal_sell_price'


class IndexPriceStamp(models.Model):
    created = models.DateTimeField(verbose_name='stock exchange price timestamp', null=True, blank=True)
    price = models.FloatField(verbose_name='price rate', null=True, blank=True)

    class Meta:
        db_table = 'index_price_stamp'

