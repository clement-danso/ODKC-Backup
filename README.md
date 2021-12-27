### ODKC Backup With AWS S3
This aims to employ the use of AWS S3 as a backup storage.
## Table of contents
* [Pre-requisites](#pre-requisites)
* [Download Backup Scripts](#Download-Backup-Scripts)
* [Install python 2.7, pip, and AWS CLI](#Install-python-2-7--pip--and-AWS-CLI)
* [Configure AWS CLI](#Configure-AWS-CLI)
* [Create an S3 Bucket on AWS](#Create-an-S3-Bucket-on-AWS)
* [Setup cron jobs to run scripts](#Setup-cron-jobs-to-run-scripts)

## Pre-requisites
* ODK Central URL
* Administrator account on ODK Central, with credentials readily available
* Create an AWS IAM User ([Procedure](https://aws.amazon.com/getting-started/hands-on/backup-to-s3-cli/))
* Access Key ID, and Secret Access Key in the credentials file downloaded from creating the AWS IAM User.


## Download Backup Scripts
* Run:
```
$ git clone https://github.com/clement-danso/ODKC-Backup.git
$ cd ODKC-Backup
```

* Open to the backup script to input administrator credentials for the user that will perform the backup:
```
$ nano ODKC-backup.py
```
* And update the following fields with administrator credentials

#variables
Central_url: 
Passphrase:

NB: This passphrase will be used to encrypt the backup file, and will subsequently be needed to decrypt it during a backup restoration.
INCLUDE THE https:// part of the server URL


#Login and Session API calling
Email:
Password:

NB: This password is the login password

Press CTRL+x to save and close



## Install python 2.7, pip, and AWS CLI
* While you’re still in ‘ODKC-Backup’ directory, install python 2.7,  pip and AWS CLI with the env_setup.sh script
```
$ bash env_setup.sh
```

## Configure AWS CLI
The AWS CLI has already been installed from the script you run. To configure it,
* Type the command below and press Enter.
```
$ aws configure
```
* Enter the following when prompted:
_AWS Access Key ID [None]:_ enter the Access Key Id from the credentials.csv file you downloaded in ‘Create an AWS IAM User’ step.  
**Note: this should look something like _AKIAPWINCOKAO3U4FWTN_**  
_AWS Secret Access Key [None]:_ enter the Secret Access Key from the credentials.csv file you downloaded in Create an AWS IAM User’ step.  
**Note: this should look something like _5dqQFBaGuPNf5z7NhFrgou4V5JJNaWPy1XFzBfX3_**  
_Default region name [None]: enter us-east-1_  
_Default output format [None]: enter json_  

## Create an S3 Bucket on AWS
If you do not have one, you can create one by running :
```
$ aws s3 mb s3://name_of_bucket
```
_Note: bucket naming has some restrictions; one of those restrictions is that bucket names must be globally unique (e.g. two different AWS users can not have the same bucket name)_

* Now open the ‘ODKC-backup.sh’ file
```
$ nano ODKC-backup.sh
```
* On the last line (AWS Command), replace name_of_bucket with the **name of the bucket** you just created on AWS S3, or replace it with an already existing bucket name you already have.


## Setup cron jobs to run scripts
* To schedule cron tasks to run the ODKC-backup.sh script periodically, run:
```
$ aws s3 mb s3://name_of_bucket
```

* At the very bottom, schedule the cron job in the format _***** command_
For example if you want backups to be made hourly:
```
0 * * * * bash /home/quoda/ODKC-Backup/ODKC_backup.sh
```
This will run the job hourly.

* Again set up a cron task to run the **backup_upload.sh** file 10-15 mins after ODK-backup.sh is run
This will move the backup file downloaded to the Central server to the AWS S3 bucket configured.

```
10 * * * * bash /home/quoda/ODK-Backup/backup_upload.sh
```

This will run this job 10-15 mins after every hour.
