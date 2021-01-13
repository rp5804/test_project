from random import choice
import string


def create_device(num_devices=1, num_subnets=1):
    # Create an empty list of devices
    created_devices = list()

    if num_devices > 254 or num_subnets > 254:
        print('Error: Too many devices/subnets')
        return created_devices

    for subnet_index in range(1, num_subnets + 1):

        for device_index in range(1, num_devices + 1):

            # Create device dictionary
            device = dict()

            # Random device details
            device['name'] = choice(['r1', 'r2', 'r3'])

            # Types of os, version and ip address depending on vendor choice
            device['vendor'] = choice(['Arista', 'Cisco', 'Juniper'])

            if device['vendor'] == 'Arista':
                device['os'] = 'eos'
                device['version'] = choice(['1.1', '2.0.1', '3.1.2'])
            elif device['vendor'] == 'Cisco':
                device['os'] = choice(['ios', 'iosxe', 'iosxr', 'nexus'])
                device['version'] = choice(['12.1', '20.0.1', '13.1.2'])
            elif device['vendor'] == 'Juniper':
                device['os'] = 'junos'
                device['version'] = choice(['11.1', '12.2.1', '13.1.2'])

            device['ip'] = '10.0.' + '.' + str(subnet_index) + '.' + str(device_index)
            created_devices.append(device)
    return created_devices
