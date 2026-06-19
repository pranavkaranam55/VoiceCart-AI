\# VoiceCart AI



\## Overview



VoiceCart AI is an AI-powered multilingual voice-based grocery ordering system that converts spoken customer requests into structured order data using OpenAI Whisper.



The project combines Artificial Intelligence, Speech Recognition, Cloud Deployment, Containerization, and DevOps practices to provide a complete end-to-end solution.



\---



\# Problem Statement



Traditional ordering systems require customers or operators to manually enter product information.



This introduces several challenges:



\* Manual typing consumes time.

\* Human errors occur while taking orders.

\* Telephone order management depends on operators.

\* Regional language users face accessibility issues.

\* Voice conversations are difficult to convert into structured data.



VoiceCart AI addresses these challenges by automatically converting voice commands into digital orders.







\# Solution



VoiceCart AI allows users to place orders using natural speech.



Example:



"I need two oil packets and one rice packet."



The system automatically:



\* Converts speech into text.

\* Detects the spoken language.

\* Extracts products and quantities.

\* Stores order information.

\* Updates dashboard statistics.



\---



\# Features



\* Voice-based ordering

\* Multilingual support

\* Automatic language detection

\* Speech-to-text conversion

\* Order extraction

\* Dashboard analytics

\* Demand prediction

\* CSV export

\* Excel export

\* PDF export

\* Cloud deployment

\* CI/CD integration



\---



\# AI Model Used



\## OpenAI Whisper Tiny



Whisper is a Transformer-based Automatic Speech Recognition (ASR) model developed by OpenAI.



\### Why Whisper?



\* Supports multilingual speech.

\* High transcription accuracy.

\* Automatic language detection.

\* Suitable for noisy environments.

\* CPU compatible.



\### Framework



PyTorch



\### Model Used



Whisper Tiny



\---



\# Speech Processing Pipeline



1\. User records audio.

2\. Audio is sent to the FastAPI backend.

3\. FFmpeg preprocesses audio.

4\. Whisper converts speech into text.

5\. Language is detected automatically.

6\. Order parser extracts products and quantities.

7\. Structured JSON is generated.

8\. Database stores order information.

9\. Dashboard and analytics are updated.



\---



\# Order Extraction



The parser extracts:



\* Product names

\* Quantities



Example:



Input:



I need two oil packets and one rice packet



Output:



Oil → 2



Rice → 1



\---



\# Database



SQLite is used to store:



\* Product

\* Quantity

\* Language

\* Status

\* Timestamp



\---



\# Dashboard Features



\* Total Orders

\* Revenue

\* Delivered Orders

\* Analytics

\* Weekly Sales

\* Top Products



\---



\# Report Generation



Supported formats:



\* CSV

\* Excel

\* PDF



\---



\# Tech Stack



\## Artificial Intelligence



\* OpenAI Whisper Tiny

\* PyTorch



\## Backend



\* FastAPI

\* Python



\## Frontend



\* React JS



\## Database



\* SQLite



\## Audio Processing



\* FFmpeg



\## Data Processing



\* Pandas

\* NumPy



\## Machine Learning



\* Scikit-learn



\## Report Generation



\* OpenPyXL

\* ReportLab



\---



\# DevOps Implementation



\## Version Control



Git and GitHub are used for source code management.



Benefits:



\* Source code backup

\* Version history tracking

\* Collaborative development



\---



\## Continuous Integration using Jenkins



Jenkins automates the build process.



Whenever code is pushed to GitHub:



\* Jenkins retrieves the latest source code.

\* The pipeline defined in Jenkinsfile is executed.

\* Build validation is performed.

\* Dependencies are verified.

\* The application is prepared for deployment.



This automation reduces manual effort and improves reliability.



\---



\## Containerization using Docker



Docker packages the application into portable containers.



Benefits:



\* Environment consistency

\* Simplified deployment

\* Portability

\* Reduced configuration issues



\---



\## Continuous Delivery



Every successful build produces deployable code.



This enables faster releases and reduces deployment risks.



\---







\### Frontend



Vercel



\### Backend



Railway



\---



\# Tools Used in DevOps



\* Git

\* GitHub

\* Jenkins

\* Docker

\* Railway

\* Vercel



\---



\# Project Structure



```text

VoiceCart-AI/

│

├── FrontEnd/

├── BackEnd/

├── Jenkins/

├── Jenkinsfile

├── docker-compose.yml

└── README.md

```



\---



\# Deployment Links



\## Frontend



https://voice-cart-ai.vercel.app



\## Backend API Documentation



https://voicecart-ai-production.up.railway.app/docs



\---



\# Future Enhancements



\* Faster Whisper

\* PostgreSQL

\* Authentication

\* Kubernetes

\* Prometheus Monitoring

\* Grafana Dashboards

\* LLM-based Order Extraction



\---



\# Conclusion



VoiceCart AI demonstrates how Artificial Intelligence and DevOps can be integrated to create a scalable voice-based ordering platform.



The project successfully combines:



\* Speech Recognition

\* Deep Learning

\* Docker

\* Jenkins CI/CD

\* Cloud Deployment

\* Database Management



to provide a complete end-to-end solution.



