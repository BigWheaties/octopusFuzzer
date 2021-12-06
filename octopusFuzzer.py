'''BROWSER = 'chrome'
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()'''
#input: python3 octopusFuzzer.py numFiles
#all inputs are assumed to be correctly formatted internally and when the function is called

''' Declare functions '''
# a function to expand all container divs on the page
def expandDivs():
    for i in range(0, 20):
        try:
            driver.find_element_by_xpath("//button[@aria-expanded='false']").click()
        except:
            #do nothing, just prevents errors
            
# a function to produce ASCII fuzz 
def fuzz(minChars, maxChars):
    numChars = random.randint(minChars, maxChars)
    tempFuzz = ""
    for i in range(numChars):
        tempChar = chr(random.randint(0, 255))
        tempFuzz = tempFuzz + tempChar 
    return tempFuzz
        
# a function to fuzz a YAML file for deployment
def fuzzDeployment(driver):
    # expand page
    expandDivs()
    
    # select deployment as resource type
    try:
        driver.find_element_by_xpath("//input[@value='Deployment']").click() 
    except:
        print("ERROR: FAILED TO SELECT DEPLOYMENT RESOURCE TYPE")
        
    # enter details for deployment
    try:
        deploymentName = driver.find_element_by_name('Deployment name')
        deploymentName.sendKeys(fuzz(0, 50))
        
        numReplicas = driver.find_element_by_name('Replicas')
        numReplicas.sendKeys(fuzz(0, 50))
        
        revisionLimit = driver.find_element_by_name('Revision history limit')
        revisionLimit.sendKeys(fuzz(0, 50))
        
        progressionDeadline = driver.find_element_by_name('Progression deadline in seconds')
        progressionDeadline.sendKeys(fuzz(0, 50))
        
        terminationGracePeriod = driver.find_element_by_name('Pod termination grace period in seconds')
        terminationGracePeriod.sendKeys(fuzz(0, 50))
        
        numLabels = random.randint(0, 5)
        for i in range(numLabels):
            try:
                driver.find_element_by_xpath("//button[@title='Add Label']").click() 
                labelNameTarget = driver.find_element_by_xpath("//button[@name='Name' and @value='']")
                labelNameTarget.sendKeys(fuzz(0, 50))
                labelValueTarget = driver.find_element_by_xpath("//button[@name='Value']")
                labelValueTarget.sendKeys(fuzz(0, 50))
            except:
                print("ERROR: FAILED TO PROPERLY CREATE LABELS IN DEPLOYMENT DETAILS")
    except:
        print("ERROR: FAILED TO PROPERLY ENTER DETAILS FOR DEPLOYMENT")
    
    # select deployment strategy
    try:
        deploymentStrategyInt = random.randint(0, 1)
        if deploymentStrategyInt == 0:
            driver.find_element_by_xpath("//input[@value='Recreate']").click() 
        if deploymentStrategyInt == 1:
            driver.find_element_by_xpath("//input[@value='RollingUpdate']").click()
            driver.find_element_by_name("Max Unavailable").sendKeys(fuzz(0, 50))
            driver.find_element_by_name("Max Surge").sendKeys(fuzz(0, 50))
    except:
        print("ERROR: DEPLOYMENT STRATEGY SELECTION FAILED")
        
    # add volumes
    try:
        driver.find_element_by_xpath("//button[@title='Add Volume']").click() 
        # ! - TODO the window that pops up has things to address
    except:
        print("ERROR: VOLUME ADDITION FAILED")
        
    # manage containers
    try:
        # ! - EXTREMELY COMPLEX AND DIFFICULT
    
    # manage DNS policy
    try:
        dnsPolicySelection = random.randint(0, 3)
        if dnsPolicySelection == 0:
            labelValueTarget = driver.find_element_by_xpath("//input[@value='ClusterFirst']")
        elif dnsPolicySelection == 1:
            labelValueTarget = driver.find_element_by_xpath("//input[@value='ClusterFirstWithHostNet']")
        elif dnsPolicySelection == 2:
            labelValueTarget = driver.find_element_by_xpath("//input[@value='Default']")
        elif dnsPolicySelection == 3:
            labelValueTarget = driver.find_element_by_xpath("//input[@value='None']")
        labelValueTarget.click()
    except:
        print("ERROR: DNS POLICY SELECTION FAILED")
    
    # manage DNS config
    try:
        # ! - TODO
    except:
        print("ERROR: DNS CONFIG FAILED")
    
    # manage host networking
    try:
        # ! - difficult selection process, TODO
    except:
        print("ERROR: FAILED TO PROPERLY SELECT A HOST NETWORKING OPTION")

    # manage pod security context
    try:
        # ! - TODO, VERY COMPLEX
    except:
        print("ERROR: POD SECURITY CONTEXT CONFIGURATION FAILED")
    
    # manage pod affinity/anti-affinity
    try:
        # ! - TODO, VERY COMPLEX
    except:
        print("ERROR: POD AFFINITY CONFIGURATION FAILED")
    
    # manage node affinity
    try:
        # ! - TODO, VERY COMPLEX
    except:
        print("ERROR: NODE AFFINITY CONFIGURATION FAILED")
    
    # manage tolerations
    try:
        # ! - TODO, VERY COMPLEX
    except:
        print("ERROR: TOLERATION CONFIGURATION FAILED")
    
    # manage pod annotations
    try:
        # ! - TODO, functionally similar to other name/value sections
    except:
        print("ERROR: POD ANNOTATION FAILED")
    
    # manage deployment annotations
    try:
        # ! - TODO, functionally similar to other name/value sections
    except:
        print("ERROR: DEPLOYMENT ANNOTATION FAILED")
    
    # manage service account name
    try:
        driver.find_element_by_name("Service Account Name").sendKeys(fuzz(0, 50))
    except:
        print("ERROR: SERVICE ACCOUNT NAME CONFIGURATION FAILED")
    
    # manage readiness gates
    try:
        driver.find_element_by_name("Pod readiness gates").sendKeys(fuzz(0, 50))
    except:
        print("ERROR: FAILED TO CONFIGURE READINESS GATES")
        
