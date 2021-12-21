#!/bin/bash

# get name of last file
lastbackupfile=`ls -Art | tail -n 1`

# upload the latest backup to the server
aws s3 mv $lastbackupfile s3://quodatrybucket/
