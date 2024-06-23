import hashlib
import time
import shelve
import os
from fims import helpers
from fims.__init__ import TITLE, DATABASE, monitor
from fims.monit import getFiles


def main():
    helpers.hello(TITLE)

    files = {}

    try:
        while True:
            for file in getFiles(monitor):
                hash = hashlib.sha256()

                with open(file, 'rb') as f:
                    for chunk in iter(lambda: f.read(2048), b''):
                        hash.update(chunk)

                sha256 = hash.hexdigest()

                if file in files and sha256 != files[file]:
                    print(f'{file} has been changed! {time.strftime("%Y-%m-%d %H:%M:%S")}')

                files[file] = sha256
                with shelve.open(DATABASE) as s:
                    s[file] = files[file]

            time.sleep(1)

    except KeyboardInterrupt:
        helpers.bye(TITLE)

if __name__ == "__main__":
    main()