#!/usr/bin/python3
import subprocess as sub

interface = “eth0”

new_mac = “08:00:27:02:3a:71”

sub.call([‘sudo’, ‘ifconfig’, interface, ‘down’])

sub.call([‘sudo’, ‘ifconfig’, interface, ‘hw’, ‘ether’, new_mac])

sub.call([‘sudo’, ‘ifconfig’, interface, ‘up’])
