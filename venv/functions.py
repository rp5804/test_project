from util.util import create_device

from tabulate import tabulate

if __name__ == '__main__':
    devices = create_device(num_devices=3, num_subnets=3)
    print('\n', tabulate(devices, headers='keys'))
