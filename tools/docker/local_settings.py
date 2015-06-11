# Copyright (c) 2015 Ansible, Inc.
# All Rights Reserved.

# Local Django settings for AWX project.  Rename to "local_settings.py" and
# edit as needed for your development environment.

# All variables defined in awx/settings/development.py will already be loaded
# into the global namespace before this file is loaded, to allow for reading
# and updating the default settings as needed.

###############################################################################
# MISC PROJECT SETTINGS
###############################################################################

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

# Database settings to use PostgreSQL for development.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'awx-dev',
        'USER': 'awx-dev',
        'PASSWORD': 'AWXsome1',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Use SQLite for unit tests instead of PostgreSQL.  If the lines below are
# commented out, Django will create the test_awx-dev database in PostgreSQL to
# run unit tests.
if len(sys.argv) >= 2 and sys.argv[1] == 'test':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'awx.sqlite3'),
            # Test database cannot be :memory: for celery/inventory tests.
            'TEST_NAME': os.path.join(BASE_DIR, 'awx_test.sqlite3'),
        }
    }

# Celery AMQP configuration.
BROKER_URL = 'redis://localhost/'

# Set True to enable additional logging from the job_event_callback plugin
JOB_CALLBACK_DEBUG = False

# Absolute filesystem path to the directory to host projects (with playbooks).
# This directory should NOT be web-accessible.
PROJECTS_ROOT = os.path.join(BASE_DIR, 'projects')

# Absolute filesystem path to the directory for job status stdout
# This directory should not be web-accessible
JOBOUTPUT_ROOT = os.path.join(BASE_DIR, 'job_status')

# The UUID of the system, for HA.
SYSTEM_UUID = '00000000-0000-0000-0000-000000000000'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# SECURITY WARNING: keep the secret key used in production secret!
# Hardcoded values can leak through source control. Consider loading
# the secret key from an environment variable or a file instead.
SECRET_KEY = 'p7z7g1ql4%6+(6nlebb6hdk7sd^&fnjpal308%n%+p^_e6vo1y'

# HTTP headers and meta keys to search to determine remote host name or IP. Add
# additional items to this list, such as "HTTP_X_FORWARDED_FOR", if behind a
# reverse proxy.
REMOTE_HOST_HEADERS = ['REMOTE_ADDR', 'REMOTE_HOST']

# Define additional environment variables to be passed to subprocess started by
# the celery task.
#AWX_TASK_ENV['FOO'] = 'BAR'

# If set, use -vvv for project updates instead of -v for more output.
# PROJECT_UPDATE_VVV=True

# Set verbosity for inventory import command when running inventory updates.
# INVENTORY_UPDATE_VERBOSITY=1

###############################################################################
# EMAIL SETTINGS
###############################################################################

# Email address that error messages come from.
SERVER_EMAIL = 'root@localhost'

# The email backend to use. For possible shortcuts see django.core.mail.
# The default is to use the SMTP backend.
# Third-party backends can be specified by providing a Python path
# to a module that defines an EmailBackend class.
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Host for sending email.
EMAIL_HOST = 'localhost'

# Port for sending email.
EMAIL_PORT = 25

# Optional SMTP authentication information for EMAIL_HOST.
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False

# Default email address to use for various automated correspondence from
# the site managers.
DEFAULT_FROM_EMAIL = 'webmaster@localhost'

# Subject-line prefix for email messages send with django.core.mail.mail_admins
# or ...mail_managers.  Make sure to include the trailing space.
EMAIL_SUBJECT_PREFIX = '[AWX] '

###############################################################################
# LOGGING SETTINGS
###############################################################################

# Enable logging to syslog. Setting level to ERROR captures 500 errors,
# WARNING also logs 4xx responses.
LOGGING['handlers']['syslog'] = {
    'level': 'WARNING',
    'filters': [],
    'class': 'django.utils.log.NullHandler',
    'formatter': 'simple',
}

# Enable the following lines to also log to a file.
#LOGGING['handlers']['file'] = {
#    'class': 'logging.FileHandler',
#    'filename': os.path.join(BASE_DIR, 'awx.log'),
#    'formatter': 'simple',
#}

# Enable the following lines to turn on lots of permissions-related logging.
#LOGGING['loggers']['awx.main.access']['propagate'] = True
#LOGGING['loggers']['awx.main.signals']['propagate'] = True
#LOGGING['loggers']['awx.main.permissions']['propagate'] = True

# Enable the following lines to turn on LDAP auth logging.
#LOGGING['loggers']['django_auth_ldap']['handlers'] = ['console']
#LOGGING['loggers']['django_auth_ldap']['level'] = 'DEBUG'

