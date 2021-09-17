
from jenkinsapi.jenkins import Jenkins

def get_server_instance():
    jenkins_url = 'http://ci-bit/'
    server = Jenkins(jenkins_url, username='dkr20262', password='Ankara35')
    return server

if __name__ == '__main__':
    print (get_server_instance().version)

# get_latest_build , get_latest_complete_build , get_latest_test_results , get_timestamp()
#, 
##############################

print(server.get_job("aky-be-pipeline-prod").get_last_buildnumber())

server.get_jobs_info("aky-be-pipeline-prod")
server.get_job
server.get_data
server.get_jobs
print(server.get_jobs_list)
server.get_jenkins_obj
server.get_queue