'''    # IMPLEMENT AT A LATER DATE
# a function to fuzz a YAML file for a stateful set
def fuzzStatefulSet():

# a function to fuzz a YAML file for a daemon
def fuzzDaemonSet():
'''

''' Main program '''
# import libraries
import selenium 
import sys
import os
import random

# declare variables
loopCounter = 0

# get user input
numFilesNeeded = int(sys.argv[1])

# generate random seed
random.seed()

# initiate Selenium objects
            # ! - TODO


# create the desired number of fuzzed files
while loopCounter < numFilesNeeded:
    # get page for fuzzing
            # ! - TODO
    
    fuzzDeployment(driver)
    ''' # IMPLEMENT AT A LATER DATE
    # pick and call a fuzzing function
    fuzzSelection = random.randint(0, 2)
    if fuzzSelection == 0:
        fuzzDeployment()
    elif fuzzSelection == 1:
        fuzzStatefulSet()
    elif fuzzSelection == 2:
        fuzzDaemonSet()
    '''
    
    # fetch generated YAML file from webpage and save it
    webpageOutput = str(driver.find_element_by_id('yaml'))
    newFileName = "fuzz" + str(loopCounter) + ".yaml"
    try:
        print("Creating file " + str(loopCounter + 1) + "...")
        newFilePointer = open(newFileName, "w")
        newFilePointer.write(webpageOutput)
        newFilePointer.close()
    except:
        print("ERROR: FAILED TO CREATE THE FILE " + newFileName + ".  NO INFORMATION WRITTEN TO TARGET.")
        
    loopCounter += 1
