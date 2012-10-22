######################################################################
#
# Copyright 2012 TreborTech, llc.  All Rights Reserved.
#
######################################################################

import Globals
import os
from Products.CMFCore.DirectoryView import registerDirectory
from Products.ZenModel.ZenPack import ZenPack as ZenPackBase

skinsDir = os.path.join(os.path.dirname(__file__), 'skins')
if os.path.isdir(skinsDir):
    registerDirectory(skinsDir, globals())


class ZenPack(ZenPackBase):

    def install(self, app):
        # productName is used in the UpdateCheck call to dev.zenoss.org to
        # identify what product is checking version.
        app.zport.dmd.productName = 'trebortechlayout'
        ZenPackBase.install(self, app)
        app = self.dmd.getPhysicalRoot()


    def remove(self, app, leaveObjects=False):
        if hasattr(app.zport.dmd, 'productName'):
            del app.zport.dmd.productName
        ZenPackBase.remove(self, app, leaveObjects)

