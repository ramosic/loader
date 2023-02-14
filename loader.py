#!/usr/bin/env python3
# Author: Christer Karlsen
# Email: chris@ramosicked.com
# Project: loader
# Copyright (c) 2023, Christer Karlsen
# License: MIT License
#
# loader.py
import os
import subprocess

def run_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode().strip(), result.stderr.decode().strip()

def handle_command(command):
    if command == 'uptime':
        return run_command('uptime')
    else:
        return 'Unknown command', ''

def run_plugins(plugins):
    for plugin in plugins:
        output, error = plugin.run()
        if error:
            print(f'Error from {plugin.__class__.__name__}: {error}')
        else:
            print(f'Output from {plugin.__class__.__name__}: {output}')

# Example plugin
class DiskUsagePlugin:
    def run(self):
        return run_command('df -h')

if __name__ == '__main__':
    plugins = [DiskUsagePlugin()]
    run_plugins(plugins)

