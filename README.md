# jenkins-python-calculator

This project demonstrates **Continuous Integration (CI) with Jenkins** for a Python-based calculator application. The pipeline automates code checkout, builds dependencies, runs tests, and sends notifications.

## Project Overview

This repository contains a simple **Python Calculator application** that performs basic arithmetic operations. The **Jenkins pipeline** is set up to automatically **detect code changes on GitHub**, execute test cases, and display results.

### **Technologies Used**
- **Python** - Application and testing
- **GitHub** - Code repository
- **Jenkins** - CI/CD automation
- **Git** - Version control
- **pytest** - Unit testing framework


## Pipeline Stages

The Jenkins pipeline includes the following **automated CI/CD stages**:

1. **Checkout** - Pulls the latest code from GitHub
2. **Build** - Installs dependencies using `pip install -r requirements.txt`
3. **Test** - Runs unit tests using `pytest`
4. **Notification** - Displays build success or failure

## Setup Instructions

### **1. Clone the Repository**
```bash
git clone https://github.com/yaminimerugu/jenkins-python-calculator.git
cd jenkins-python-calculator

### **2. Install Dependencies**
pip install -r requirements.txt

### **3. Run Test Locally**
pytest tests/


## Jenkins Setup

### **1️⃣ Install Jenkins**
1. Download & install **Jenkins** from [Jenkins official site](https://www.jenkins.io/download/).
2. Start Jenkins and unlock it using the **admin password** found in:
   ```plaintext
   C:\ProgramData\Jenkins\.jenkins\secrets\initialAdminPassword

   2️⃣ Install Required Plugins
In Jenkins Dashboard → Manage Jenkins → Plugins, install:
✅ Git Plugin (for repository access)
✅ Pipeline Plugin (for Jenkinsfile execution)
✅ GitHub Integration Plugin (for polling GitHub changes)

3️⃣ Configure GitHub Credentials in Jenkins
Go to Jenkins → Manage Jenkins → Credentials
Add a GitHub Personal Access Token:
Scope: repo
Permissions: Read & Write access
In Jenkins → Manage Jenkins → Configure System:
Set GitHub API URL:
plaintext
Copy
Edit
https://api.github.com/
Add your GitHub credentials under "GitHub Server" section

Configuring GitHub Integration (Polling Approach)
Step 1: Create a Pipeline Job in Jenkins
Go to Jenkins Dashboard → New Item
Select Pipeline and name it Calculator-Pipeline
Under Pipeline Definition, choose Pipeline script from SCM
Repository URL:
plaintext
Copy
Edit
https://github.com/yaminimerugu/jenkins-python-calculator.git
Branch: main
Script Path: Jenkinsfile
Step 2: Enable Poll SCM in Jenkins
In Jenkins → Pipeline Job → Configure
Enable Poll SCM and set the schedule:
Copy
Edit
H/5 * * * *
(Jenkins will check GitHub for new commits every 5 minutes.)
Save and apply changes.


 Jenkins Pipeline Configuration
Pipeline Stages
The pipeline runs the following stages:
1️⃣ Checkout - Pulls the latest code from GitHub
2️⃣ Build - Installs dependencies using pip install -r requirements.txt
3️⃣ Test - Runs unit tests using pytest
4️⃣ Notification - Displays build success or failure


