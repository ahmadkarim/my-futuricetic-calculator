# my-futuricetic-calculator
A simple calculator that parses the querry string and responds with the solved calculation.
 
 The service is available at : https://futuricetic-calculator.azurewebsites.net/
 
 A base64 encoded expresssion can be sent as follows:
 
 expression to be solved: 2 * (23/(3 * 3))- 23 * (2 * 3)
 
 base64encoded string : MiAqICgyMy8oMyozKSktIDIzICogKDIqMyk=
 
 sample query: https://futuricetic-calculator.azurewebsites.net/calculus?query=MiAqICgyMy8oMyozKSktIDIzICogKDIqMyk=


## Work flow
The repository contains three main branches 'main', 'develop', and 'release'. 'Develop' is the default branch and branch where the source code of HEAD always reflects a state with the latest delivered development changes for the next release. When the source code in the develop branch reaches a stable point and is ready to be released, all of the changes should be merged back into 'main'. The 'main' branch is where the source code of HEAD always reflects a production-ready state. To deploy the new release the 'main' branch should be merged with the 'release' branch which will trigger the deployment procedure from the creation of a Docker container and then pushing it to the Azure container registry (ACR). An Azure App Service uses the container from ACR via webhook and the new release is deployed.

## Deploying the container on Aure app service (with continuous deployment)

* Create a 'Resource-group' at Azure (To manage all the resources).
* Create Azure Container Registry (ACR) to push container images to this registry from Github.
* Create registry access keys at ACR and add them in the Github repository settings(Github secrets) and use them in the Github-Actions-Flow so that containers can be pushed to ACR. (see my-futuricetic-calculator/.github/workflows/main.yml)
* Create an 'App-Service' at Azure, assign it to the previously created resource group, use Docker for publishing by choosing 'Docker' in the publish option.
* After app service is successfully created, navigate to 'App-Service > Settings > Container Settings', here choose 'Azure Container Registry' as the image source, Select the previously created registry, then chose the image name and tag then save settings.
* For Continous deployment, turn on the option 'Continous deployment' by navigating to 'App-Service > Settings > Container Settings', Copy the webhook URL, then navigate to 'Container registry > Services > Webhooks', Then add a webhook here, give it a name and paste the Webhook URL link here. This will create a webhook and whenever a new container image is pushed to ACR it will be deployed to the APP-service.
