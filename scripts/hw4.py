#!/usr/bin/python
import rpm,sys,os

filename = sys.argv[1]
rpm_file = open(filename)
ts = rpm.TransactionSet()
ts.setVSFlags(rpm._RPMVSF_NOSIGNATURES)
package = ts.hdrFromFdno(rpm_file)
print package[rpm.RPMTAG_RELEASE]
