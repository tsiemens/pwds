#!/usr/bin/env python

import os
import unittest
from PwdsTestLib import PwdsBaseTest

class PwdsBasicTest( PwdsBaseTest ):

    def setUp( self ):
        super( PwdsBasicTest, self ).setUp()
        self.initSafe()

    def tearDown( self ):
        os.remove( self.safeFile )

    def test_second_run( self ):
        out = self.runPwds( 'show --raw' )
        self.assertLines( out, [ '\[\]' ] )

    def test_no_args( self ):
        out= self.runPwds( '', passwordPrompts=[] )
        self.assertLines( out, [ 'usage' ] )

    def test_add( self ):
        print 'thing'

if __name__ == '__main__':
    unittest.main()
