# mETaL

## References

Task №1: Create Team

Task №2: GitHub Repo

Task №3: https://docs.google.com/presentation/d/1FlMaD3UYV3isiqQ4khlfJ4fg2SOmUeGApOc7ZTPYI9U/edit?usp=sharing

Task №4: https://docs.google.com/document/d/1ilmZWZ4-yEUfUanzLw11iRW2gQ4b2FEnqN64QAGmVkU/edit?usp=sharing

Task №5: https://docs.google.com/presentation/d/1qOqScX0XhQLIA76nCZpglLcfXFSS5KNsb52CblAUeOU/edit?usp=sharing

## Team

Name: Micro SD<br/>
Group: МСПИН241<br/>
Members:
   * Abrosov Sergey  
   * Anisin Aleksandr  
   * Lanin George  
   * Malysh Igor  
   * Pan Zhengwu

## Introduction

Ensuring high data quality and availability is crucial for applications operating within our framework. Our extension for VS Code utilizes “data modules,” which are stored either on Amazon S3 or in a relational database management system (RDBMS). Each data module is defined by metadata compatible with JSON-LD, a collection protocol, and versioned data. The ETL (Extract, Transform, Load) service is designed to pull data from internal corporate systems, perform extensive cleansing, merging, anonymization, and transformation of the data, and subsequently upload it to create a new version of the data module. These processed data modules are then readily available for use by machine learning applications deployed within the framework.

## Stakeholders

* Data Scientist  
* Data Engineer  
* Developers and Engineers  
* Project Managers

## Features

### 1. Multistage Data Cleansing

Multistage data cleansing is a process where data undergoes a series of transformations to improve its quality. This involves removing duplicates, correcting errors, normalizing data, and other cleansing steps described below. This feature helps create accurate and consistent datasets.

**Detailed Description:**

* **Removing Duplicates:** When the dataset contains multiple records for the same entity, the ETL system identifies duplicates and suggests removing them based on a unique identifier.  
* **Correcting Errors:** When the dataset contains misspelled words or inconsistent data formats, the system corrects errors by referring to a predefined dictionary or format rules.  
* **Normalizing Data:** When data comes from multiple sources with varying formats, the ETL system standardizes the data to a single format, ensuring consistency across all records.  
* **Standardizing Categories:** When the dataset contains categories with variations, the ETL system standardizes similar categories into a single format to unify the data.

### 2. Data Anonymization and Masking

Data anonymization and masking involve modifying data to protect personally identifiable information (PII) while retaining its utility for analysis.

**Detailed Description:**

* **Anonymization:** When the dataset contains personal data (such as names or phone numbers), the system anonymizes the data by removing or replacing sensitive information with pseudonyms or hashed values.  
* **Masking:** When the dataset needs to retain readability but hide sensitive information, the system masks the data, showing only partial values, such as displaying the last four digits of a credit card number.  

### 3. Data Merging

Data merging is the process of combining data from multiple sources into a unified dataset.

**Detailed Description:**  

* **Merging Data:** When data comes from multiple sources, such as two .csv files, the system merges them by matching records based on a unique identifier. If conflicts arise, such as mismatching identifiers, the system returns an error or requests user intervention.

### 4. Metadata and Protocol Management

Metadata and protocol management involves storing and managing metadata in a structured format and ensuring that data collection adheres to defined protocols.

**Detailed Description:**

* **Storing Metadata:** When a dataset is processed, the system generates and stores metadata in JSON-LD format that describes its schema, origin, and any transformations applied.  

### 5. Data Quality

Data quality analysis ensures that the imported data meets specific quality standards through various validation tests.

**Detailed Description:**

* **Null Value Test:** When the system encounters missing or null values in critical fields, it flags them for correction or applies predefined rules such as imputation or deletion.  
* **String Patterns Test:** When the system detects that fields requiring a specific format, such as emails, do not conform, it flags these entries for review or correction.  
* **Imbalanced Class Test:** When the system detects a class imbalance in a classification problem, it suggests techniques like oversampling or undersampling to address the imbalance, ensuring balanced data distribution.

### 6. Compatibility

The ETL service must be compatible with two formats: JSON and CSV. This ensures that the software can ingest data from various sources and export processed data in formats easily consumed by other systems.

**Detailed Description:**

* **Importing JSON:** When the system processes a complex JSON file with nested arrays or objects, it parses the data and flattens the relevant fields for easier processing.  
* **Importing CSV:** When a CSV file is imported, the system detects different delimiters (such as commas or semicolons) and properly handles header rows for accurate data interpretation.  
* **Exporting Data:** When the data has been processed, the system exports it in either JSON or CSV formats, based on the user’s selection.

### 7. Logging and Audit Trails

Logging and audit trails involve tracking the history of data processing steps to ensure transparency, traceability, and accountability.

**Detailed Description:**

* **Logging Data Processing:** When the system processes data (such as removing duplicates or correcting errors), it automatically logs each action, noting the type of transformation applied, the affected records, and the timestamp.
* **Audit Trail for User Actions:** When a user performs manual actions (such as resolving a conflict during data merging or correcting flagged errors), the system records the action, along with the user’s identity and timestamp, for audit purposes.
* **Viewing Logs:** When a user requests, the system displays a detailed log of all data transformations, showing a step-by-step breakdown of actions applied to the dataset for transparency and review.

## Constraints

1. **Disaster Recovery**  
   ETL service must recover automatically after a failure.

2. **Maintainability**  
   Updates and patches should be applied without causing significant downtime.

3. **Usability**  
   The system interface should be intuitive for users with varying technical backgrounds.

4. **Portability**  
   ETL service must run as a VS Code extension, compatible with the required VS Code version (TBD).
