import sys
import os
import subprocess
from subprocess import PIPE
import pexpect
from unittest import TestCase

def runPwds( executable, cmd, password, passwordPrompts=[], promptsAndInputs=[] ):
    args = [ executable ]
    args.extend( cmd.split() )

    proc = pexpect.spawn( ' '.join( [ executable ] + [ cmd ] ) )
    try:
        for passPrompt in passwordPrompts:
            proc.expect( passPrompt, timeout=1 )
            proc.sendline( password )

        for prompt, inp in promptsAndInputs:
            proc.expect( passPrompt, timeout=1 )
            proc.sendline( password )
    except ( pexpect.TIMEOUT, pexpect.EOFError ) as e:
        pass

    lines = []
    line = proc.readline()
    while line != '':
        line = line.replace( '\r\n', '' )
        if line != '':
            lines.append( line )
        line = proc.readline()
    return lines

class PwdsBaseTest( TestCase ):

    def setUp( self ):
        self.filepass = 'TestPass'
        testdir = os.path.dirname( sys.argv[ 0 ] )
        self.executable = os.path.join( testdir, '../pwds' )
        self.assertTrue( os.path.isfile( self.executable ), 'Could not find pwds binary!' )
        self.safeFile = '/tmp/pwdsTest.safe'

    def tearDown( self ):
        pass

    def runPwds( self, cmd, passwordPrompts=[ 'Enter password for .*: ' ],
             promptsAndInputs=[] ):
        cmd = '%s --file %s' % ( cmd, self.safeFile )
        return runPwds( self.executable, cmd, self.filepass, passwordPrompts=passwordPrompts,
                promptsAndInputs=promptsAndInputs )

    def initSafe( self ):
        if os.path.isfile( self.safeFile ):
            os.remove( self.safeFile )
        # extra password for file creation
        ret = self.runPwds( 'show', passwordPrompts=[ 'Enter new .*: ', 'Confirm .*: ' ] )
        self.assertTrue( os.path.isfile( self.safeFile ) )

    def assertLines( self, lines, exp ):
        for l, e in zip( lines, exp ):
            self.assertRegexpMatches( l, e )

