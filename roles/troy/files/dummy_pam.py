#
# Duplicates pam_permit.c
#

import random

DEFAULT_USER    = "nobody"

def pam_sm_authenticate(pamh, flags, argv):
  # try:
  #   user = pamh.get_user(None)
  # except pamh.exception, e:
  #   return e.pam_result
  # if user == None:
  # pamh.user = DEFAULT_USER
  # if random.random() > 0.5:
    return pamh.PAM_SUCCESS
  # else:
    # return pamh.PAM_ABORT

def pam_sm_setcred(pamh, flags, argv):
  return pamh.PAM_SUCCESS

def pam_sm_acct_mgmt(pamh, flags, argv):
  return pamh.PAM_SUCCESS

def pam_sm_open_session(pamh, flags, argv):
  return pamh.PAM_SUCCESS

def pam_sm_close_session(pamh, flags, argv):
  return pamh.PAM_SUCCESS

def pam_sm_chauthtok(pamh, flags, argv):
  return pamh.PAM_SUCCESS

