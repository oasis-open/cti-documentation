#!/usr/bin/python

from time import gmtime, strftime
from sys import exit, stderr
from subprocess import call

def main():
    new_date = 'last_updated: {}'.format(strftime("\"%a %b %d %H:%M:%S UTC %Y\"", gmtime()))
    with open('_config.yml', 'rb') as FILE:
        filedata = FILE.read()

    old_date_loc = filedata.find('last_updated: \"')
    if old_date_loc < 0:
        print_err()

    old_date = filedata[old_date_loc:filedata.find("\n", old_date_loc)]
    filedata = filedata.replace(old_date, new_date)

    with open('_config.yml', 'wb') as FILE:
        FILE.write(filedata)

    if call(["git", "add", "_config.yml"]):
        print_err()

    if call(["git", "commit", "-m", "Git Hook: Updated 'last_updated' time"]):
        print_err()

    print "[+] Updated 'last_updated' time"
    exit(0)

def print_err():
    stderr.write("[!] Error updating 'last_updated:' in '_config.yml. Exiting...\n")
    exit(1)

if __name__ == '__main__':
    main()
