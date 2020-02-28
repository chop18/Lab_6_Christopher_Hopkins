class Node:

	def __init__ ( self, data, nextPointer = None ):

		self.data 	     = data

		self.nextPointer = nextPointer

	def setData( self, nData ):

		self.data = nData

	def getData( self ):

		return( self.data )

	def setNextPointer( self, new_nextPointer ):

		self.nextPointer = new_nextPointer

	def getNextPointer( self ):

		return( self.nextPointer )

