# -*- coding: utf-8 -*-
#
# Copyright 2017 Ricequant, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ...utils.repr import property_repr
from ...environment import Environment


class BasePosition(object):

    __repr__ = property_repr

    def __init__(self, order_book_id):
        self._order_book_id = order_book_id

    def get_state(self):
        raise NotImplementedError

    def set_state(self, state):
        raise NotImplementedError

    @property
    def order_book_id(self):
        return self._order_book_id

    @property
    def market_value(self):
        """
        [float] 当前仓位市值
        """
        raise NotImplementedError

    @property
    def transaction_cost(self):
        raise NotImplementedError

    @property
    def type(self):
        raise NotImplementedError

    @property
    def last_price(self):
        return Environment.get_instance().get_last_price(self._order_book_id)

    # -- Function
    def is_de_listed(self):
        """
        判断合约是否过期
        """
        instrument = Environment.get_instance().get_instrument(self._order_book_id)
        current_date = Environment.get_instance().trading_dt
        if instrument.de_listed_date is not None and current_date >= instrument.de_listed_date:
            return True
        return False

    def apply_settlement(self):
        raise NotImplementedError

    def apply_trade(self, trade):
        raise NotImplementedError
