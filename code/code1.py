# The following code assumes that the user defines many of these terms elsewhere in the code, 
# such as my_network and the methods is_down and last_change. 

for switch in my_network:
    for interface in switch:
        if interface.is_down() and interface.last_change() > thirty_days:
            interface.shutdown()
            interface.set_description("Interface disabled per Policy")

