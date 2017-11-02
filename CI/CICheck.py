import sys
from CITests import CITests

# Instance of CITests
ci = CITests("/CI")

# Run Check on OpenIPSL
testPASS = ci.runSyntaxCheck("checkPASS","/CIcheck/checkPASS.mo")
testFAIL = ci.runSyntaxCheck("checkFAIL","/CIcheck/checkFAIL.mo")

if (testPASS == True) and (testFAIL == False):
    # Everything is fine
    sys.exit(0)
else:
    # Exit with error
    raise Exception("The CI script is NOT working as expected")
