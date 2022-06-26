from book import Book
from node import Node



def main():
	a = Book("ivan", "ivan franko", 2110, "mria", 12.3)
	b = Book("aleg", "taras sevchenko", 2110, "d", 12.3)
	d = Book("veres", "joanne rowling", 2110, "ukraine", 12.3) 
       
	tree = Node(a)
	tree.insert(d)
	tree.insert(b)


	print(tree.print_tree())
	print("-----------")
	print(tree.find("ukraine"))
	print("-----------")
	print(tree.delete("d"))
	print(tree.print_tree())


 
 
if __name__ == '__main__':
    main()