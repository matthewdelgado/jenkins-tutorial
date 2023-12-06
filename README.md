# Jenkins Automated Test Execution Tutorial

This tutorial provides a step-by-step guide on how to set up and use Jenkins to run automated tests using the provided Jenkins pipeline job. The pipeline job is designed to checkout source code from a GitHub repository and run pytest tests. Follow the instructions below to get started.

## Prerequisites

Before you begin, ensure that you have the following prerequisites in place:

- Jenkins server installed and running.
- Jenkins Git plugin and Pipeline plugin installed on your Jenkins server.
- A GitHub repository containing the source code and pytest tests that you want to execute.

## Step 1: Create a New Jenkins Pipeline Job

1. Log in to your Jenkins server.

2. Click on "New Item" to create a new Jenkins job.

3. Enter a name for your job (e.g., "Automated Tests").

4. Select "Pipeline" as the job type, and click on "OK."

## Step 2: Configure the Jenkins Pipeline

In the Jenkins job configuration, follow these steps:

1. In the "Pipeline" section, select "Pipeline script" as the definition.

2. Copy and paste the provided Jenkins pipeline script into the "Script" text area.

   ```groovy
   pipeline {
       agent any

       stages {
           stage('Checkout') {
               steps {
                   // Checkout source code repository
                   checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/matthewdelgado/jenkins-tutorial.git']])
               }
           }

           stage('Run Tests') {
               steps {
                   // Run pytest tests
                   sh 'pytest'
               }
           }
       }
   }
   ```

3. Click on "Save" to save the job configuration.

## Step 3: Build the Jenkins Pipeline

1. In the Jenkins dashboard, find the job you just created (e.g., "Automated Tests").

2. Click on the job name to open its details page.

3. Click on "Build Now" to trigger the pipeline execution.

## Step 4: Monitor the Pipeline Execution

You can monitor the progress of the pipeline job by clicking on the job name and then selecting "Console Output." This will display the console log, showing the progress of each stage and the pytest test results.

## Conclusion

Congratulations! You have successfully set up and executed automated tests using Jenkins and the provided pipeline job. You can customize the pipeline script further to fit the specific requirements of your project, such as specifying different Git branches or test commands.

Feel free to explore more Jenkins features and plugins to enhance your continuous integration and delivery processes.
