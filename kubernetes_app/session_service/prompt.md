# Step 1: Analyze Frameworks

You are an expert software architect evaluating microservices frameworks for **(GOAL_NAME)**.

### Context:
You are an expert software architect evaluating microservices frameworks for **(GOAL_NAME)**.
You need to choose frameworks from the following list: https://github.com/mfornos/awesome-microservices.  
The selected frameworks should meet the following **technical requirement**: **(TECH_REQUIREMENT)**.  
Your primary goal is to find frameworks that excel in building scalable and efficient systems for **(GOAL_NAME)**.

### Informations, Resources
- **(ADDITIONAL_INFORMATIONS)**

### Task:
1. Analyze the frameworks from the GitHub list.
2. Shortlist the **two most suitable frameworks** for **(GOAL_NAME)**, based on the following criteria:
   - Ease of setup and learning.
   - Scalability and performance potential.
   - Documentation quality.
   - Community activity (GitHub stars, updates, etc.).
   - **(ADDITIONAL_CRITERIA)**

### Output Format:
Provide your output in the following structure:
1. Framework Name.
2. Key Features (3 bullet points).
3. Brief Justification (1-2 sentences).
4. **(ADDITIONAL_CRITERIA_OUTPUT_FORMAT)**

Constraints:
- Do not exceed two frameworks.
- Frameworks must match **(TECH_REQUIREMENT)** and align with **(GOAL_NAME)**.
- **(ADDITIONAL_CONSTRAINTS)**


# Step 2: Implementation
For the **(SELECTED_FRAMEWORKS)** frameworks, write a basic "{SERVICE}" program. Ensure:
1. Provide the openapi yml
2. Include all necessary setup instructions (e.g., dependencies to install).
3. Provide the command to run the program.

Commands
1. /fix - fix the code with certain description
2. /add - add a new feature with certain description
3. /remove - remove a feature with certain description
4. /run - give the instruction to run the code
5. /unit-test - give the instruction to write unit test for the code
6. /lint - give the instruction to lint the code
7. /overview - give the overview of the code
    - flag `-a` give the overview of all files
    - flag `-f` give the overview of a certain file
    - flag `-c` give the overview of a certain class
    - flag `-m` give the overview of a certain method
    - flag `-v` give the overview of a certain variable

#### Chain of Thought for Code Generation:
1. Identify the simplest way to create an HTTP server in the framework.
2. Outline the steps to install dependencies and set up the environment.
3. Generate clean and beginner-friendly code.

#### Example Output:
**Framework**: FastAPI  
- **Setup**:
  ```bash
  pip install fastapi uvicorn

	•	Code:

File location: `main.py`
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


	•	Run Command:
```

Run

```bash
uvicorn main:app --reload
```


