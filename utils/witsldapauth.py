from pprint import pprint
import ldap  # pip install python-ldap
from django_auth_ldap.backend import LDAPBackend  # pip install django-auth-ldap
from django_auth_ldap.config import LDAPSearch
from users.models import CustomUser


# ========================================================================= #
# SETTINGS                                                                  #
# ========================================================================= #


# -----------------------------------------
# COMMON SETTINGS, EXTRACTED FROM BELOW
# -----------------------------------------
#   - LDAP: `v3`
#   - Search Subcontexts: `Yes`
#   - Distinguished Name: `DS\a1234… + Password`
#   - Data Mappings (remember to lock):
#     - Firstname: `givenName`
#     - Surname: `sn`
#     - Email: `mail`
#     - ID Number: `cn`
#   - Password change url:
#     - https://passwordreset.wits.ac.za/default.aspx
# -----------------------------------------


# Populate Django user from LDAP directory
_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email_human": "mail",
    "email": "userprincipalname",
    "id_number": "cn",
}

_ALWAYS_UPDATE_USER = True

_CONNECTION_OPTIONS = {
    ldap.OPT_DEBUG_LEVEL: 0,
    ldap.OPT_REFERRALS: 0
}


# ========================================================================= #
# STUDENTS                                                                  #
# ========================================================================= #


# -----------------------------------------
# RAW SETTINGS GIVEN BY WITS IT DEPARTMENT:
# -----------------------------------------
# SS (Students):
# ·         Host: ldap://ss.wits.ac.za/;ldap://146.141.8.201
# ·         LDAP V3
# ·         Distinguished Name: DS\a1234… + Password
# ·         Contexts: ou=students,ou=wits university,dc=ss,dc=wits,dc=ac,dc=za
# o    or for Science & Engineering only: ou=FSCI,ou=students,ou=wits university,dc=ss,dc=wits,dc=ac,dc=za;ou=FEBE,ou=students,ou=wits university,dc=ss,dc=wits,dc=ac,dc=za
# ·         Search Subcontexts: Yes
# ·         Password change url: https://passwordreset.wits.ac.za/default.aspx
# ·         Data Mappings (remember to lock):
# o    Firstname: givenName
# o    Surname: sn
# o    Email: mail
# o    ID Number: cn
# -----------------------------------------


# extending LDAPBackend base class
class LDAPBackendWitsStudents(LDAPBackend):

    settings_prefix = "AUTH_LDAP_SS_"

    default_settings = {
        'SERVER_URI': 'ldap://ss.wits.ac.za',
        'USER_SEARCH': LDAPSearch("OU=Students,OU=Wits University,DC=ss,DC=WITS,DC=AC,DC=ZA", ldap.SCOPE_SUBTREE, "(cn=%(user)s)"),
        'CONNECTION_OPTIONS': _CONNECTION_OPTIONS,
        'ALWAYS_UPDATE_USER': _ALWAYS_UPDATE_USER,
        'USER_ATTR_MAP': _USER_ATTR_MAP,
    }

    def authenticate_ldap_user(self, ldap_user, password):
        print(" - Attempting Authentication as Student")
        self.settings.BIND_DN = f'{ldap_user._username}@students.wits.ac.za'
        self.settings.BIND_PASSWORD = password

        user = None
        # Check if user already exists
        if CustomUser.objects.filter(username=ldap_user._username).exists():  # User must be pre authorised to use site
            print(ldap_user._username + " - User Exists Already")
            try:
                user = super(LDAPBackendWitsStudents, self).authenticate_ldap_user(ldap_user, password)
            except:
                user = None
            if user:
                # ldap_user._last_name = ldap_user.attrs['sn'][0]
                # ldap_user._first_name = ldap_user.attrs['givenName'][0]
                # Fix for USER_ATTR_MAP not working properly - hopefully...
                # user1 = CustomUser.objects.get(pk=user.username)
                # user1.first_name = ldap_user.attrs['givenName'][0]
                # user1.last_name = ldap_user.attrs['sn'][0]
                # username.first_name = ldap_user.attrs['givenName'][0]
                # username.last_name = ldap_user.attrs['sn'][0]
                # print(username.first_name)
                print(f" - Authenticated as Student: {ldap_user._username} ({ldap_user.attrs['sn'][0]}, {ldap_user.attrs['givenName'][0]})")
        else:
            print(ldap_user._username + " - User not authorised")
        return user


# Not required for now - We cannot test this anyway since we don't have staff access
# ========================================================================= #
# STAFF                                                                     #
# ========================================================================= #


# -----------------------------------------
# RAW SETTINGS GIVEN BY WITS IT DEPARTMENT:
# -----------------------------------------
# DS (Staff):
# ·         Host: ldap://ds.wits.ac.za/;ldap://146.141.128.150
# ·         LDAP V3
# ·         Distinguished Name: DS\a1234… + Password
# ·         Contexts: ou=wits university,dc=ds,dc=wits,dc=ac,dc=za
# o    Changed contexts to be faculty specific to allow for staff synchronisation.
# o    ou=faculty of science,ou=wits university,dc=ds,dc=wits,dc=ac,dc=za
# o    OU=Faculty of Engineering and the Built Environment,OU=Wits University,DC=ds,DC=WITS,DC=AC,DC=ZA
# o    OU=Faculty of Commerce\, Law & Management,OU=Wits University,DC=ds,DC=WITS,DC=AC,DC=ZA
# ·         Search Subcontexts: Yes
# ·         Data Mappings (remember to lock):
# o    Firstname: givenName
# o    Surname: sn
# o    Email: mail
# o    ID Number: cn
# -----------------------------------------


# We don't have staff access so not implemented for now...
# class LDAPBackendWitsStaff(LDAPBackend):
#
#     settings_prefix = "AUTH_LDAP_DS_"
#
#     default_settings = {
#         'SERVER_URI': 'ldap://ds.wits.ac.za',
#         'USER_SEARCH': LDAPSearch("OU=Wits University,DC=ds,DC=WITS,DC=AC,DC=ZA", ldap.SCOPE_SUBTREE, "(cn=%(user)s)"),
#         'CONNECTION_OPTIONS': _CONNECTION_OPTIONS,
#         'ALWAYS_UPDATE_USER': _ALWAYS_UPDATE_USER,
#         'USER_ATTR_MAP': _USER_ATTR_MAP,
#     }
#
#     def authenticate_ldap_user(self, ldap_user, password):
#         print(" - Attempting Authentication as Staff")
#         self.settings.BIND_DN = f'{ldap_user._username}@wits.ac.za'
#         self.settings.BIND_PASSWORD = password
#         try:
#             username = super(LDAPBackendWitsStaff, self).authenticate_ldap_user(ldap_user, password)
#         except:
#             username = None
#         if username is not None:
#             print(f" - Authenticated as Staff: {ldap_user._username} ({ldap_user.attrs['sn'][0]}, {ldap_user.attrs['givenName'][0]})")
#         return username

