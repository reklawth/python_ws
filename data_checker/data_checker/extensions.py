import glob
import filecmp

from scrapy import signals
from scrapy.exceptions import NotConfigured

class EmailOnChange(object):
    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.getbool("EMAIL_ON_CHANGE_ENABLED"):
            raise NotConfigured

        # Create an instance of our extension
        extension = cls()

        crawler.signals.connect(extension.engine_stopped, signal=signals.engine_stopped)

        return extension

    def engine_stopped(self):
        # List out previous runs
        runs = sorted(glob.glob("/tmp/[0-9]*-[0-9]*-[0-9]*T[0-9]*-[0-9]*-[0-9]*.json"), reverse=True)

        if len(runs) < 2:
            # We cannot compare if there is only 1 run
            return

        # Grab the newest 2 runs
        current_file, previous_file = runs[0:2]

        # Compare them
        if not filecmp.cmp(current_file, previous_file):
            print("\n\nTHE FILES ARE DIFFERENT \n\n")
        else: 
            print("\n\nNO CHANGE \n\n")
