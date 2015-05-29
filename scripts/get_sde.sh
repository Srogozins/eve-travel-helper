#!/bin/bash
# Downloads and extracts CCP's EVE Online Static Data export

SDE_DIR=../SDE
archive=Mosaic_1.2_112318_db.zip

rm -r $SDE_DIR
mkdir $SDE_DIR
cd $SDE_DIR

wget http://cdn1.eveonline.com/data/$archive
unzip $archive
