#!/usr/bin/env python

import os

os.system('brew cask install osxfuse')

os.system('sudo mkdir /usr/local/Cellar')

os.system('sudo chmod u+w /usr/local/Cellar')

os.system('sudo chown -R $USER /usr/local/Cellar')

os.system('sudo mkdir /usr/local/opt')

os.system('sudo chmod u+w /usr/local/opt')

os.system('sudo chown -R $USER /usr/local/opt')

os.system('sudo mkdir /usr/local/sbin')

os.system('sudo chmod u+w /usr/local/sbin')

os.system('sudo chown -R $USER /usr/local/sbin')

os.system('brew install ntfs-3g')

os.system('chmod +x Mount_NTFS.command')

os.system('sudo diskutil unmount /dev/disk2s1')

os.system('sudo mkdir /Volumes/NTFS')

os.system('sudo chmod u+w /Volumes/NTFS/')

os.system('sudo chown -R $USER /Volumes/NTFS/')

os.system('sudo /usr/local/bin/ntfs-3g /dev/disk2s1 /Volumes/NTFS -o local -o allow_other -o auto_xattr -o auto_cache')