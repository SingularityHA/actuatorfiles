# Actuator Functions
def NBswitch(dev, intent, data = None):
        if intent == "on":
                logger.debug("switch_"+ dev +"_on")
                mqttc.publish("rfm_ninjablock/send", "switch_"+ str(dev) +"_on" )
        if intent == "off":
                mqttc.publish("rfm_ninjablock/send", "switch_"+ str(dev) +"_off" )
 
#actuators
actuator_source = {
        "NBswitch" : NBswitch,
        }
