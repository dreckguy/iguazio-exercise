#!/usr/bin/env groovy 
pipeline {
  agent any
  triggers {
    pollSCM('* * * * *')
  }
  stages{
    stage('Check'){

      steps{
withCredentials([usernamePassword(credentialsId: 'amazon', usernameVariable: 'USERNAME', passwordVariable: 'API_KEY')]) {              
              sh "python script.py ${API_KEY}"
            }          
      }
    }
       
  }
}