###############################################################################
# LDAP AUTHENTICATION SETTINGS
###############################################################################

# Refer to django-auth-ldap docs for more details:
# http://pythonhosted.org/django-auth-ldap/authentication.html

# LDAP server URI, such as "ldap://ldap.example.com:389" (non-SSL) or
# "ldaps://ldap.example.com:636" (SSL).  LDAP authentication is disable if this
# parameter is empty.
AUTH_LDAP_SERVER_URI = ''

# DN of user to bind for all search queries. Normally in the format
# "CN=Some User,OU=Users,DC=example,DC=com" but may also be specified as
# "DOMAIN\username" for Active Directory.
AUTH_LDAP_BIND_DN = ''

# Password using to bind above user account.
AUTH_LDAP_BIND_PASSWORD = ''

# Enable TLS when the connection is not using SSL.
AUTH_LDAP_START_TLS = False

# Imports needed for remaining LDAP configuration.
import ldap
from django_auth_ldap.config import LDAPSearch, LDAPSearchUnion
from django_auth_ldap.config import ActiveDirectoryGroupType

# LDAP search query to find users.
AUTH_LDAP_USER_SEARCH = LDAPSearch(
    'OU=Users,DC=example,DC=com',   # Base DN
    ldap.SCOPE_SUBTREE,             # SCOPE_BASE, SCOPE_ONELEVEL, SCOPE_SUBTREE
    '(sAMAccountName=%(user)s)',    # Query
)

# Alternative to user search, if user DNs are all of the same format.
#AUTH_LDAP_USER_DN_TEMPLATE = 'uid=%(user)s,OU=Users,DC=example,DC=com'

# Mapping of LDAP to user atrributes (key is user attribute name, value is LDAP
# attribute name).
AUTH_LDAP_USER_ATTR_MAP = {
    'first_name': 'givenName',
    'last_name': 'sn',
    'email': 'mail',
}

# LDAP search query to find groups. Does not support LDAPSearchUnion.
AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    'DC=example,DC=com',    # Base DN
    ldap.SCOPE_SUBTREE,     # SCOPE_BASE, SCOPE_ONELEVEL, SCOPE_SUBTREE
    '(objectClass=group)',  # Query
)
# Type of group returned by the search above. Should be one of the types
# listed at: http://pythonhosted.org/django-auth-ldap/groups.html#types-of-groups
AUTH_LDAP_GROUP_TYPE = ActiveDirectoryGroupType()

# Group DN required to login. If specified, user must be a member of this
# group to login via LDAP.
#AUTH_LDAP_REQUIRE_GROUP = ''

# Group DN denied from login. If specified, user will not be allowed to login
# if a member of this group.
#AUTH_LDAP_DENY_GROUP = ''

# User profile flags updated from group membership (key is user attribute name,
# value is group DN).
AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    #'is_superuser': 'CN=Domain Admins,CN=Users,DC=example,DC=com',
}

# Mapping between organization admins/users and LDAP groups. Keys are
# organization names (will be created if not present). Values are dictionaries
# of options for each organization's membership, where each can contain the
# following parameters:
# - remove: True/False. Defaults to False. Specifies the default for
#   remove_admins or remove_users if those parameters aren't explicitly set.
# - admins: None, True/False, string or list/tuple of strings.
#   If None, organization admins will not be updated.
#   If True/False, all LDAP users will be added/removed as admins.
#   If a string or list of strings, specifies the group DN(s). User will be
#   added as an org admin if the user is a member of ANY of these groups.
# - remove_admins: True/False. Defaults to False. If True, a user who is not a
#   member of the given groups will be removed from the organization's admins.
# - users: None, True/False, string or list/tuple of strings. Same rules apply
#   as for admins.
# - remove_users: True/False. Defaults to False. If True, a user who is not a
#   member of the given groups will be removed from the organization's users.
AUTH_LDAP_ORGANIZATION_MAP = {
    #'Test Org': {
    #    'admins': 'CN=Domain Admins,CN=Users,DC=example,DC=com',
    #    'users': ['CN=Domain Users,CN=Users,DC=example,DC=com'],
    #},
    #'Test Org 2': {
    #    'admins': ['CN=Administrators,CN=Builtin,DC=example,DC=com'],
    #    'users': True,
    #},
}

