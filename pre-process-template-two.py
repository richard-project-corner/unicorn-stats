import string
import random

def main():
    with open(r'template_two.yaml', 'r') as file:
        with open('openapispec.yaml', 'r') as g:
            open_api_body = g.read()
            open_api_body = open_api_body.replace("\n","\n                  ")
            suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
            data = file.read()
            data = data.replace("PLACEHOLDER_ApiGatewayDeployment_PlACEHOLDER", f"Deployment{suffix}")
            data = data.replace("YAMLINSERT__PLACEHOLDER__YAMLINSERT", open_api_body)
    
    with open(r'template_out.yaml', 'w') as file:
        file.write(data)

if __name__ == "__main__":
    main()