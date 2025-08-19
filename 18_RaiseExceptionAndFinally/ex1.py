# python has Many buildin Exception,Memory Error,IndexError,KeyError,TypeError,ValueError,ZeroDivisionError
try:
    raise MemoryError("This is a Memory Error") # you can write only Exception Class here because  MemoryError is a subclass of Exception
except MemoryError as e:
    print(e)
