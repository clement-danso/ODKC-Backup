#!/bin/bash

#########################################
# Copying recent backup to S3 bucket and deleting the file to prevent storage consumption. This script will copy
# recent backup file downloaded, into a remote s3 bucket, and delete the backup from the central server.

#########################################

# Copying backup to AWS S3 bucket

cd ODKC-Backup

# find last backup file added
lastbackupfile=`ls -Art | tail -n 1`

# delete lastbackup file from server storage
rm -rf $lastbackupfile
