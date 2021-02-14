#!/usr/bin/env groovy 
pipeline {
  agent any
  triggers {
    pollSCM('* * * * *')
  }
  stages{
    stage('Check'){

       steps{
          sh 'python script.py'
  }
      
}
       
}

  
}
