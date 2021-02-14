#!/usr/bin/env groovy 
pipeline {
  agent any
  triggers {
    cron('0 * * * *')
  }
  stages{
    stage('Install packages'){
      steps{
        sh 'pip install -r requirements'
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
