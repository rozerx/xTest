# xTest
node {
    stage("Git Clone"){
        git credentialsId: 'GIT_HUB_CREDENTIALS',url:'https://github.com/rozerx/babootcampTest.git'
    }
    
    
    stage("Kubernetes DEV   Deployment"){
        script{
            env.DOCKER_BUILD_NUMBER=Jenkins.instance.getItem("dockerbuildtest").lastSuccessfulBuild.number
        }
        
        sh 'echo ${DOCKER_BUILD_NUMBER}'
        sh 'envsubst <./KubernetesYamls/dev/deployment.yaml | kubectl apply -f -'
        sh 'kubectl apply -f ./KubernetesYamls/dev/service.yaml'
        
    }
    stage("Kubernetes TEST   Deployment"){
        script{
            env.DOCKER_BUILD_NUMBER=Jenkins.instance.getItem("dockerbuildtest").lastSuccessfulBuild.number
        }
        
        sh 'echo ${DOCKER_BUILD_NUMBER}'
        sh 'envsubst <./KubernetesYamls/test/deployment.yaml | kubectl apply -f -'
        sh 'kubectl apply -f ./KubernetesYamls/test/service.yaml'
        
    }
    stage("Kubernetes PROD   Deployment"){
        
        def deployment = input (message:'PROD Deployment ?',ok:'ok', parameters:[booleanParam(defautlValue:true,description:'',name:'YES')])
        
        if (deployment == true){
            
            script{
            env.DOCKER_BUILD_NUMBER=Jenkins.instance.getItem("dockerbuildtest").lastSuccessfulBuild.number
            }
        
        sh 'echo ${DOCKER_BUILD_NUMBER}'
        sh 'envsubst <./KubernetesYamls/prod/deployment.yaml | kubectl apply -f -'
        sh 'kubectl apply -f ./KubernetesYamls/prod/service.yaml'
        
        }
        else{
            echo "Deployment Skipped"
        }
        
        
        
    }
}
