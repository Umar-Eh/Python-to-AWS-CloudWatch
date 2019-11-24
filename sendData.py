import boto3
import datetime
import time

cloudWatch = boto3.client('cloudwatch')

def sendMetricsToAWS(metric, value):
    responseData = cloudWatch.put_metric_data(
        Namespace='Position Data from RPI',
        MetricData=[
            {
                'MetricName': metric,
                'Dimensions': [
                    {
                        'Name': 'RPI Metric',
                        'Value': metric,
                    },
                ],
                'Timestamp': datetime.datetime.now(),
                'Unit': 'None',
                'Value': value,
            },
        ]
    )
    print("AWS Response to request:")
    print("------------------------")
    print(responseData)
    print()


# Example 

distance = [110, 120, 130, 140, 150, 160, 170, 180, 190, 200]

for index in range (0, len(distance)):
    sendMetricsToAWS("Distance from home", distance[index])
    # custom metrics may require a 60 sec wait between data points
    # requires further investigation
    sendMetricsToAWS
    time.sleep(60)
