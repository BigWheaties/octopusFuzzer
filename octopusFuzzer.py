#input: python3 octopusFuzzer.py numFiles
    
''' Declare functions '''
# a function to expand all container divs on the page
def expandDivs():
    try:
        divsToExpand = driver.find_elements_by_class_name("style_clickable__2rbjz")
        for div in divsToExpand:
            div.click()
    except:
        print("ERROR: PROBLEM EXPANDING DIV")
            
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
        driver.find_element_by_xpath("//*[@id=\"app\"]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div[2]/div[1]/input").click() 
    except:
        print("ERROR: FAILED TO SELECT DEPLOYMENT RESOURCE TYPE")
        
    # enter details for deployment
    try:
        deploymentName = driver.find_element_by_name("Deployment name")
        deploymentName.clear()
        deploymentName.send_keys(fuzz(0, 50))

        numReplicas = driver.find_element_by_name("Replicas")
        numReplicas.clear()
        numReplicas.send_keys(fuzz(0, 50))
        
        revisionLimit = driver.find_element_by_name("Revision history limit")
        revisionLimit.clear()
        revisionLimit.send_keys(fuzz(0, 50))
        
        progressionDeadline = driver.find_element_by_name("Progression deadline in seconds")
        progressionDeadline.clear()
        progressionDeadline.send_keys(fuzz(0, 50))
        
        terminationGracePeriod = driver.find_element_by_name("Pod termination grace period in seconds")
        terminationGracePeriod.clear()
        terminationGracePeriod.send_keys(fuzz(0, 50))
        
        
        numLabels = random.randint(0, 5)
        if numLabels != 0:
            for i in range(numLabels):
                try:
                    driver.find_element_by_xpath("//button[@title='Add Label']").click() 
                    
                    if i == 0:
                        labelNameTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/span/div[1]/div[2]/div/div/div/div[16]/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div/div/div/input")
                        labelNameTarget.clear()
                        labelNameTarget.send_keys(fuzz(0, 50))
                        labelValueTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/span/div[1]/div[2]/div/div/div/div[16]/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div/div/div/input")
                        labelValueTarget.clear()
                        labelValueTarget.send_keys(fuzz(0, 50))
                    
                    elif i == 1:
                        labelNameTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/span/div[1]/div[2]/div/div/div/div[16]/div[2]/div[2]/div/div[1]/div[1]/div/div[1]/div/div/div/input")
                        labelNameTarget.clear()
                        labelNameTarget.send_keys(fuzz(0, 50))
                        labelValueTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/span/div[1]/div[2]/div/div/div/div[16]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div/div/div/input")
                        labelValueTarget.clear()
                        labelValueTarget.send_keys(fuzz(0, 50))
                        
                    elif i == 2:
                        labelNameTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/span/div[1]/div[2]/div/div/div/div[16]/div[2]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div/input")
                        labelNameTarget.clear()
                        labelNameTarget.send_keys(fuzz(0, 50))
                        labelValueTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/span/div[1]/div[2]/div/div/div/div[16]/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div/div/div/input")
                        labelValueTarget.clear()
                        labelValueTarget.send_keys(fuzz(0, 50))                    
                    elif i == 3:
                        labelNameTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/span/div[1]/div[2]/div/div/div/div[16]/div[2]/div[4]/div/div[1]/div[1]/div/div[1]/div/div/div/input")
                        labelNameTarget.clear()
                        labelNameTarget.send_keys(fuzz(0, 50))
                        labelValueTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/span/div[1]/div[2]/div/div/div/div[16]/div[2]/div[4]/div/div[1]/div[2]/div/div[1]/div/div/div/input")
                        labelValueTarget.clear()
                        labelValueTarget.send_keys(fuzz(0, 50))                    
                    elif i == 4:
                        labelNameTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/span/div[1]/div[2]/div/div/div/div[16]/div[2]/div[5]/div/div[1]/div[1]/div/div[1]/div/div/div/input")
                        labelNameTarget.clear()
                        labelNameTarget.send_keys(fuzz(0, 50))
                        labelValueTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/span/div[1]/div[2]/div/div/div/div[16]/div[2]/div[5]/div/div[1]/div[2]/div/div[1]/div/div/div/input")
                        labelValueTarget.clear()
                        labelValueTarget.send_keys(fuzz(0, 50))
                except:
                    print("ERROR: FAILED TO PROPERLY CREATE LABELS IN DEPLOYMENT DETAILS")
    except:
        print("ERROR: FAILED TO PROPERLY ENTER DETAILS FOR DEPLOYMENT")
    
    # select deployment strategy
    try:
        deploymentStrategyInt = random.randint(0, 1)
        if deploymentStrategyInt == 0:
            driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/span/div[2]/div[2]/div/div/div/div/div[2]/div[1]/input").click() 
        else:
            driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/span/div[2]/div[2]/div/div/div/div/div[2]/div[5]/input").click()
            maxUnavailableTarget = driver.find_element_by_name("Max Unavailable")
            maxUnavailableTarget.clear()
            maxUnavailableTarget.send_keys(fuzz(0, 50))
            maxSurgeTarget = driver.find_element_by_name("Max Surge")
            maxSurgeTarget.clear()
            maxSurgeTarget.send_keys(fuzz(0, 50))
    except:
        print("ERROR: DEPLOYMENT STRATEGY SELECTION FAILED")
        
    # add volumes
    try:
        numVolumes = random.randint(0, 5)
        for i in range(numVolumes):
            driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[2]/div[2]/div/div/div/div[3]/div[1]/div/button']").click() 
            
            volumeType = random.randint(0, 5)
            # config map
            if volumeType == 0:
                configMapOption = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[2]/div/div/div/div[1]/div/div/div/div[2]")
                configMapOption.click()
                configMapOption.send_keys(ENTER)
                configMapName = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/input")
                configMapName.clear()
                configMapName.send_keys(fuzz(0, 50))
                configMapNameName = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[2]/div/div/div/div[3]/div[1]/div[1]/div/div/div/input")
                configMapNameName.clear()
                configMapNameName.send_keys(fuzz(1, 50))
                # add item
                numItems = random.randint(0, 5)
                for i in range(numItems):
                    driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div/button").click()
                    
                    
                    if i == 0:
                        itemKeyTarget = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div/div/div/input")
                        itemKeyTarget.clear()
                        itemKeyTarget.send_keys(fuzz(0, 50))
                        itemPathTarget = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div/div/div/input")
                        itemPathTarget.clear()
                        itemPathTarget.send_keys(fuzz(0, 50))
                    
                    elif i == 1:
                        itemKeyTarget = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div[2]/div/div[1]/div[1]/div/div[1]/div/div/div/input")
                        itemKeyTarget.clear()
                        itemKeyTarget.send_keys(fuzz(0, 50))
                        itemPathTarget = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div/div/div/input")
                        itemPathTarget.clear()
                        itemPathTarget.send_keys(fuzz(0, 50))
                    elif i == 2:
                        itemKeyTarget = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div/input")
                        itemKeyTarget.clear()
                        itemKeyTarget.send_keys(fuzz(0, 50))
                        itemPathTarget = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div/div/div/input")
                        itemPathTarget.clear()
                        itemPathTarget.send_keys(fuzz(0, 50))
                    elif i == 3:
                        itemKeyTarget = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div[4]/div/div[1]/div[1]/div/div[1]/div/div/div/input")
                        itemKeyTarget.clear()
                        itemKeyTarget.send_keys(fuzz(0, 50))
                        itemPathTarget = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div[4]/div/div[1]/div[2]/div/div[1]/div/div/div/input")
                        itemPathTarget.clear()
                        itemPathTarget.send_keys(fuzz(0, 50))
                    elif i == 4:
                        itemKeyTarget = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div[5]/div/div[1]/div[1]/div/div[1]/div/div/div/input")
                        itemKeyTarget.clear()
                        itemKeyTarget.send_keys(fuzz(0, 50))
                        itemPathTarget = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[2]/div/div/div/div[3]/div[2]/div[2]/div[5]/div/div[1]/div[2]/div/div[1]/div/div/div/input")
                        itemPathTarget.clear()
                        itemPathTarget.send_keys(fuzz(0, 50))
            
            driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[3]/div[2]/div[2]/button").click()
            
            ''' not implemented due to time constraints
            # secret
            elif volumeType == 1:
                secretOption = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[2]/div/div/div/div[1]/div/div/div/div[2]")
                secretOption.click()
                secretOption.send_keys(ARROW_DOWN)
                secretOption.send_keys(ENTER)

            # empty dir
            elif volumeType == 2:
                Option = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[2]/div/div/div/div[1]/div/div/div/div[2]")
                Option.click()
                Option.send_keys(ARROW_DOWN)
                Option.send_keys(ARROW_DOWN)
                Option.send_keys(ENTER)       
                
            # host path
            elif volumeType == 3:
                Option = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[2]/div/div/div/div[1]/div/div/div/div[2]")
                Option.click()
                Option.send_keys(ARROW_DOWN)
                Option.send_keys(ARROW_DOWN)
                Option.send_keys(ARROW_DOWN)
                Option.send_keys(ENTER)
                
            # persistent volume claim
            elif volumeType == 4:
                Option = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[2]/div/div/div/div[1]/div/div/div/div[2]")
                Option.click()
                Option.send_keys(ARROW_DOWN)
                Option.send_keys(ARROW_DOWN)
                Option.send_keys(ARROW_DOWN)
                Option.send_keys(ARROW_DOWN)
                Option.send_keys(ENTER)
                
            # raw YAML
            elif volumeType == 5: 
                Option = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[2]/div/div/div/div[1]/div/div/div/div[2]")
                Option.click()
                Option.send_keys(ARROW_DOWN)
                Option.send_keys(ARROW_DOWN)
                Option.send_keys(ARROW_DOWN)
                Option.send_keys(ARROW_DOWN)
                Option.send_keys(ARROW_DOWN)
                Option.send_keys(ENTER)   
            '''
            
    except:
        print("ERROR: VOLUME ADDITION FAILED")
        
    # manage containers --- EXTREMELY COMPLEX AND DIFFICULT!  IMPLEMENT AT A LATER DATE

    # manage DNS policy
    try:
        dnsPolicySelectionInt = random.randint(0, 3)
        if dnsPolicySelectionInt == 0:
            dnsPolicySelectionChoice = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[4]/div[2]/div/div/div/div[1]/div[1]/div[2]/div[1]/input")
        elif dnsPolicySelectionInt == 1:
            dnsPolicySelectionChoice = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[4]/div[2]/div/div/div/div[1]/div[1]/div[2]/div[3]/input")
        elif dnsPolicySelectionInt == 2:
            dnsPolicySelectionChoice = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[4]/div[2]/div/div/div/div[1]/div[1]/div[2]/div[5]/input")
        elif dnsPolicySelectionInt == 3:
            dnsPolicySelectionChoice = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[4]/div[2]/div/div/div/div[1]/div[1]/div[2]/div[7]/input")
        dnsPolicySelectionChoice.click()
    except:
        print("ERROR: DNS POLICY SELECTION FAILED")
    
    # manage DNS config
    try:
        nameServerTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[5]/div[2]/div/div/div/div[1]/div[1]/div/div/div/textarea[1]")
        nameServerTarget.clear()
        nameServerTarget.send_keys(fuzz(0, 50))
        searchesTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[5]/div[2]/div/div/div/div[3]/div[1]/div/div/div/textarea[1]")
        searchesTarget.clear()
        searchesTarget.send_keys(fuzz(0, 50))
        try:
            numOptions = random.randint(0, 5)
            if numOptions != 0:
                for i in range(numOptions):
                    driver.find_element_by_xpath("").click() 
                        
                    if i == 0:
                        optionNameTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[5]/div[2]/div/div/div/div[5]/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div/div/div/input")
                        optionNameTarget.clear()
                        optionNameTarget.send_keys(fuzz(0, 50))
                        optionValueTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[5]/div[2]/div/div/div/div[5]/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div/div/div/input")
                        optionValueTarget.clear()
                        optionValueTarget.send_keys(fuzz(0, 50))
                        
                    elif i == 1:
                        optionNameTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[5]/div[2]/div/div/div/div[5]/div[2]/div[2]/div/div[1]/div[1]/div/div[1]/div/div/div/input")
                        optionNameTarget.clear()
                        optionNameTarget.send_keys(fuzz(0, 50))
                        optionValueTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[5]/div[2]/div/div/div/div[5]/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div/div/div/input")
                        optionValueTarget.clear()
                        optionValueTarget.send_keys(fuzz(0, 50))
                            
                    elif i == 2:
                        optionNameTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[5]/div[2]/div/div/div/div[5]/div[2]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div/input")
                        optionNameTarget.clear()
                        optionNameTarget.send_keys(fuzz(0, 50))
                        optionValueTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[5]/div[2]/div/div/div/div[5]/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div/div/div/input")
                        optionValueTarget.clear()
                        optionValueTarget.send_keys(fuzz(0, 50))                   
                    elif i == 3:
                        optionNameTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[5]/div[2]/div/div/div/div[5]/div[2]/div[4]/div/div[1]/div[1]/div/div[1]/div/div/div/input")
                        optionNameTarget.clear()
                        optionNameTarget.send_keys(fuzz(0, 50))
                        optionValueTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[5]/div[2]/div/div/div/div[5]/div[2]/div[4]/div/div[1]/div[2]/div/div[1]/div/div/div/input")
                        optionValueTarget.clear()
                        optionValueTarget.send_keys(fuzz(0, 50))                    
                    elif i == 4:
                        optionNameTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[5]/div[2]/div/div/div/div[5]/div[2]/div[5]/div/div[1]/div[1]/div/div[1]/div/div/div/input")
                        optionNameTarget.clear()
                        optionNameTarget.send_keys(fuzz(0, 50))
                        optionValueTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[5]/div[2]/div/div/div/div[5]/div[2]/div[5]/div/div[1]/div[2]/div/div[1]/div/div/div/input")
                        optionValueTarget.clear()
                        optionValueTarget.send_keys(fuzz(0, 50))
        except:
            print("ERROR: FAILED TO PROPERLY CREATE OPTIONS IN DNS CONFIG")
    except:
        print("ERROR: DNS CONFIG FAILED")
    
    # manage host networking
    try:
        hostNetworkingInt = random.randint(0, 1)
        if hostNetworkingInt == 0:
            hostNetworkingChoice = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[6]/div[2]/div/div/div/div[1]/div[1]/div[2]/div[1]/input")
        if hostNetworkingInt == 1:
            hostNetworkingChoice = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[6]/div[2]/div/div/div/div[1]/div[1]/div[2]/div[3]/input")
        hostNetworkingChoice.click()
    except:
        print("ERROR: FAILED TO PROPERLY SELECT A HOST NETWORKING OPTION")

    # manage pod security context
    #try:
        # ! - TODO, VERY COMPLEX
    #except:
    #    print("ERROR: POD SECURITY CONTEXT CONFIGURATION FAILED")
    
    # manage pod affinity/anti-affinity
    #try:
        # ! - TODO, VERY COMPLEX
    #except:
    #    print("ERROR: POD AFFINITY CONFIGURATION FAILED")
    
    # manage node affinity
    #try:
        # ! - TODO, VERY COMPLEX
    #except:
    #    print("ERROR: NODE AFFINITY CONFIGURATION FAILED")
    
    # manage tolerations
    try:
        numTolerations = random.randint(0, 5)
        for i in range(numTolerations):
            driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[10]/div[2]/div/div/div/div/div[1]/div/button").click()
            keyTarget = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[2]/div/div/div/div[2]/div[1]/div[1]/div/div/div/input")
            keyTarget.clear()
            keyTarget.send_keys(fuzz(0, 50))
            operatorTarget = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[2]/div/div/div/div[3]/div[1]/div[1]/div/div/div/input")
            operatorTarget.clear()
            operatorTarget.send_keys(fuzz(0, 50))
            tolerationValueTarget = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[2]/div/div/div/div[4]/div[1]/div[1]/div/div/div/input")
            tolerationValueTarget.clear()
            tolerationValueTarget.send_keys(fuzz(0, 50))
            effectTarget = driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[2]/div/div/div/div[5]/div[1]/div[1]/div/div/div/input")
            effectTarget.clear()
            effectTarget.send_keys(fuzz(0, 50))
            driver.find_element_by_xpath("/html/body/div[3]/div[3]/div/div/div[3]/div[2]/div[2]/button").click()
            
    except:
        print("ERROR: TOLERATION CONFIGURATION FAILED")
    
    # manage pod annotations
    try:
        numAnnotations = random.randint(0, 5)
        if numAnnotations != 0:
            for i in range(numAnnotations):
                driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[11]/div[2]/div/div/div/div/div[1]/div/button").click() 
                    
                if i == 0:
                    annotationNameTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[11]/div[2]/div/div/div/div/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div/div/div/input")
                    annotationNameTarget.clear()
                    annotationNameTarget.send_keys(fuzz(0, 50))
                    annotationValueTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[11]/div[2]/div/div/div/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div/div/div/input")
                    annotationValueTarget.clear()
                    annotationValueTarget.send_keys(fuzz(0, 50))
                    
                elif i == 1:
                    annotationNameTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[11]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div[1]/div/div[1]/div/div/div/input")
                    annotationNameTarget.clear()
                    annotationNameTarget.send_keys(fuzz(0, 50))
                    annotationValueTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[11]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div/div/div/input")
                    annotationValueTarget.clear()
                    annotationValueTarget.send_keys(fuzz(0, 50))
                        
                elif i == 2:
                    annotationNameTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[11]/div[2]/div/div/div/div/div[2]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div/input")
                    annotationNameTarget.clear()
                    annotationNameTarget.send_keys(fuzz(0, 50))
                    annotationValueTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[11]/div[2]/div/div/div/div/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div/div/div/input")
                    annotationValueTarget.clear()
                    annotationValueTarget.send_keys(fuzz(0, 50))                    
                elif i == 3:
                    annotationNameTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[11]/div[2]/div/div/div/div/div[2]/div[4]/div/div[1]/div[1]/div/div[1]/div/div/div/input")
                    annotationNameTarget.clear()
                    annotationNameTarget.send_keys(fuzz(0, 50))
                    annotationValueTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[11]/div[2]/div/div/div/div/div[2]/div[4]/div/div[1]/div[2]/div/div[1]/div/div/div/input")
                    annotationValueTarget.clear()
                    annotationValueTarget.send_keys(fuzz(0, 50))                    
                elif i == 4:
                    annotationNameTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[11]/div[2]/div/div/div/div/div[2]/div[5]/div/div[1]/div[1]/div/div[1]/div/div/div/input")
                    annotationNameTarget.clear()
                    annotationNameTarget.send_keys(fuzz(0, 50))
                    annotationValueTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[11]/div[2]/div/div/div/div/div[2]/div[5]/div/div[1]/div[2]/div/div[1]/div/div/div/input")
                    annotationValueTarget.clear()
                    annotationValueTarget.send_keys(fuzz(0, 50))
    except:
        print("ERROR: POD ANNOTATION FAILED")
    
    # manage deployment annotations
    try:
        numAnnotations = random.randint(0, 5)
        if numAnnotations != 0:
            for i in range(numAnnotations):
                driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[12]/div[2]/div/div/div/div/div[1]/div/button").click() 
                    
                if i == 0:
                    annotationNameTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[12]/div[2]/div/div/div/div/div[2]/div[1]/div/div[1]/div[1]/div/div[1]/div/div/div/input")
                    annotationNameTarget.clear()
                    annotationNameTarget.send_keys(fuzz(0, 50))
                    annotationValueTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[12]/div[2]/div/div/div/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div/div/div/input")
                    annotationValueTarget.clear()
                    annotationValueTarget.send_keys(fuzz(0, 50))
                    
                elif i == 1:
                    annotationNameTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[12]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div[1]/div/div[1]/div/div/div/input")
                    annotationNameTarget.clear()
                    annotationNameTarget.send_keys(fuzz(0, 50))
                    annotationValueTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[12]/div[2]/div/div/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div[1]/div/div/div/input")
                    annotationValueTarget.clear()
                    annotationValueTarget.send_keys(fuzz(0, 50))
                        
                elif i == 2:
                    annotationNameTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[12]/div[2]/div/div/div/div/div[2]/div[3]/div/div[1]/div[1]/div/div[1]/div/div/div/input")
                    annotationNameTarget.clear()
                    annotationNameTarget.send_keys(fuzz(0, 50))
                    annotationValueTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[12]/div[2]/div/div/div/div/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div/div/div/input")
                    annotationValueTarget.clear()
                    annotationValueTarget.send_keys(fuzz(0, 50))                    
                elif i == 3:
                    annotationNameTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[12]/div[2]/div/div/div/div/div[2]/div[4]/div/div[1]/div[1]/div/div[1]/div/div/div/input")
                    annotationNameTarget.clear()
                    annotationNameTarget.send_keys(fuzz(0, 50))
                    annotationValueTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[12]/div[2]/div/div/div/div/div[2]/div[4]/div/div[1]/div[2]/div/div[1]/div/div/div/input")
                    annotationValueTarget.clear()
                    annotationValueTarget.send_keys(fuzz(0, 50))                    
                elif i == 4:
                    annotationNameTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[12]/div[2]/div/div/div/div/div[2]/div[5]/div/div[1]/div[1]/div/div[1]/div/div/div/input")
                    annotationNameTarget.clear()
                    annotationNameTarget.send_keys(fuzz(0, 50))
                    annotationValueTarget = driver.find_element_by_xpath("/html/body/div[1]/div/div[2]/div/div[12]/div[2]/div/div/div/div/div[2]/div[5]/div/div[1]/div[2]/div/div[1]/div/div/div/input")
                    annotationValueTarget.clear()
                    annotationValueTarget.send_keys(fuzz(0, 50))
    except:
        print("ERROR: FAILED TO PROPERLY CREATE DEPLOYMENT ANNOTATIONS")
    
    # manage service account name
    try:
        serviceAccountNameTarget = driver.find_element_by_name("Service Account Name")
        serviceAccountNameTarget.clear()
        serviceAccountNameTarget.send_keys(fuzz(0, 50))
    except:
        print("ERROR: SERVICE ACCOUNT NAME CONFIGURATION FAILED")
    
    # manage readiness gates
    try:
        readinessGateTarget = driver.find_element_by_name("Pod readiness gates")
        readinessGateTarget.clear()
        readinessGateTarget.send_keys(fuzz(0, 50))
    except:
        print("ERROR: FAILED TO CONFIGURE READINESS GATES")
        
    # fetch generated YAML file from webpage and save it
    webpageOutput = driver.find_element_by_id('yaml').text
    newFileName = "fuzz" + str(loopCounter) + ".yaml"
    try:
        print("Creating file " + str(loopCounter) + "...")
        newFilePointer = open(newFileName, "w")
        newFilePointer.write(webpageOutput)
        newFilePointer.close()
    except:
        print("ERROR: FAILED TO CREATE THE FILE " + newFileName + ".  NO INFORMATION WRITTEN TO TARGET.")
    
    # close the tab
    driver.close()    
    
