from django.db.models import Model, IntegerField
from apps.binance.models import AbstractBaseMinimalSellPriceModel, AbstractBasePriceStampModel


class IndexMinimalSellPriceModel(AbstractBaseMinimalSellPriceModel):
    buy_amount = IntegerField(verbose_name='purchased amount', null=True, blank=True)

    class Meta(AbstractBaseMinimalSellPriceModel.Meta):
        db_table = 'index_minimal_sell_price'


class IndexPriceStampModel(Model):
    class Meta(AbstractBasePriceStampModel.Meta):
        db_table = 'index_price_stamp'
