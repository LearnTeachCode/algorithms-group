# comment ou
class ListNode:
    def __init__(self, val=None):
        self.data = val
        self.next = None
class LinkedList:
	def __init__(self):
		self.head = None
	
	def setHead(self, head):
		self.head = head

my_list = LinkedList()
node = ListNode(10)
my_list.setHead(node)
