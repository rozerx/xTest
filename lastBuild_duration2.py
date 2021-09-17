import jenkins #Python-Jenkins
import requests
import json
import time

username = 'dkr20262'
password = 'Ankara35'

server = jenkins.Jenkins('http://ci-bit/',username='dkr20262',password='Ankara35')

user = server.get_whoami()
version = server.get_version()
print('Hello %s from Jenkins %s' % (user['fullName'], version))
jobsCount = server.jobs_count()
print ('Jobs count %s' % jobsCount)
theJob = server.get_job_info('aky-be-pipeline-prod', 0, True)
print("JOB INFO %s" % theJob)

last_build_number = server.get_job_info('aky-be-pipeline-prod')['lastCompletedBuild']['number']
print("Job's last build number %s" % last_build_number)

theTime = server.get_job_info('aky-be-pipeline-prod')['lastCompletedBuild']['timestamp']

print("Job's TIMESTAP %s" % theTime)



"""
class DurationMetrics:
    username = 'dkr20262'
    password = 'Ankara35'
    buildDurations = []
    buildTimestamps = []
    def __init__(self,username,password):
        self.username = username
        self.password = password
    def getJobDuration(self):
        # TODO: get job duration
        jenkinsJobs = self.server.get_all_jobs()
        #print(jenkinsJobs)
        theJob = self.server.get_job_info('aky-be-pipeline-prod', 0, True)
        print(theJob)
        theJobBuilds = theJob.get('builds')
        for build in theJobBuilds:
            buildNumber = build.get('number')
            print(buildNumber)    
            buildInfo = self.server.get_build_info('aky-be-pipeline-prod', buildNumber)
            print(buildInfo)
            
            
            buildTimestamp = buildInfo.get('timestamp')
            self.buildTimestamps.append(buildTimestamp)
    def connectToJenkins(self):
        # TODO: connect to Jenkins server
        self.server = jenkins.Jenkins('http://ci-bit/', username=self.username, password=self.password)
        user = self.server.get_whoami()
        version = self.server.get_version()
        print('Hello %s from Jenkins %s' % (user['fullName'], version))
    def convertTimestamps(self):
        dates = []
        for timestamp in self.buildTimestamps:
            dateTimeObj = datetime.fromtimestamp((timestamp / 1000))
            dates.append(dateTimeObj)
        return dates  

def main(argv):
    username = 'dkr20262'
    password = 'Ankara35'
    try:
        opts, args = getopt.getopt(argv, "hu:p:", ["username=", "password="])
    except getopt.GetoptError:
        print
        'python test02.py -u <username> -p <password>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print
            'python test02.py -u <username> -p <password>'
            sys.exit()
        elif opt in ("-u", "--username"):
            username = arg
        elif opt in ("-p", "--password"):
            password = arg
    durationMetrics = DurationMetrics(username,password)
    durationMetrics.connectToJenkins()
    print(durationMetrics.getJobDuration())
    

if __name__ == "__main__":
   main(sys.argv[1:])


     """
