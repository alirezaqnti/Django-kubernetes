from core.Core_Config.utils.collections import deep_update
from core.Core_Config.utils.settings import get_settings_from_environment

"""
This takes env variables with a matching prefix, strips out the prefix, and adds it to globa
For example:
export FORESETTING_IN_DOCKER=true (environment variable)
Could then be referenced as a global as:
IN DOCKER (where the value would be True)
"""


deep_update(globals(), get_settings_from_environment(ENVVAR_SETTINGS_PREFIX))  # type: ignore