# Mapping between team members (users) and LDAP groups. Keys are team names
# (will be created if not present). Values are dictionaries of options for
# each team's membership, where each can contain the following parameters:
# - organization: string. The name of the organization to which the team
#   belongs.  The team will be created if the combination of organization and
#   team name does not exist.  The organization will first be created if it
#   does not exist.
# - users: None, True/False, string or list/tuple of strings.
#   If None, team members will not be updated.
#   If True/False, all LDAP users will be added/removed as team members.
#   If a string or list of strings, specifies the group DN(s). User will be
#   added as a team member if the user is a member of ANY of these groups.
# - remove: True/False. Defaults to False. If True, a user who is not a member
#   of the given groups will be removed from the team.
AUTH_LDAP_TEAM_MAP = {
    'My Team': {
        'organization': 'Test Org',
        'users': ['CN=Domain Users,CN=Users,DC=example,DC=com'],
        'remove': True,
    },
    'Other Team': {
        'organization': 'Test Org 2',
        'users': 'CN=Other Users,CN=Users,DC=example,DC=com',
        'remove': False,
    },
}

###############################################################################
# SCM TEST SETTINGS
###############################################################################

# Define these variables to enable more complete testing of project support for
# SCM updates.  The test repositories listed do not have to contain any valid
# playbooks.

try:
    path = os.path.expanduser(os.path.expandvars('~/.ssh/id_rsa'))
    TEST_SSH_KEY_DATA = file(path, 'rb').read()
except IOError:
    TEST_SSH_KEY_DATA = ''

TEST_GIT_USERNAME = ''
TEST_GIT_PASSWORD = ''
TEST_GIT_KEY_DATA = TEST_SSH_KEY_DATA
TEST_GIT_PUBLIC_HTTPS = 'https://github.com/ansible/ansible.github.com.git'
TEST_GIT_PRIVATE_HTTPS = 'https://github.com/ansible/product-docs.git'
TEST_GIT_PRIVATE_SSH = 'git@github.com:ansible/product-docs.git'

TEST_HG_USERNAME = ''
TEST_HG_PASSWORD = ''
TEST_HG_KEY_DATA = TEST_SSH_KEY_DATA
TEST_HG_PUBLIC_HTTPS = 'https://bitbucket.org/cchurch/django-hotrunner'
TEST_HG_PRIVATE_HTTPS = ''
TEST_HG_PRIVATE_SSH = ''

TEST_SVN_USERNAME = ''
TEST_SVN_PASSWORD = ''
TEST_SVN_PUBLIC_HTTPS = 'https://github.com/ansible/ansible.github.com'
TEST_SVN_PRIVATE_HTTPS = 'https://github.com/ansible/product-docs'

# To test repo access via SSH login to localhost.
import getpass
TEST_SSH_LOOPBACK_USERNAME = getpass.getuser()
TEST_SSH_LOOPBACK_PASSWORD = ''

###############################################################################
# LDAP TEST SETTINGS
###############################################################################

# LDAP connection and authentication settings for unit tests only.  LDAP tests
# will be skipped if TEST_AUTH_LDAP_SERVER_URI is not configured.

TEST_AUTH_LDAP_SERVER_URI = ''
TEST_AUTH_LDAP_BIND_DN = ''
TEST_AUTH_LDAP_BIND_PASSWORD = ''
TEST_AUTH_LDAP_START_TLS = False

# LDAP username/password for testing authentication.
TEST_AUTH_LDAP_USERNAME = ''
TEST_AUTH_LDAP_PASSWORD = ''

# LDAP search query to find users.
TEST_AUTH_LDAP_USER_SEARCH = LDAPSearch(
    'CN=Users,DC=example,DC=com',
    ldap.SCOPE_SUBTREE,
    '(sAMAccountName=%(user)s)',
)

# Alternative to user search.
#TEST_AUTH_LDAP_USER_DN_TEMPLATE = 'sAMAccountName=%(user)s,OU=Users,DC=example,DC=com'

# Mapping of LDAP attributes to user attributes.
TEST_AUTH_LDAP_USER_ATTR_MAP = {
    'first_name': 'givenName',
    'last_name': 'sn',
    'email': 'mail',
}

# LDAP search query for finding groups.
TEST_AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
    'DC=example,DC=com',
    ldap.SCOPE_SUBTREE,
    '(objectClass=group)',
)
# Type of group returned by the search above.
TEST_AUTH_LDAP_GROUP_TYPE = ActiveDirectoryGroupType()

# Test DNs for a group required to login.  User should be a member of the first
# group, but not a member of the second.
TEST_AUTH_LDAP_REQUIRE_GROUP = 'CN=Domain Admins,CN=Users,DC=example,DC=com'
TEST_AUTH_LDAP_REQUIRE_GROUP_FAIL = 'CN=Guest,CN=Users,DC=example,DC=com'

