# 装饰器

## 什么是装饰器？

- 装饰器是要把原来的函数装饰成新的函数，并且返回这个函数本身的高阶函数

## 示例1：常规的装饰器

- ```python
  def decorator1(func):
      def wrapper1(*args, **kwargs):
          print('准备执行...')
          func(*args, **kwargs)
          print('执行成功！')
      return wrapper1
  
  
  @decorator1
  def wrapped1():
      print(f'被装饰函数1: {wrapped1.__name__}')
      print('签名指向 => wrapper1')
  
  if __name__ == '__main__':
      wrapped1()
       
  # output
  '''
  准备执行...
  被装饰函数1: wrapper1
  签名指向 => wrapper1
  执行成功！
  '''
  ```

## 示例2：解决常规装饰器的签名问题

- ```python
  import functools
  
  def decorator2(func):
      @functools.wraps(func)
      def wrapper2(*args, **kwargs):
          print('start executing...')
          func(*args, **kwargs)
          print('execution succeed')
      return wrapper2
  
  
  @decorator2
  def wrapped2():
      print(f'被装饰函数2: {wrapped2.__name__}')
      print('签名指向 => wrapped2')
      
  if __name__ == '__main__':
      wrapped2()
          
  # output
  '''
  start executing...
  被装饰函数2: wrapped2
  签名指向 => wrapped2
  execution succeed
  '''
  ```

## 示例3：使用 decorator 库实现装饰器

- ```python
  from decorator import decorator
  
  @decorator
  def wrapper3(func, *args, **kwargs):
      print('starting executing...')
      func(*args, **kwargs)
      print('execution succeed')
  
  
  @wrapper3
  def wrapped3():
      print(f'被装饰函数3: {wrapped3.__name__}')
      print(f'签名指向 => wrapped3')
      
  if __name__ == '__main__':
      wrapped3()
      
  # output
  '''
  starting executing...
  被装饰函数3: wrapped3
  签名指向 => wrapped3
  execution succeed
  
  '''
  ```

## 示例4：使用 decorator 库实现带参数的装饰器

- ```python
  import time
  from decorator import decorator
  
  @decorator
  def wrapper4(func, timelimit=60, *args, **kwargs):
      print(f'starting executing...')
      start_time = time.time()
      result = func(*args, **kwargs)
      end_time = time.time()
      dt = end_time - start_time
      if dt > timelimit:
          print(f'超时完成: {dt} s')
      else:
          print(f'限时内完成: {dt} s')
      print('execution succeed!')
      return result
  
  
  @wrapper4(timelimit=60)
  def wrapped4(*args, **kwargs):
      print(f'被装饰函数4: {wrapped4.__name__}')
      print('签名指向 => wrapped4')
      print(args)
      print(kwargs)
  
  
  if __name__ == '__main__':
      wrapped4(1, 2, 3, a=1, b=2, c=3)
          
  # output
  '''
  starting executing...
  被装饰函数4: wrapped4
  签名指向 => wrapped4
  (1, 2, 3)
  {'a': 1, 'b': 2, 'c': 3}
  限时内完成: 0.0 s
  execution succeed!
  '''
  ```

- 

