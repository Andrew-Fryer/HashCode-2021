def algorithm(simStep, simSet, graph, iterations):
    bestScore = 0
    bestConfig = []
    changeTime = 0
    
    config = 'red'
    
    #Set all lights to red
    simSet(config)
    #Run until all cars stopped
    while (True):
        state = simStep()
    changeTime = state.time
    for i in range(intersectionNum):
        updateConfig()
    #Run to completion
    while (True):
        state = simStep()
    #Set best
    bestScore = graph.score()
    bestConfig = config
        
    #Run a certain number of experiments
    for i in range(iterations):
        #Set to bestconfig
        simSet(bestConfig)
        #Run until last changetime
        for j in range(changeTime):
            state = simStep()
        #Lookahead
        for j in range(i+1):
            state = simStep()
        #Update config by averaging
        newConfig = getNewConfig()
        simSet(newConfig)
        resetSim()
        #Run to completion
        while (True):
            state = simStep()
        if (graph.score() > bestScore):
            bestConfig = newConfig
            bestScore = graph.score()
        