'''    # IMPLEMENT AT A LATER DATE
# a function to fuzz a YAML file for a stateful set
def fuzzStatefulSet():

# a function to fuzz a YAML file for a daemon
def fuzzDaemonSet():
'''

''' Main program '''
# import libraries
import selenium 
from selenium import webdriver
import sys
import random

# declare variables
loopCounter = 0

# get user input
if len(sys.argv) != 2:
    print("ERROR: INCORRECT NUMBER OF ARGUMENTS")
    exit()
else:
    numFilesNeeded = int(sys.argv[1])

# generate random seed
random.seed()

# create the desired number of fuzzed files
while loopCounter < numFilesNeeded:
    print("Generating file " + str(loopCounter) + "...")

    # initiate Selenium objects
    driver = webdriver.Edge()

    # get page for fuzzing
    driver.get("https://k8syaml.com/")
    # call the fuzzing function
    fuzzDeployment(driver)
    ''' IMPLEMENT AT A LATER DATE
    # pick and call a fuzzing function
    fuzzSelection = random.randint(0, 2)
    if fuzzSelection == 0:
        fuzzDeployment()
    elif fuzzSelection == 1:
        fuzzStatefulSet()
    elif fuzzSelection == 2:
        fuzzDaemonSet()
    '''
    
    # keep track of number of files created
    loopCounter += 1
print("File generation complete")