import sys 
import boto3
ec2 = boto3.resource('ec2')
i=0
if len(sys.argv) > 1:
	for instance in ec2.instances.all():
		instance_type = instance.instance_type
		if instance.instance_type in sys.argv[1:]:
			i += 1
			print ("Instance #",i,",", instance.instance_type)
else:
	for instance in ec2.instances.all():
		i += 1
		print ("Instance #",i,",", instance.instance_type)