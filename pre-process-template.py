import string
import random

def main():
    with open(r'template.yaml', 'r') as file:
        suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        data = file.read()
        data = data.replace("PLACEHOLDER_ApiGatewayDeployment_PlACEHOLDER", f"Deployment{suffix}")
    
    with open(r'template_out.yaml', 'w') as file:
        file.write(data)

if __name__ == "__main__":
    main()