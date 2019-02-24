from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class AbstractBaseMinimalSellPriceModel(models.Model):
    price = models.FloatField(verbose_name='everage price for buying', null=True, blank=True)
    buy_price = models.FloatField(verbose_name='buy price', null=True, blank=True)
    buy_amount = models.FloatField(verbose_name='purchased amount', null=True, blank=True)

    class Meta:
        abstract = True
        verbose_name = 'Minimal sell price'


class AbstractBasePriceStamp(models.Model):
    created = models.DateTimeField(verbose_name='stock exchange price timestamp', null=True, blank=True)
    price = models.FloatField(verbose_name='price rate', null=True, blank=True)

    class Meta:
        abstract = True
        verbose_name = 'Price stamp'


class BinanceMinimalSellPriceModel(AbstractBaseMinimalSellPriceModel):
    class Meta(AbstractBaseMinimalSellPriceModel.Meta):
        db_table = 'binance_minimal_sell_price'


class BinancePriceStamp(AbstractBasePriceStamp):
    class Meta(AbstractBasePriceStamp.Meta):
        db_table = 'binance_price_stamp'


class IndexMinimalSellPriceModel(AbstractBaseMinimalSellPriceModel):
    buy_amount = models.IntegerField(verbose_name='purchased amount', null=True, blank=True)

    class Meta(AbstractBaseMinimalSellPriceModel.Meta):
        db_table = 'index_minimal_sell_price'


class IndexPriceStamp(models.Model):
    class Meta(AbstractBasePriceStamp.Meta):
        db_table = 'index_price_stamp'
