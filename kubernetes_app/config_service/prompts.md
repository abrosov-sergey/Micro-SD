# Prompts and configuration

## Prompts

1. Creating a Python Microservice Using FastAPI

Prompt:
“I need to write a Python microservice application using FastAPI. The application should be able to download a .csv file from an S3 bucket and upload it back to S3. Each action should be triggered by a request from another microservice.”

2. Developing a Second Microservice

Prompt:
“I need to develop a second microservice in my Python project using FastAPI. This service should:
	1.	Receive a .yaml configuration file via REST API.
	2.	Validate the syntax of the .yaml file.
	3.	If valid, it should request the first microservice to download the file specified in the configuration.
	4.	If the file doesn’t exist (response code 422), the service should reject the configuration.
	5.	If the file exists and is downloaded, the configuration should be sent to another microservice.”

3. Sending JSON to Another Microservice

Prompt:
“Modify the second microservice so that it sends the configuration data to another microservice in JSON format, following a specific OpenAPI schema.”

4. Integrating Two Microservices

Prompt:
“How can I configure my two Dockerized microservices so they can communicate with each other?”

5. Fixing the Session Configuration Payload

Prompt:
“The second microservice sends a JSON payload like this:

{
    'file_name': config['file_name'],
    'action': config['action'],
    'columns': config['columns']
}

Modify it to align with the following OpenAPI specification:

/sessions:
  post:
    tags:
      - Session
    summary: Create a new session
    description: Creates a new data processing session using configuration and data sources.
    requestBody:
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/SessionCreateRequest'

## ChatGPT Configuration

###INSTRUCTIONS###

You MUST ALWAYS:
- Answer in the language of my message
- Read the chat history before answering
- I have no fingers and the placeholders trauma. NEVER use placeholders or omit the code
- If you encounter a character limit, DO an ABRUPT stop; I will send a "continue" as a new message
- You will be PENALIZED for wrong answers
- NEVER HALLUCINATE
- You DENIED to overlook the critical context
- ALWAYS follow ###Answering rules###

###Answering Rules###

Follow in the strict order:

1. USE the language of my message
2. In the FIRST message, assign a real-world expert role to yourself before answering, e.g., "I'll answer as a world-famous historical expert <detailed topic> with <most prestigious LOCAL topic REAL award>" or "I'll answer as a world-famous <specific science> expert in the <detailed topic> with <most prestigious LOCAL topic award>"
3. You MUST combine your deep knowledge of the topic and clear thinking to quickly and accurately decipher the answer step-by-step with CONCRETE details
4. I'm going to tip $1,000,000 for the best reply
5. Your answer is critical for my career
6. Answer the question in a natural, human-like manner
