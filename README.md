# Sending metrics to AWS CloudWatch through the boto3 AWS sdk for python on a raspberry pi #

### Instructions ###

#### Setting up AWS account ####

1. Go to https://aws.amazon.com and create a new AWS account (pick the free tier if needed).
2. Once the account is created, goto https://console.aws.amazon.com
3. In "Find Services, type 'IAM' without any quotes.
4. Click on the IAM link shown under the search bar which will take you to the IAM console.
5. Click on "users" in the left side-bar and then click on "Add User" button on the new page.
6. Enter username i.e. "rpiuser" and check the checkbox against "Programmatic Access".
   This ensures that the identity management client allows our code to access AWS services.
7. Click next and on the next screen, choose "Attach existing policies directly". In the "filter policies" field,
   type "cloudwatchfullaccess" and pick the resulting option by clicking on the checkbox. Click next.
8. Keep clicking next until you see the page with a success message along with an Access Key ID and a Secret Access Key.
9. Note down both of the keys for now.

#### Set-up on RPI ####

1. Download the boto3 sdk: pip3 install boto3 
2. In your home directory (use cd ~ to switch to it), creade the .aws directory: mkdir .aws
3. Create the credentials file: touch ~/.aws/credentials
4. Add the following information to the ~/.aws/credentials file:
   
   [default]
   aws-access_key_id = 'The access key id from step 8 of setting up AWS account'
   aws_secret_access_key = 'The secret access key from step 8 of setting up AWS account'

5. Create the config file: touch ~/.aws/config
6. Add the following information to the ~/.aws/config file:

   [default]
   region='Pick a region'
   
   For example, I have picked region='us-east-1'
   How to pick your region: go back to the AWS console home (just click on the AWS
   icon on the top left) and see what it says after home? in the url bar. That will
   be the default region.

#### Sending metrics ####

1. Run the sendData.py file and it will send some metrics to the AWS CloudWatch service with 1 minute 
   intervals. 
2. In your AWS console, type "cloudwatch" in Find Services and click on the resulting cloudwatch link.
3. Click on "metrics" in the left side-bar and then on "all metrics" at the bottom of the graph. 
4. Pick the "Position Data from RPI" and pick the "distance" metric. Click the checkbox.
5. Wait for a few minutes for data points to show up. The first time cloudwatch takes a while.
6. The code can be modified to send any metrics. In the "dashboard" link in the left sidebar, a dashboard can be 
   created in cloudwatch which can be configured to show certain metrics over time.
   
