import sys
import os
from houseagent.utils.config import Config

"""
This init file defines some commonly used HouseAgent paths.
These paths depend on the operating system version/type, and the working situation (development/test and production) 
"""

""" Configuration path """
if os.name == 'nt':
    from win32com.shell import shellcon, shell            
    config_path = os.path.join(shell.SHGetFolderPath(0, shellcon.CSIDL_COMMON_APPDATA, 0, 0), 'HouseAgent')
else:
    config_path = os.path.join('/', 'etc', 'HouseAgent')
    
# If the path doesn't exist, lets assume we are running in a dev environment
# and just return the current working directory.
if not os.path.exists(os.path.join(config_path, 'HouseAgent.conf')):
    config_path = os.getcwd()

# init config instance
conf = Config(os.path.join(config_path, 'HouseAgent.conf'))

""" Database name and location """
db_name = 'houseagent.db'

if os.name == 'nt':
    # Windows specific code
    from win32com.shell import shellcon, shell            
    db_path = os.path.join(shell.SHGetFolderPath(0, shellcon.CSIDL_COMMON_APPDATA, 0, 0), 'HouseAgent', db_name)  
else:    
    db_path = os.path.join(sys.prefix, 'share', 'HouseAgent', db_name)
    
if os.path.exists(db_path):
    # Production environment
    db_location = db_path
else:
    # Most likely test/development environment
    db_location = db_name

""" Template directory """
template_dir = os.path.join(os.path.dirname(__file__), 'templates')

""" Template plugin directory """
template_plugin_dir = os.path.join(os.path.dirname(__file__), 'plugins')

""" Logging directory """
if os.name == 'nt':
    from win32com.shell import shellcon, shell            
    log_path = os.path.join(shell.SHGetFolderPath(0, shellcon.CSIDL_COMMON_APPDATA, 0, 0), 'HouseAgent', 'logs')  
else:    
    if os.path.exists(conf.general.logpath):
        log_path = conf.general.logpath
    else:
        log_path = 'logs'