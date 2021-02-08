#!/usr/bin/env python

from time import gmtime, strftime
from sys import exit, stderr
from subprocess import call, check_output


def main():
    git_log = check_output("git log".split(' ')).decode()
    if git_log.split('\n')[4].find("Git Hook: Updated 'last_updated' time") >= 0:
        exit(0)

    new_date = 'last_updated: {}'.format(strftime("\"%a %b %d %H:%M:%S UTC %Y\"", gmtime()))
    with open('_config.yml', 'r') as FILE:
        filedata = FILE.read()

    old_date_loc = filedata.find('last_updated: \"')
    if old_date_loc < 0:
        print_err()

    old_date = filedata[old_date_loc:filedata.find("\n", old_date_loc)]
    filedata = filedata.replace(old_date, new_date)

    with open('_config.yml', 'w') as FILE:
        FILE.write(filedata)

    if call("git add _config.yml".split(' ')):
        print_err()

    if call(["git", "commit", "-m", "Git Hook: Updated 'last_updated' time"]):
        print_err()

    print("[+] Updated 'last_updated' time. Please `git push` again.")
    exit(1)


def print_err():
    stderr.write("[!] Error updating 'last_updated:' in '_config.yml. Exiting...\n")
    exit(1)


if __name__ == '__main__':
    main()
