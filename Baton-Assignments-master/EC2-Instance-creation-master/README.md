# EC2-Instance-Creation
This repository contains ansible playbook and python script. Ansible playbook will create  ec2 instance.  Python script will list all EC2 instances that belong to an AWS account. The script will take an optional parameter to specify the instance type and when provided, will list all instances of that particular type. When the parameter is ignored, then the script lists all EC2 instances across all types.

## Prerequisites

Below are the prerequisites to run this playbook.

  - Centos 7 or Redhat 7.
  - latest version of Ansible installed.
  
## Before run playbook

  - Make an AWS account
  - Create an IAM role and obtain your access and secret keys
  - Generate a public/private key pair

## Achieving below through Ansible Playbook

  - Create a security group for the environment and add the appropriate rules
  - Launch an EC2 instance based on the type and region
  - Wait for the SSH is up on Instance.
  - install apache
  - install aws-cli and boto3 using pip to run python script

## Installation

Ansible required Python module boto3 to communiate with AWS API. So, boto3 needs to be installed on your machine.

```
>> pip install boto boto3
```

Storing keys in Ansible vault.

After creating the IAM account, we'll need to store the AWS keys using Ansible vault to encrypt. 

```
>> ansible-vault create aws_keys.yml
#Add the your key details into this file like below and save.
aws_access_key: AKXXXXXXXXXXXXXXX3UA
aws_secret_key: iMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXnUt
```

#### Create key_pair with name "AWS-Ansible"

```
>> aws ec2 create-key-pair --key-name "AWS-Ansible"
```

#### Create ansible config file

Before running playbook create new ansible.cfg with below values for custom configuration of anisible playbook.

```
>> vi ansible.cfg

[defaults]
host_key_checking = False
private_key_file = /path/to/key-file/AWS-Ansible.pem
```
You can customize ec2-instance values by editing ec2-provisioning.yml along with this file.

#### Running Ansible playbook

```
>> ansible-playbook -i hosts --ask-vault-pass ec2-provisioning.yml

PLAY [local] ****************************************************************************************************************************************************************************************************************************************************************

TASK [Gathering Facts] *******************************************************************************************************************************************************************************************************************************************************
ok: [localhost]
.
.
.
.
.
.
PLAY RECAP *******************************************************************************************************************************************************************************************************************************************************************
localhost                  : ok=4    changed=1    unreachable=0    failed=0
```

# Running Python Script

This script will list all EC2 instances that belong to an AWS account. The script will take an optional parameter to specify the instance type and when provided, will list all instances of that particular type. When the parameter is ignored, then the script lists all EC2 instances across all types

Before run this script make sure you have pyhton3 installed with awscli and boto3 libraries on your machine. Above ansible playbook will do all of its configuration.
```
>> python list_instances.py <Optional Parameter to filter instance type>
```
E.g.
```
>> python list_instances.py
Instance #1, t2.small
Instance #2, t2.small
Instance #3, t2.medium
Instance #4, t2.medium
Instance #5, t2.large
```
```
>> python list_instances.py 't2.medium'
Instance #3, t2.medium
Instance #4, t2.medium
```
