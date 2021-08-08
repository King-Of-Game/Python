#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# __author__ : YiXuan
# __date__ : 1/7/2021 3:16 PM
# __software__ : PyCharm

from decimal import Decimal, ROUND_HALF_UP


if __name__ == '__main__':
    float1 = 1.345
    print(Decimal(str(float1)).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP))