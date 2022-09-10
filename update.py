# update everything

import pkg_resources, subprocess
from config import Config
if Config.UPDATE_ALL:
    subprocess.call("pip install --upgrade " + ' '.join([dist.project_name for dist in pkg_resources.working_set]), shell=True)