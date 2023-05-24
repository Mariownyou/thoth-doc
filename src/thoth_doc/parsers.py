import os
import re


def env_var_parser(line):
    ''' Parses [$env.ENV_VAR_NAME] syntax '''

    match = re.match(r'\[\$env\.(\w+)\]', line)
    if match:
        print(match.groups())
        value = os.environ.get(match.group(1))
        return line.replace(match.group(0), str(value))
    return None


def django_settings_parser(line):
    ''' Parses [$settings.SETTINGS_VAR_NAME] syntax '''

    match = re.match(r'\[\$settings\.(\w+)\]', line)
    if match:
        try:
            from django.conf import settings
        except ImportError:
            raise ImportError('Django is not installed')
        value = getattr(settings, match.group(1))
        return line.replace(match.group(0), str(value))
    return None
