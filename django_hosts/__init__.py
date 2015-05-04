# flake8: noqa
try:  # pragma: no cover
    from django_hosts.defaults import patterns, host
    from django_hosts.resolvers import (reverse, reverse_lazy,
                                        reverse_host, reverse_host_lazy)
    from django_hosts.reverse import reverse_full
except ImportError:  # pragma: no cover
    pass

__version__ = '1.1.0.1'
__author__ = 'Jannis Leidel <jannis@leidel.info>'

default_app_config = 'django_hosts.apps.HostsConfig'
