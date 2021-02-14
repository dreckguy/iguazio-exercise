#!/usr/bin/env groovy 
pipeline {
  agent any
  triggers {
    pollSCM('0 * * * *')
  }
  stages{
    stage('Install packages'){
      steps{
        sh 'pip install -r requirements.txt'
      }
    }
    stage('Run script'){

      steps{
withCredentials([usernamePassword(credentialsId: 'open-weather', usernameVariable: 'USERNAME', passwordVariable: 'API_KEY')]) {              
              sh "python weather.py ${API_KEY}"
            }          
      }
    }
       
  }
}
