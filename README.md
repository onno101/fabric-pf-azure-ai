# Structured and Unstructured Fabric Data in Promptflow in Azure AI 


## Overview
This repo is conataining a prompt flow that is able to ground answers based on structured and unstrured data from Fabric. The structured data is queried through a Fabric AI Skills Endpoint. The unstructured data is coming from Azure AI Search. 

## Features
- **Azure AI Integration**: Utilizes Azure AI services for natural language processing and understanding.
- **Structured Data Handling**: Efficiently processes and retrieves information from structured data sources.
- **Unstructured Data Handling**: Capable of understanding and extracting information from unstructured data.
- **Prompt Flow**: Implements a sophisticated prompt flow to manage conversations and ensure coherent interactions.

## Getting Started

### Prerequisites
- Azure Account
- Fabric F64 license
- Azure and Fabric L100/L200 knowledge
- git
 
### Configuration
1. Create a Fabric Lakehouse in your preferred method
1. Set up your Azure AI environment in the Azure portal:
    - Create an Azure AI resource in your Azure portal.
    - Create an Azure AI project in your Azure AI resource 
    - Create Azure AI Search in your Azure portal.
1. Create the connections and deploy the models in Azure AI
    - Create the data connection to the Lakehouse from AI Studio on the 'Data' page on the left plane
    - Create connection to AI Search from AI Studio from the 'Connections' page on Hub-level
    - Create model deployment for an embeddings model (e.g. text-embedding-ada-002) on the 'Deployments' page on the left plane
    - Create model deployment for gpt model (e.g. gpt-4o-mini) on de 'Deployments' page on the left plane
1. Import the data into Fabric
    - Import structured data into the Gold Lakehouse [according to this documentation](https://learn.microsoft.com/en-us/fabric/data-science/ai-skill-scenario#create-a-lakehouse-with-adventureworksdw)
    - Import the unstructured data in the bronze layer that can be found in `data/unstructured`
    - Convert the unstructured data to markdown using the Notebook in the `src/markdown-pdf` folder
1. Create the AI Skill
    - Follow the instructions like [described in the Microsoft Documentation](https://learn.microsoft.com/en-us/fabric/data-science/ai-skill-scenario#create-an-ai-skill)
1. Create the search index
    - In you AI project in AI Studio, navigate to 'Indexes' in the left pane
    - Click 'create new index'
    - Use the "Data in Azure AI Studio" and select the earlier made Connection to the Fabric data
    - Use the connection to the AI Search you connected earlier
    - Use the embedding model to create a vector embedding.
1. Import the prompt flow
    - Create a new prompt flow in the AI Studio UI and select: 'Upload from local'
    - Select the `src\Structured + Unstructured AI Skill` folder and import it into prompt flow
    - Make sure to recheck all connections in the prompt flow when imported
1. Connect AI Skill 
    - In the 'Connections' pane in the AI Studio Hub, create a 'custom connection'
    - Add the following variables to the custom connection
    ![sceenshot_connection](image.png)
1. Test and debug the AI Skill
    - When ready, deploy it to an endpoint and start interacting from anywhere through the API endpoint



## Project Structure
- `src/`: Contains the source code for the prompt flow and a notebook to convert pdfs to markdown.
- `data/`: Includes structured and unstructured data samples.
- `README.md`: Project documentation.

## Contributing
Contributions are welcome! Please read the contributing guidelines for more details.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements
- Azure AI
- Microsoft
- Fabric Conference Sweden September 2024
- Fabric AI Product Marketing Management Team 

## Contact
For any questions or suggestions, please contact use the Issues section

