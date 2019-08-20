from pprint import pprint
import ldap
from django_auth_ldap.backend import LDAPBackend
from django_auth_ldap.config import LDAPSearch


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


# TODO: Extract common behavior
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
        try:
            username = super(LDAPBackendWitsStudents, self).authenticate_ldap_user(ldap_user, password)
        except:
            username = None
        if username:
            print(f" - Authenticated as Student: {ldap_user._username} ({ldap_user.attrs['sn'][0]}, {ldap_user.attrs['givenName'][0]})")
        return username


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


# TODO: Extract common behavior
class LDAPBackendWitsStaff(LDAPBackend):

    settings_prefix = "AUTH_LDAP_DS_"

    default_settings = {
        'SERVER_URI': 'ldap://ds.wits.ac.za',
        'USER_SEARCH': LDAPSearch("OU=Wits University,DC=ds,DC=WITS,DC=AC,DC=ZA", ldap.SCOPE_SUBTREE, "(cn=%(user)s)"),
        'CONNECTION_OPTIONS': _CONNECTION_OPTIONS,
        'ALWAYS_UPDATE_USER': _ALWAYS_UPDATE_USER,
        'USER_ATTR_MAP': _USER_ATTR_MAP,
    }

    def authenticate_ldap_user(self, ldap_user, password):
        print(" - Attempting Authentication as Staff")
        self.settings.BIND_DN = f'{ldap_user._username}@wits.ac.za'
        self.settings.BIND_PASSWORD = password
        try:
            username = super(LDAPBackendWitsStaff, self).authenticate_ldap_user(ldap_user, password)
        except:
            username = None
        if username is not None:
            print(f" - Authenticated as Staff: {ldap_user._username} ({ldap_user.attrs['sn'][0]}, {ldap_user.attrs['givenName'][0]})")
        return username

