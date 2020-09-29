#!/usr/bin/env python

import os

os.system('sudo diskutil unmount /dev/disk2s1')

os.system('sudo /usr/local/bin/ntfs-3g /dev/disk2s1 /Volumes/NTFS -o local -o allow_other -o auto_xattr -o auto_cache')