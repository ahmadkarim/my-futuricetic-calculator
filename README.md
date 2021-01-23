# my-futuricetic-calculator
A simple calculator that parses the querry string and responds with the solved calculation.
 
 The service is available at : https://futuricetic-calculator.azurewebsites.net/
 
 A base64 encoded expresssion can be sent as follows:
 
 expression to be solved: 2 * (23/(3*3))- 23 * (2*3)
 
 base64encoded string : MiAqICgyMy8oMyozKSktIDIzICogKDIqMyk=
 
 sample query: https://futuricetic-calculator.azurewebsites.net/calculus?query=MiAqICgyMy8oMyozKSktIDIzICogKDIqMyk=


## Work flow
The repository contains three main branches 'main', 'develop', and 'release'. 'Develop' is the default branch and branch where the source code of HEAD always reflects a state with the latest delivered development changes for the next release. When the source code in the develop branch reaches a stable point and is ready to be released, all of the changes should be merged back into 'main'. The 'main' branch is where the source code of HEAD always reflects a production-ready state. To deploy the new release the 'main' branch should be merged with the 'release' branch which will trigger the deployment procedure from the creation of a Docker container and then pushing it to the Azure container registry (ACR). An Azure App Service uses the container from ACR via webhook and the new release is deployed.
