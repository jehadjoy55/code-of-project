class EEGProcessor:
    def __init__(self, thresholds):
        self.thresholds = thresholds

    def process_signals(self, brain_signals):
        actions = {}
        if brain_signals['focus'] > self.thresholds['focus']:
            actions['light'] = "on"
        else:
            actions['light'] = "off"
        
        if brain_signals['relaxation'] > self.thresholds['relaxation']:
            actions['fan'] = "on"
        else:
            actions['fan'] = "off"
        
        if brain_signals['intensity'] > self.thresholds['intensity']:
            actions['lock'] = "lock"
        else:
            actions['lock'] = "unlock"

        if brain_signals['calm'] > self.thresholds['calm']:
            actions['curtain'] = "open"
        else:
            actions['curtain'] = "close"
        
        if brain_signals['overall_activity'] > self.thresholds['overall_activity']:
            actions['thermostat'] = "on"
        else:
            actions['thermostat'] = "off"

        return actions
