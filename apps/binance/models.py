from django.db import models


class AbstractBaseMinimalSellPriceModel(models.Model):
    price = models.FloatField(verbose_name='everage price for buying', null=True, blank=True)
    buy_price = models.FloatField(verbose_name='buy price', null=True, blank=True)
    buy_amount = models.FloatField(verbose_name='purchased amount', null=True, blank=True)

    class Meta:
        abstract = True
        verbose_name = 'Minimal sell price'


class AbstractBasePriceStampModel(models.Model):
    created = models.DateTimeField(verbose_name='stock exchange price timestamp', null=True, blank=True)
    price = models.FloatField(verbose_name='price rate', null=True, blank=True)

    class Meta:
        abstract = True
        verbose_name = 'Price stamp'


class BinanceMinimalSellPriceModel(AbstractBaseMinimalSellPriceModel):
    class Meta(AbstractBaseMinimalSellPriceModel.Meta):
        db_table = 'binance_minimal_sell_price'


class BinancePriceStampModel(AbstractBasePriceStampModel):
    class Meta(AbstractBasePriceStampModel.Meta):
        db_table = 'binance_price_stamp'
