import jenkins #Python-Jenkins
import pout

username = 'dkr20262'
password = 'Ankara35'
server = jenkins.Jenkins('http://ci-bit/',username='dkr20262',password='Ankara35')

#   https://python-jenkins.readthedocs.io/en/latest/api.html

user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))

print (server.jobs_count())

jobs = server.get_jobs()
pout.v(jobs)
#
# print(server.get_job("aky-be-pipeline-prod").get_last_buildnumber())
    
last_build_number = server.get_job_info('aky-be-pipeline-prod')['lastCompletedBuild']['name']
print (last_build_number)
#build_info = server.get_build_info('aky-be-pipeline-prod', last_build_number)
#build_info

def b_time():
    for key,job in server.iteritems():
        build_time(job)
    return(0)


def get_last_buildno(job_name):
    #j = Jenkins(JENKINS_URL, requester=Requester(username, password, baseurl=JENKINS_URL, ssl_verify=False))
    j = jenkins.Jenkins('http://ci-bit/', ssl_verify=False)
    try:
        return j.get_job(job_name).get_last_good_build().buildno
    except jenkins.custom_exceptions.NoBuildData:
        return j.get_job(job_name).get_last_build().buildno
    except jenkins.custom_exceptions.UnknownJob:
        raise

# Get all builds
jobs = server.get_all_jobs(folder_depth=None)
for job in jobs:
    print(job['fullname'])

info = server.get_job_info('job-name')
# Passed
print(info['lastCompletedBuild'])
# Unstable
print(info['lastUnstableBuild'])
# Failed
print(info['lastFailedBuild'])

info2 = server.get_job_info('job-name')
# Loop over builds
builds = info['builds']
for build in builds:
    for build in builds:
        print(server.get_build_info('job-name', build['number']))

"""
# get all jobs from the specific view
jobs = server.get_jobs(view_name='View Name')
print jobs


def __init__(self,username,password):
        self.username = username
        self.password = password
    # def getJobLastBuild(self):          #Last Build Number
    last_build_number = server.get_job_info('aky-be-pipeline-prod')['lastCompletedBuild']['number']
    print (last_build_number)
    print(server.get_job("aky-be-pipeline-prod").get_last_buildnumber())

build_info = server.get_build_info('aky-be-pipeline-prod', last_build_number)
print build_info
"""
