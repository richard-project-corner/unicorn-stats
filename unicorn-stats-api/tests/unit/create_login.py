import os

import boto3
import urllib
import json
import requests

def get_credentials(role_arn: str):
    ACCESS_KEY_ID = os.environ.get("ACCESS_KEY_ID")
    SECRET_ACCESS_KEY = os.environ.get("SECRET_ACCESS_KEY")
    
    dev = boto3.session.Session(
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=SECRET_ACCESS_KEY
    )
    sts_client = dev.client('sts')
    assume_role_response = sts_client.assume_role(
        RoleArn=role_arn,
        RoleSessionName='console-session',
        DurationSeconds=6*60*60,
    )
    credentials = assume_role_response['Credentials']
    return credentials

def main():
    REGION = os.environ.get("REGION")
    credentials = get_credentials(role_arn='arn:aws:iam::617267062318:role/Console-Role')
    json_credentials = {
        "sessionId": credentials['AccessKeyId'],
        "sessionKey": credentials['SecretAccessKey'],
        "sessionToken": credentials['SessionToken']
    }
    environment_url=f"https://{REGION}.console.aws.amazon.com"
    url_prefix=f"https://signin.aws.amazon.com/federation?Action=getSigninToken&Session={urllib.parse.quote(json.dumps(json_credentials))}"
    signin_token_response = requests.get(url_prefix)
    signin_link = f"""https://signin.aws.amazon.com/federation?Action=login&Destination={urllib.parse.quote(environment_url)}&SigninToken={signin_token_response.json()['SigninToken']}"""
    print(signin_link)

if __name__=="__main__":
    main()