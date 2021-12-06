# -*- coding: utf-8 -*-
"""
    @author  mruizq@unah.hn
    @version 0.1.0
    @date 2021/10/28
"""

from carmd import CarMD

class CarMDHandler:

    def __init__(self):
        self.account = None
        self.countRequests = 0

    def getCredits(self):
        return self.account.acct_credits()['data']['credits']

    def getAccount(self, authorization, partnerToken):
        self.account = CarMD(authorization, partnerToken)
        return self.account

    