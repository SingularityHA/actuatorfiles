# Actuator Functions
def limitlessLight(dev, intent, data = None):
    if data is None:
        logger.debug("Actuating " + dev + " intent " + intent)
        mqttc.publish("limitlessLED", json.dumps([dev, intent]))
    else:
        logger.debug("Actuating " + dev + " intent " + intent + " data " + data)
        mqttc.publish("limitlessLED", json.dumps([dev, intent, data]))
 
 
#actuators
actuator_source = {
    "limitlessLED" : limitlessLight,
}
