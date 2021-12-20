#!/bin/bash


cd ODKC-Backup

python2 /home/quoda/ODKC-Backup/ODKC_backup.py



sleep 5s

# get name of last file
lastbackupfile=`ls -Art | tail -n 1`

# upload the latest backup to the server
aws s3 cp $lastbackupfile s3://name_of_bucket/


