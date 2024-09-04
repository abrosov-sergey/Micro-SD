# mETaL

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

Multistage data cleansing is a process where data undergoes a series of transformations to improve its quality. This involves removing duplicates, correcting errors, normalizing data, and other cleansing steps described below. This feature helps create accurate and consistent dataset.

**Detailed Description:**

* **Removing Duplicates:** If the dataset contains multiple records for the same entity (e.g., customer data with the same email address), the ETL system should identify and suggest removing duplicate entries.  
* **Correcting Errors:** Suppose a dataset contains misspelled words or incorrect data formats (e.g., phone numbers formatted inconsistently). The software could automatically correct these errors by referring to a predefined dictionary.  
* **Normalizing Data:** If data comes from multiple sources with different formats (e.g., date formats like `MM/DD/YYYY` and `DD-MM-YYYY`), normalization would standardize all dates to a single format.  
* **Standardizing Categories:** In a dataset containing product categories with slight variations (e.g., "electronics," "Electronics," "Elec."), the ETL software would standardize these variations to a single category.

### 2. Data Anonymization and Masking

Data anonymization and masking involve modifying data to protect personally identifiable information (PII) while retaining the utility of the data for analysis or other purposes. Anonymization removes PII completely, while masking replaces it with obfuscated data.

**Detailed Description:**

* **Anonymization:** When processing a dataset that includes customer names, addresses, and phone numbers, the software could anonymize this data by removing or replacing names and phone numbers with hashed values or pseudonyms.  
* **Masking:** In cases where data needs to be readable but secure, such as showing only the last four digits of a bank card number (`1234-4545-6789-2344` to `XXXX-XXXX-XXXX-2344`), the software could mask sensitive parts of the data.  
* **Tokenization:** Replacing sensitive data with a token that maps to the original data but is meaningless if intercepted. For example, a credit card number might be replaced with a token like "Token1234" during analysis.

### 3. Data Merging

Data merging is the process of combining data from multiple sources into a single, coherent dataset.

**Detailed Description:** If data comes from two .csv files, the ETL software should combine these datasets by matching records based on a unique identifier, such as an ID. If there’s conflicting information (e.g., different IDs), the software returns an error.

### 4. Metadata and Protocol Management

Metadata and protocol management involves storing and managing metadata in a structured format like JSON-LD, and ensuring that data collection and processing adhere to predefined protocols. This helps in understanding the data’s context, provenance, and usage constraints.

**Detailed Description:**

* **Storing Metadata:** For each dataset processed by the ETL, the software should generate and store metadata that describes the data’s schema, origin, processing history, and any transformations applied. This metadata should be stored in JSON-LD format for compatibility with web standards.  
* **Automated Documentation:** Automatically generate a JSON-LD document for each processed dataset, detailing the steps taken during ETL, the sources of the data, and any transformations applied.

### 5. Data Quality

Data quality analysis ensures that the data imported into the ETL process meets specific quality standards. The software should perform various tests to identify issues such as missing values, inconsistent patterns, and imbalances in data distribution.

**Detailed Description:**

* **Null Value Test:** The software should scan the dataset for missing or null values in critical fields and either flag these for correction or handle them according to predefined rules (e.g., imputation, deletion).  
* **String Patterns Test:** For fields that should follow a specific format (e.g., email addresses, phone numbers), the ETL tool should validate the pattern and flag entries that do not conform.  
* **Imbalanced Class Test:** In a classification problem, the software should check for class imbalance (e.g., 90% of data belonging to one class) and suggest techniques such as oversampling, undersampling, or synthetic data generation to address it.

### 6. Compatibility

The ETL service must be compatible with 2 formats: JSON and CSV. This ensures that the software can ingest data from various sources and export processed data in a format that other systems can easily consume.

**Detailed description:**

* **Importing JSON:** The software should be able to parse complex JSON structures, including nested arrays and objects. For example, when importing a JSON file with customer orders, the ETL should extract and flatten relevant fields for easier processing.  
* **Importing CSV:** The tool should handle different delimiters (commas, semicolons). It should also detect and handle header rows.  
* **Exporting Data:** After processing, the software should allow exporting processed data in JSON or CSV formats.\]

## Constraints

1. Disaster Recovery  
   The ETL service must support automatic recovery after failures.  
2. Maintainability  
   The system should be easy to maintain and update. Updates and patches should be deployable without significant downtime or the need for a complete system restart.  
3. Usability  
   The system interface should be intuitive for users with different technical backgrounds.  
4. Portability  
   ETL Service should run as a VS Code Extension. Required VS Code version: _TBD_
