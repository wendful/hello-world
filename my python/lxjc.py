#菱形继承
#多个子类继承同一个父类，这些子类由同一个类继承
class (A):
	pass
class B(A):
	pass
class C(A):
	pass
class D(B,C):
	pass