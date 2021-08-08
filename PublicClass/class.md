# 类的定义和使用

+ ```python
  #! /usr/bin/env python3
  # -*- coding: utf-8 -*-
  # __author__ : YiXuan
  # __date__ : 2021/3/24 10:52
  # __software__ : PyCharm
  
  class Test(object):
      """ 类属性 """
      class_attribute = 200
  
      """ 类方法 """
      @classmethod
      def class_method(cls, value):
          print(f'tip: {value} (类方法中输出类属性: {cls.class_attribute})')
  
      """ 静态方法 """
      @staticmethod
      def static_method(value):
          print(f'tip: {value}')
  
      """ 初始化实例属性 """
      def __init__(self, name=None):
          self.name = name
  
      """ 实例方法 """
      def self_method(self, value):
          print(f'tip: {value}')
  
  
  if __name__ == '__main__':
      print(f'=== 类相关 ===')
      t1 = Test()
      # 类属性
      print(f'类对象输出类属性: {Test.class_attribute}')
      print(f'实例对象输出类属性: {t1.class_attribute}')
      # 类方法
      t1.class_method(value='实例对象调用类方法')
      Test.class_method(value='类对象调用类方法')
  
      print(f'\n=== 实例相关 ===')
      # 初始化时定义实例属性
      t2 = Test(name='jack')
  
      t2.age = 18
      print(f'实例对象输出实例属性: {t2.name}, {t2.age}')
      # 实例方法
      t2.self_method(value='实例对象调用实例方法')
  
      print(f'\n=== 静态方法 ===')
      # 静态方法
      t3 = Test()
      t3.static_method(value='实例对象调用静态方法')
      Test.static_method(value='类对象调用静态方法')
  
      
  # output
  '''
  === 类相关 ===
  类对象输出类属性: 200
  实例对象输出类属性: 200
  tip: 实例对象调用类方法 (类方法中输出类属性: 200)
  tip: 类对象调用类方法 (类方法中输出类属性: 200)
  
  === 实例相关 ===
  实例对象输出实例属性: jack, 18
  tip: 实例对象调用实例方法
  
  === 静态方法 ===
  tip: 实例对象调用静态方法
  tip: 类对象调用静态方法
  
  '''
  ```