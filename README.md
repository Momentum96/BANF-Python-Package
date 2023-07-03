A package of Python functions used by BANF's data scientists and developers.

# Requirements
- python 3
- aws credentials setting (for AWS S3)

# Installation
```bash
pip install banf
```
# Usage
```python
# import in python or ipython code
import banf
from banf.data_processing.preprocessing import ForMeasurement
```
## AWS Credentials Setting

You need to make a file named 'credentials' in '~/.aws' directory.  
in Windows, make directory at %UserProfile%\.aws  
in Linux, make directory at ~/.aws  

This Package use 'default' profile in credentials file.  
So, you must set 'default' profile in credentials file.

```bash
# credentials file sample

[default] ; default Profile section information

aws_access_key_id = YOUR_ACCESS_KEY1

aws_secret_access_key = YOUR_SECRET_KEY1
```

# Acknowledgments
## BANF R&D Team
---
- GW Jeon (BANF Co., Ltd. email : gwjeon@banf.co.kr)
- EG Kim (BANF Co., Ltd. email : egkim@banf.co.kr)
- DH Kim (BANF Co., Ltd. email : kim.donghun@banf.co.kr)