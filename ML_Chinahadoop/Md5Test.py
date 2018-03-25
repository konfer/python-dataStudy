# coding:utf-8

import hashlib

if __name__ == "__main__":
	md5 = hashlib.md5()
	md5.update("This is a sentence".encode("utf-8"))
	print(u"不出意外，乱码：", md5.digest())
	print("md5(u):", md5.hexdigest())
	print(md5.digest_size, md5.block_size)
	print("-----------")
	
	sha1 = hashlib.sha1()
	sha1.update("This is a sentence".encode("utf-8"))
	print(sha1.digest,":",sha1.hexdigest())
	print(sha1.digest_size,sha1.block_size)
	
	  