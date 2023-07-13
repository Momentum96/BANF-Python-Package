# v0.0.1
Import packages created by banf_sendreceive, override name  

# v0.0.2
Remove AWS Credential in Code for use boto3 package.  
(use AWS Credential in users credentials file. (~/.aws/credentials))

# v0.0.3
add install_requires & update keyowrds

# v0.0.4
Update install_requires to include more than just that version, rather than limiting it to a single version.

# v0.0.5
Remove packages from install_requirements that are specific to the windows os.

# v0.0.6
Update data_preprocessing/preprocessing.py  
- change lookupS3Objects, importS3Objects file type from csv to parquet.