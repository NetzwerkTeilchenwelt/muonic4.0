from ...common.CountRecord import CountRecord
from mongoengine import BooleanField, EmbeddedDocument, DecimalField, IntField


class CountRecordAdapter(EmbeddedDocument):
    valid = BooleanField()
    counts_ch0 = IntField()
    counts_ch1 = IntField()
    counts_ch2 = IntField()
    counts_ch3 = IntField()
    counts_trigger = IntField()
    counters_time = DecimalField()

    @staticmethod
    def get(rec):
        return CountRecordAdapter(valid=rec.valid,
                                  counts_ch0=rec.counts_ch0,
                                  counts_ch1=rec.counts_ch1,
                                  counts_ch2=rec.counts_ch2,
                                  counts_ch3=rec.counts_ch3,
                                  counts_trigger=rec.counts_trigger,
                                  counters_time=rec.counters_time)

    def set(self):
        rec = CountRecord("")
        rec.valid = self.valid
        rec.counts_ch0 = self.counts_ch0
        rec.counts_ch1 = self.counts_ch1
        rec.counts_ch2 = self.counts_ch2
        rec.counts_ch3 = self.counts_ch3
        rec.counts_trigger = self.counts_trigger
        rec.counters_time = self.counters_time
        return rec