# Test DNs for a group denied from login.  User should not be a member of the
# first group, but should be a member of the second.
TEST_AUTH_LDAP_DENY_GROUP = 'CN=Guest,CN=Users,DC=example,DC=com'
TEST_AUTH_LDAP_DENY_GROUP_FAIL = 'CN=Domain Admins,CN=Users,DC=example,DC=com'

# User profile flags updated from group membership.  Test user should be a
# member of the group.
TEST_AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    'is_superuser': 'CN=Domain Admins,CN=Users,DC=example,DC=com',
}

# Test mapping between organization admins/users and LDAP groups.
TEST_AUTH_LDAP_ORGANIZATION_MAP = {
    'Test Org': {
        'admins': 'CN=Domain Admins,CN=Users,DC=example,DC=com',
        'users': ['CN=Domain Users,CN=Users,DC=example,DC=com'],
    },
    'Test Org 2': {
        'admins': ['CN=Administrators,CN=Builtin,DC=example,DC=com'],
        'users': True,
    },
}
# Expected results from organization mapping.  After login, should user be an
# admin/user in the given organization?
TEST_AUTH_LDAP_ORGANIZATION_MAP_RESULT = {
    'Test Org': {'admins': True, 'users': False},
    'Test Org 2': {'admins': False, 'users': True},
}

# Second test mapping to test remove parameters.
TEST_AUTH_LDAP_ORGANIZATION_MAP_2 = {
    'Test Org': {
        'admins': 'CN=Domain Users,CN=Users,DC=example,DC=com',
        'users': True,
        'remove_admins': True,
        'remove_users': False,
    },
    'Test Org 2': {
        'admins': ['CN=Domain Admins,CN=Users,DC=example,DC=com',
                   'CN=Administrators,CN=Builtin,DC=example,DC=com'],
        'users': False,
        'remove': True,
    },
}

# Expected results from second organization mapping.
TEST_AUTH_LDAP_ORGANIZATION_MAP_2_RESULT = {
    'Test Org': {'admins': False, 'users': True},
    'Test Org 2': {'admins': True, 'users': False},
}

# Test mapping between team users and LDAP groups.
TEST_AUTH_LDAP_TEAM_MAP = {
    'Domain Users Team': {
        'organization': 'Test Org',
        'users': ['CN=Domain Users,CN=Users,DC=example,DC=com'],
        'remove': False,
    },
    'Admins Team': {
        'organization': 'Admins Org',
        'users': 'CN=Domain Admins,CN=Users,DC=example,DC=com',
        'remove': True,
    },
    'Everyone Team': {
        'organization': 'Test Org 2',
        'users': True,
    },
}
# Expected results from team mapping.  After login, should user be a member of
# the given team?
TEST_AUTH_LDAP_TEAM_MAP_RESULT = {
    'Domain Users Team': {'users': False},
    'Admins Team': {'users': True},
    'Everyone Team': {'users': True},
}

# Second test mapping for teams to remove user.
TEST_AUTH_LDAP_TEAM_MAP_2 = {
    'Domain Users Team': {
        'organization': 'Test Org',
        'users': ['CN=Domain Users,CN=Users,DC=example,DC=com'],
        'remove': False,
    },
    'Admins Team': {
        'organization': 'Admins Org',
        'users': 'CN=Administrators,CN=Builtin,DC=example,DC=com',
        'remove': True,
    },
    'Everyone Team': {
        'organization': 'Test Org 2',
        'users': False,
        'remove': False,
    },
}
# Expected results from second team mapping.  After login, should user be a
# member of the given team?
TEST_AUTH_LDAP_TEAM_MAP_2_RESULT = {
    'Domain Users Team': {'users': False},
    'Admins Team': {'users': False},
    'Everyone Team': {'users': True},
}

###############################################################################
# INVENTORY IMPORT TEST SETTINGS
###############################################################################

# Define these variables to enable more complete testing of inventory import
# from cloud providers.

# EC2 credentials
TEST_AWS_ACCESS_KEY_ID = ''
TEST_AWS_SECRET_ACCESS_KEY = ''
TEST_AWS_REGIONS = 'all'

# Rackspace credentials
TEST_RACKSPACE_USERNAME = ''
TEST_RACKSPACE_API_KEY = ''
TEST_RACKSPACE_REGIONS = 'all'

# VMware credentials
TEST_VMWARE_HOST = ''
TEST_VMWARE_USER = ''
TEST_VMWARE_PASSWORD = ''
