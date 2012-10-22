##############################################################################
#
# Copyright (C) TreborTech, Llc. 2012, all rights reserved.
#
##############################################################################

PYTHON=$(shell which python)
HERE=$(PWD)
PYWBEM_DIR=$(HERE)/src/pywbem-0.8.0
ZP_DIR=$(HERE)/ZenPacks/zenoss/EMC/base
LIB_DIR=$(ZP_DIR)/lib
BIN_DIR=$(ZP_DIR)/bin

default: egg

egg:
    # setup.py will call 'make build' before creating the egg
	python setup.py bdist_egg

build:

clean:
	rm -rf lib build dist
	rm -rf ZenPacks.zenoss.EMC.base.egg-info
	cd $(PYWBEM_DIR) ; rm -rf build dist *.egg-info