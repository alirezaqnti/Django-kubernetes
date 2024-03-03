from core.Core_Config.utils.collections import deep_update
from core.Core_Config.utils.settings import get_settings_from_environment

deep_update(
    globals(),
    get_settings_from_environment(ENVVAR_SETTINGS_PREFIX),  # type: ignore # noqa
)
