| Use Case                                                              | Cooperation Name                 | Used Roles                            | Candidate Classes that Play Them            |
| --------------------------------------------------------------------- | -------------------------------- | ------------------------------------- | ------------------------------------------- |
| 1\. Login using SSO                                                   | SSO Login Process                | User, Authenticator                   | User                                        |
| 2\. Authenticate User using SSO                                       | SSO Authentication               | User, Authenticator                   | User                                        |
| 3\. View Documentation about how to write config                      | Documentation Viewing            | User, DocumentationProvider           | User, Config                                |
| 4\. Upload Config YAML                                                | Config Uploading                 | User, ConfigManager                   | User, Config                                |
| 5\. Config validation status                                          | Config Validation                | ConfigValidator, User                 | Config, User                                |
| 6\. View the data result                                              | Data Result Viewing              | User, DataViewer                      | User, DataProcessorSession                  |
| 7\. Start data processing                                             | Data Processing Initiation       | User, DataProcessor                   | User, DataProcessorSession, DataTransformer |
| 8\. Get data processing status                                        | Data Processing Status Retrieval | User, StatusChecker                   | User, DataProcessorSession                  |
| 9-13. Get data processing \[Initial, Ready, Running, Success, Error\] | Data Processing Status Retrieval | User, StatusChecker                   | User, DataProcessorSession                  |
| 14\. Create new schema                                                | Schema Creation                  | User, SchemaDesigner                  | User, Schema                                |
| 15\. Read data from DB                                                | Data Reading                     | DataReader, ExternalDatabase          | DataTransformer, ExternalDB                 |
| 16\. Write data to DB                                                 | Data Writing                     | DataWriter, ExternalDatabase          | DataTransformer, ExternalDB                 |
| 17\. Accept the request for getting DB access credential              | Credential Request Approval      | CredentialManager, User               | IDRequestManager, User                      |
| 18\. Give credential after request approval                           | Credential Provisioning          | CredentialManager, User               | IDRequestManager, DBCredential, User        |
| 20\. Accept DB connection with credential (from IDP)                  | Credential-Based DB Connection   | ExternalDatabase, CredentialValidator | ExternalDB, DBCredential                    |
