class LinkedList:

	def __init__ ( self, head = None, size = 0, tail = None ):

		self.head = head

		self.size = size

		self.tail = tail

	def setHead( self, new_head ):

		self.head = new_head

	def getHead( self ):

		return( self.head )

	def setSize( self, new_size ):

		self.size = new_size

	def getSize( self ):

		return( self.size )

	def getTail( self ):

		return( self.tail )

	def setTail( self, t ):

		self.tail = t

	def isEmpty( self ):

		if (self.getSize() == 0):

			return( True )

		return( False )

	def addNode( self, d ):

		newNode = Node( data = d )

		if( self.isEmpty()):

			self.setHead( newNode )

		else:

			self.getTail().setNextPointer( newNode )

		self.setTail( newNode )

		self.setSize( self.size + 1 )


def main():

	n = Node( data = 100 )

	print( n.getData())

	ll = LinkedList()

	ll.addNode(10)

	print(ll.getTail().getData())
if __name__ == '__main__':
	main()