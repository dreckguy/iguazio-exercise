#!/usr/bin/env groovy 
pipeline {
  agent any
  triggers {
    pollSCM('* * * * *')
  }
  stages{
    stage('Check'){

      steps{
            withCredentials([usernameColonPassword(credentialsId: 'mylogin', variable: 'USERPASS')]) {
              echo "${USERPASS}"
              sh 'python script.py'
            }          
      }
    }
       
  }
}
