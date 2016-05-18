#!/usr/bin/python
import rpm,sys,os

filename = sys.argv[1]
rpm_file = open(filename)
ts = rpm.TransactionSet()
ts.setVSFlags(rpm._RPMVSF_NOSIGNATURES)
package = ts.hdrFromFdno(rpm_file)

#print "NAME...........", package[rpm.RPMTAG_NAME]
#print "VERSION........", package[rpm.RPMTAG_VERSION]
#print "RELEASE........", package[rpm.RPMTAG_RELEASE]
#print "ARCH...........", package[rpm.RPMTAG_ARCH]
#print "LICENSE........", package[rpm.RPMTAG_LICENSE]
#print "GROUP..........", package[rpm.RPMTAG_GROUP]
#print "DISTRO.........", package[rpm.RPMTAG_DISTRIBUTION]
#print "PACKAGER.......", package[rpm.RPMTAG_PACKAGER]
#print "PROJECT_URL....", package[rpm.RPMTAG_URL]

print "%s.%s.centos" % (package['version'], package['release'])
print package[rpm.RPMTAG_RELEASE]
