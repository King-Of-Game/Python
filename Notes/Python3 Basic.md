# python3笔记

## 变量和对象的关系 *

+ 在 python 中，类型属于对象，变量是没有类型的：

+ ```python
  a=[1,2,3]
  a="Runoob"
  
  '''
  以上代码中，[1,2,3] （对象）是 List 类型，"Runoob"（对象） 是 String 类型，而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），可以是指向 List 类型对象，也可以是指向 String 类型对象。
  '''
  ```

## 查看模块当前版本的所有关键字

+ ```python
  >>> import keyword
  >>> keyword.kwlist
  ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
  ```

## python字符串格式化符号

python字符串格式化符号:



| 符  号 |                 描述                 |
| :----: | :----------------------------------: |
|   %c   |        格式化字符及其ASCII码         |
|   %s   |             格式化字符串             |
|   %d   |              格式化整数              |
|   %u   |           格式化无符号整型           |
|   %o   |         格式化无符号八进制数         |
|   %x   |        格式化无符号十六进制数        |
|   %X   |    格式化无符号十六进制数（大写）    |
|   %f   | 格式化浮点数字，可指定小数点后的精度 |
|   %e   |       用科学计数法格式化浮点数       |
|   %E   |  作用同%e，用科学计数法格式化浮点数  |
|   %g   |             %f和%e的简写             |
|   %G   |           %f 和 %E 的简写            |
|   %p   |     用十六进制数格式化变量的地址     |

## 注释的使用方法

+ 输出函数的注释

  + ```python
    def a():
        '''这是文档字符串'''
        pass
    print(a.__doc__)
    
    # output
    '''
    这是文档字符串
    '''
    ```

+ 三个双引号赋值给字符串变量时，表示一种字符串换行的特殊写法。

  + ```python
    >>> str="""
    ... want
    ... you"""
    >>> str
    'I\nwant\nyou'
    >>> print(str)
    I
    want
    you
    ```

## if __name__ == '__main__' 的作用

- ```python
  if __name__ == '__main__':
      print('仅供模块本身')
  
      def print_1(par):
          print("Hello : ", par)
          return
  
  else:
      print('所有人均可')
  
      def print_2():
          print("Hello, everyone")
          return
  ```



## ------------------------------------------------

## Python3 的六个标准数据类型

+ **不可变数据（3 个）：**Number（数字）、String（字符串）、Tuple（元组）

+ **可变数据（3 个）：**List（列表）、Dictionary（字典）、Set（集合）


## 数字-Number

- **整型(Int)** - 通常被称为是整型或整数，是正或负整数，不带小数点。Python3 整型是没有限制大小的，可以当作 Long 类型使用，所以 Python3 没有 Python2 的 Long 类型。
- **浮点型(float)** - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 10² = 250）

### 实现数学上的四舍五入

+ ```python
  from decimal import Decimal, ROUND_HALF_UP
  
  float1 = 1.345
      print(Decimal(str(float1)).quantize(Decimal('0.00'), rounding=ROUND_HALF_UP))
  
  # output
  '''
  1.35
  '''
  ```

+ 

**复数( (complex))** - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。

### 数学函数

+ | 函数                                                         | 返回值 ( 描述 )                                              |
  | :----------------------------------------------------------- | :----------------------------------------------------------- |
  | [abs(x)](https://www.runoob.com/python3/python3-func-number-abs.html) | 返回数字的绝对值，如abs(-10) 返回 10                         |
  | [ceil(x)](https://www.runoob.com/python3/python3-func-number-ceil.html) | 返回数字的上入整数，如math.ceil(4.1) 返回 5                  |
  | cmp(x, y)                                                    | 如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 **Python 3 已废弃，使用 (x>y)-(x<y) 替换**。 |
  | [exp(x)](https://www.runoob.com/python3/python3-func-number-exp.html) | 返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045         |
  | [fabs(x)](https://www.runoob.com/python3/python3-func-number-fabs.html) | 返回数字的绝对值，如math.fabs(-10) 返回10.0                  |
  | [floor(x)](https://www.runoob.com/python3/python3-func-number-floor.html) | 返回数字的下舍整数，如math.floor(4.9)返回 4                  |
  | [log(x)](https://www.runoob.com/python3/python3-func-number-log.html) | 如math.log(math.e)返回1.0,math.log(100,10)返回2.0            |
  | [log10(x)](https://www.runoob.com/python3/python3-func-number-log10.html) | 返回以10为基数的x的对数，如math.log10(100)返回 2.0           |
  | [max(x1, x2,...)](https://www.runoob.com/python3/python3-func-number-max.html) | 返回给定参数的最大值，参数可以为序列。                       |
  | [min(x1, x2,...)](https://www.runoob.com/python3/python3-func-number-min.html) | 返回给定参数的最小值，参数可以为序列。                       |
  | [modf(x)](https://www.runoob.com/python3/python3-func-number-modf.html) | 返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。 |
  | [pow(x, y)](https://www.runoob.com/python3/python3-func-number-pow.html) | x**y 运算后的值。                                            |
  | [round(x [,n\])](https://www.runoob.com/python3/python3-func-number-round.html) | 返回浮点数 x 的四舍五入值，如给出 n 值，则代表舍入到小数点后的位数。**其实准确的说是保留值将保留到离上一位更近的一端。** |
  | [sqrt(x)](https://www.runoob.com/python3/python3-func-number-sqrt.html) | 返回数字x的平方根。                                          |

### 随机数函数

+ 随机数可以用于数学，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。

+ | 函数                                                         | 描述                                                         |
  | :----------------------------------------------------------- | :----------------------------------------------------------- |
  | [choice(seq)](https://www.runoob.com/python3/python3-func-number-choice.html) | 从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。 |
  | [randrange ([start,\] stop [,step])](https://www.runoob.com/python3/python3-func-number-randrange.html) | 从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1 |
  | [random()](https://www.runoob.com/python3/python3-func-number-random.html) | 随机生成下一个实数，它在[0,1)范围内。                        |
  | [seed([x\])](https://www.runoob.com/python3/python3-func-number-seed.html) | 改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。 |
  | [shuffle(lst)](https://www.runoob.com/python3/python3-func-number-shuffle.html) | 将序列的所有元素随机排序                                     |
  | [uniform(x, y)](https://www.runoob.com/python3/python3-func-number-uniform.html) | 随机生成下一个实数，它在[x,y]范围内。                        |

### 三角函数

+ | 函数                                                         | 描述                                              |
  | :----------------------------------------------------------- | :------------------------------------------------ |
  | [acos(x)](https://www.runoob.com/python3/python3-func-number-acos.html) | 返回x的反余弦弧度值。                             |
  | [asin(x)](https://www.runoob.com/python3/python3-func-number-asin.html) | 返回x的反正弦弧度值。                             |
  | [atan(x)](https://www.runoob.com/python3/python3-func-number-atan.html) | 返回x的反正切弧度值。                             |
  | [atan2(y, x)](https://www.runoob.com/python3/python3-func-number-atan2.html) | 返回给定的 X 及 Y 坐标值的反正切值。              |
  | [cos(x)](https://www.runoob.com/python3/python3-func-number-cos.html) | 返回x的弧度的余弦值。                             |
  | [hypot(x, y)](https://www.runoob.com/python3/python3-func-number-hypot.html) | 返回欧几里德范数 sqrt(x*x + y*y)。                |
  | [sin(x)](https://www.runoob.com/python3/python3-func-number-sin.html) | 返回的x弧度的正弦值。                             |
  | [tan(x)](https://www.runoob.com/python3/python3-func-number-tan.html) | 返回x弧度的正切值。                               |
  | [degrees(x)](https://www.runoob.com/python3/python3-func-number-degrees.html) | 将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0 |
  | [radians(x)](https://www.runoob.com/python3/python3-func-number-radians.html) | 将角度转换为弧度                                  |

### 数学常量

+ | 常量 | 描述                                  |
  | :--- | :------------------------------------ |
  | pi   | 数学常量 pi（圆周率，一般以π来表示）  |
  | e    | 数学常量 e，e即自然常数（自然常数）。 |

## 字符串-String

### 转义字符

+ 在需要在字符中使用特殊字符时，python 用反斜杠 **\** 转义字符。如下表：

+ | 转义字符    | 描述                                                      | 实例                                                         |
  | :---------- | :-------------------------------------------------------- | :----------------------------------------------------------- |
  | \(在行尾时) | 续行符                                                    | `>>> print("line1 \ ... line2 \ ... line3") line1 line2 line3 >>> ` |
  | \\\         | 反斜杠符号                                                | `>>> print("\\") \`                                          |
  | \\'         | 单引号                                                    | `>>> print('\'') '`                                          |
  | \\"         | 双引号                                                    | `>>> print("\"") "`                                          |
  | \a          | 响铃                                                      | `>>> print("\a")`执行后电脑有响声。                          |
  | \b          | 退格(Backspace)                                           | `>>> print("Hello \b World!") Hello World!`                  |
  | \000        | 空                                                        | `>>> print("\000") >>> `                                     |
  | \n          | 换行                                                      | `>>> print("\n")  >>>`                                       |
  | \v          | 纵向制表符                                                | `>>> print("Hello \v World!") Hello        World! >>>`       |
  | \t          | 横向制表符                                                | `>>> print("Hello \t World!") Hello    World! >>>`           |
  | \r          | 回车                                                      | `>>> print("Hello\rWorld!") World!`                          |
  | \f          | 换页                                                      | `>>> print("Hello \f World!") Hello        World! >>> `      |
  | \yyy        | 八进制数，y 代表 0~7 的字符，例如：\012 代表换行。        | `>>> print("\110\145\154\154\157\40\127\157\162\154\144\41") Hello World!` |
  | \xyy        | 十六进制数，以 \x 开头，y 代表的字符，例如：\x0a 代表换行 | `>>> print("\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64\x21") Hello World!` |
  | \other      | 其它的字符以普通格式输出                                  |                                                              |

### 字符串运算符

+ 下表实例变量 a 值为字符串 "Hello"，b 变量值为 "Python"：

+ | 操作符 | 描述                                                         | 实例                            |
  | :----- | :----------------------------------------------------------- | :------------------------------ |
  | +      | 字符串连接                                                   | a + b 输出结果： HelloPython    |
  | *      | 重复输出字符串                                               | a*2 输出结果：HelloHello        |
  | []     | 通过索引获取字符串中字符                                     | a[1] 输出结果 **e**             |
  | [ : ]  | 截取字符串中的一部分，遵循**左闭右开**原则，str[0:2] 是不包含第 3 个字符的。 | a[1:4] 输出结果 **ell**         |
  | in     | 成员运算符 - 如果字符串中包含给定的字符返回 True             | **'H' in a** 输出结果 True      |
  | not in | 成员运算符 - 如果字符串中不包含给定的字符返回 True           | **'M' not in a** 输出结果 True  |
  | r/R    | 原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母 **r**（可以大小写）以外，与普通字符串有着几乎完全相同的语法。 | `print( r'\n' ) print( R'\n' )` |
  | %      | 格式字符串                                                   |                                 |

### 字符串格式化

+ python字符串格式化符号如下表:

+ | 符  号 | 描述                                 |
  | :----- | :----------------------------------- |
  | %c     | 格式化字符及其ASCII码                |
  | %s     | 格式化字符串                         |
  | %d     | 格式化整数                           |
  | %u     | 格式化无符号整型                     |
  | %o     | 格式化无符号八进制数                 |
  | %x     | 格式化无符号十六进制数               |
  | %X     | 格式化无符号十六进制数（大写）       |
  | %f     | 格式化浮点数字，可指定小数点后的精度 |
  | %e     | 用科学计数法格式化浮点数             |
  | %E     | 作用同%e，用科学计数法格式化浮点数   |
  | %g     | %f和%e的简写                         |
  | %G     | %f 和 %E 的简写                      |
  | %p     | 用十六进制数格式化变量的地址         |
  + 格式化操作符辅助指令

  + | 符号  | 功能                                                         |
    | :---- | :----------------------------------------------------------- |
    | *     | 定义宽度或者小数点精度                                       |
    | -     | 用做左对齐                                                   |
    | +     | 在正数前面显示加号( + )                                      |
    | <sp>  | 在正数前面显示空格                                           |
    | #     | 在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X') |
    | 0     | 显示的数字前面填充'0'而不是默认的空格                        |
    | %     | '%%'输出一个单一的'%'                                        |
    | (var) | 映射变量(字典参数)                                           |
    | m.n.  | m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)        |

### 三引号

+ python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符。实例如下

+ ```python
  #!/usr/bin/python3
   
  para_str = """这是一个多行字符串的实例
  多行字符串可以使用制表符
  TAB ( \t )。
  也可以使用换行符 [ \n ]。
  """
  print (para_str)
  
  
  # 以上实例执行结果为：
  这是一个多行字符串的实例
  多行字符串可以使用制表符
  TAB (    )。
  也可以使用换行符 [ 
   ]。
  
  ```

+ 三引号让程序员从引号和特殊字符串的泥潭里面解脱出来，自始至终保持一小块字符串的格式是所谓的WYSIWYG（所见即所得）格式的。

+ ```python
  errHTML = '''
  <HTML><HEAD><TITLE>
  Friends CGI Demo</TITLE></HEAD>
  <BODY><H3>ERROR</H3>
  <B>%s</B><P>
  <FORM><INPUT TYPE=button VALUE=Back
  ONCLICK="window.history.back()"></FORM>
  </BODY></HTML>
  '''
  cursor.execute('''
  CREATE TABLE users (  
  login VARCHAR(8), 
  uid INTEGER,
  prid INTEGER)
  ''')
  ```

### f-string

+ f-string 是 python3.6 之后版本添加的，称之为字面量格式化字符串，是新的格式化字符串的语法。

+ 

  ```python
  >>> name = 'Runoob'
  >>> f'Hello {name}'  # 替换变量
  
  >>> f'{1+2}'         # 使用表达式
  '3'
  
  >>> w = {'name': 'Runoob', 'url': 'www.runoob.com'}
  >>> f'{w["name"]}: {w["url"]}'
  'Runoob: www.runoob.com'
  ```

+ tips: 在 Python 3.8 的版本中可以使用 **=** 符号来拼接运算表达式与结果。

+ ```python
  >>> x = 1
  >>> print(f'{x+1}')   # Python 3.6
  2
  
  >>> x = 1
  >>> print(f'{x+1=}')   # Python 3.8
  'x+1=2'
  ```

### 字符串内建函数

+ | 序号 | 方法及描述                                                   |
  | :--- | :----------------------------------------------------------- |
  | 1    | [capitalize()](https://www.runoob.com/python3/python3-string-capitalize.html) 将字符串的第一个字符转换为大写 |
  | 2    | [center(width, fillchar)](https://www.runoob.com/python3/python3-string-center.html) 返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。 |
  | 3    | [count(str, beg= 0,end=len(string))](https://www.runoob.com/python3/python3-string-count.html) 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数 |
  | 4    | [bytes.decode(encoding="utf-8", errors="strict")](https://www.runoob.com/python3/python3-string-decode.html) Python3 中没有 decode 方法，但我们可以使用 bytes 对象的 decode() 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode() 来编码返回。 |
  | 5    | [encode(encoding='UTF-8',errors='strict')](https://www.runoob.com/python3/python3-string-encode.html) 以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace' |
  | 6    | [endswith(suffix, beg=0, end=len(string))](https://www.runoob.com/python3/python3-string-endswith.html) 检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False. |
  | 7    | [expandtabs(tabsize=8)](https://www.runoob.com/python3/python3-string-expandtabs.html) 把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8 。 |
  | 8    | [find(str, beg=0, end=len(string))](https://www.runoob.com/python3/python3-string-find.html) 检测 str 是否包含在字符串中，如果指定范围 beg 和 end ，则检查是否包含在指定范围内，如果包含返回开始的索引值，否则返回-1 |
  | 9    | [index(str, beg=0, end=len(string))](https://www.runoob.com/python3/python3-string-index.html) 跟find()方法一样，只不过如果str不在字符串中会报一个异常。 |
  | 10   | [isalnum()](https://www.runoob.com/python3/python3-string-isalnum.html) 如果字符串至少有一个字符并且所有字符都是字母或数字则返 回 True，否则返回 False |
  | 11   | [isalpha()](https://www.runoob.com/python3/python3-string-isalpha.html) 如果字符串至少有一个字符并且所有字符都是字母或中文字则返回 True, 否则返回 False |
  | 12   | [isdigit()](https://www.runoob.com/python3/python3-string-isdigit.html) 如果字符串只包含数字则返回 True 否则返回 False.. |
  | 13   | [islower()](https://www.runoob.com/python3/python3-string-islower.html) 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False |
  | 14   | [isnumeric()](https://www.runoob.com/python3/python3-string-isnumeric.html) 如果字符串中只包含数字字符，则返回 True，否则返回 False |
  | 15   | [isspace()](https://www.runoob.com/python3/python3-string-isspace.html) 如果字符串中只包含空白，则返回 True，否则返回 False. |
  | 16   | [istitle()](https://www.runoob.com/python3/python3-string-istitle.html) 如果字符串是标题化的(见 title())则返回 True，否则返回 False |
  | 17   | [isupper()](https://www.runoob.com/python3/python3-string-isupper.html) 如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False |
  | 18   | [join(seq)](https://www.runoob.com/python3/python3-string-join.html) 以指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串 |
  | 19   | [len(string)](https://www.runoob.com/python3/python3-string-len.html) 返回字符串长度 |
  | 20   | [ljust(width[, fillchar\])](https://www.runoob.com/python3/python3-string-ljust.html) 返回一个原字符串左对齐,并使用 fillchar 填充至长度 width 的新字符串，fillchar 默认为空格。 |
  | 21   | [lower()](https://www.runoob.com/python3/python3-string-lower.html) 转换字符串中所有大写字符为小写. |
  | 22   | [lstrip()](https://www.runoob.com/python3/python3-string-lstrip.html) 截掉字符串左边的空格或指定字符。 |
  | 23   | [maketrans()](https://www.runoob.com/python3/python3-string-maketrans.html) 创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。 |
  | 24   | [max(str)](https://www.runoob.com/python3/python3-string-max.html) 返回字符串 str 中最大的字母。 |
  | 25   | [min(str)](https://www.runoob.com/python3/python3-string-min.html) 返回字符串 str 中最小的字母。 |
  | 26   | [replace(old, new [, max\])](https://www.runoob.com/python3/python3-string-replace.html) 把 将字符串中的 old 替换成 new,如果 max 指定，则替换不超过 max 次。 |
  | 27   | [rfind(str, beg=0,end=len(string))](https://www.runoob.com/python3/python3-string-rfind.html) 类似于 find()函数，不过是从右边开始查找. |
  | 28   | [rindex( str, beg=0, end=len(string))](https://www.runoob.com/python3/python3-string-rindex.html) 类似于 index()，不过是从右边开始. |
  | 29   | [rjust(width,[, fillchar\])](https://www.runoob.com/python3/python3-string-rjust.html) 返回一个原字符串右对齐,并使用fillchar(默认空格）填充至长度 width 的新字符串 |
  | 30   | [rstrip()](https://www.runoob.com/python3/python3-string-rstrip.html) 删除字符串字符串末尾的空格. |
  | 31   | [split(str="", num=string.count(str))](https://www.runoob.com/python3/python3-string-split.html) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num+1 个子字符串 |
  | 32   | [splitlines([keepends\])](https://www.runoob.com/python3/python3-string-splitlines.html) 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。 |
  | 33   | [startswith(substr, beg=0,end=len(string))](https://www.runoob.com/python3/python3-string-startswith.html) 检查字符串是否是以指定子字符串 substr 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查。 |
  | 34   | [strip([chars\])](https://www.runoob.com/python3/python3-string-strip.html) 在字符串上执行 lstrip()和 rstrip() |
  | 35   | [swapcase()](https://www.runoob.com/python3/python3-string-swapcase.html) 将字符串中大写转换为小写，小写转换为大写 |
  | 36   | [title()](https://www.runoob.com/python3/python3-string-title.html) 返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle()) |
  | 37   | [translate(table, deletechars="")](https://www.runoob.com/python3/python3-string-translate.html) 根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中 |
  | 38   | [upper()](https://www.runoob.com/python3/python3-string-upper.html) 转换字符串中的小写字母为大写 |
  | 39   | [zfill (width)](https://www.runoob.com/python3/python3-string-zfill.html) 返回长度为 width 的字符串，原字符串右对齐，前面填充0 |
  | 40   | [isdecimal()](https://www.runoob.com/python3/python3-string-isdecimal.html) 检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。 |

## 列表-List

### 删除列表元素

+ 可以使用 del 语句来删除列表的的元素，如下实例：

+ ```python
  #!/usr/bin/python3
   
  list = ['Google', 'Runoob', 1997, 2000]
   
  print ("原始列表 : ", list)
  del list[2]
  print ("删除第三个元素 : ", list)
  
  # 以上实例输出结果：
  原始列表 :  ['Google', 'Runoob', 1997, 2000]
  删除第三个元素 :  ['Google', 'Runoob', 2000]
  ```

### 列表脚本操作符

+ 列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。

+ | Python 表达式                         | 结果                         | 描述                 |
  | :------------------------------------ | :--------------------------- | :------------------- |
  | len([1, 2, 3])                        | 3                            | 长度                 |
  | [1, 2, 3] + [4, 5, 6]                 | [1, 2, 3, 4, 5, 6]           | 组合                 |
  | ['Hi!'] * 4                           | ['Hi!', 'Hi!', 'Hi!', 'Hi!'] | 重复                 |
  | 3 in [1, 2, 3]                        | True                         | 元素是否存在于列表中 |
  | for x in [1, 2, 3]: print(x, end=" ") | 1 2 3                        | 迭代                 |

### 列表截取与拼接

+ | Python 表达式 | 结果                 | 描述                                               |
  | :------------ | :------------------- | :------------------------------------------------- |
  | L[2]          | 'Taobao'             | 读取第三个元素                                     |
  | L[-2]         | 'Runoob'             | 从右侧开始读取倒数第二个元素: count from the right |
  | L[1:]         | ['Runoob', 'Taobao'] | 输出从第二个元素开始后的所有元素                   |

+ ```python
  # example1
  >>>L=['Google', 'Runoob', 'Taobao']
  >>> L[2]
  'Taobao'
  >>> L[-2]
  'Runoob'
  >>> L[1:]
  ['Runoob', 'Taobao']
  
  # example2
  >>>squares = [1, 4, 9, 16, 25]
  >>> squares += [36, 49, 64, 81, 100]
  >>> squares
  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
  ```

### 嵌套列表

+ 使用嵌套列表即在列表里创建其它列表，例如：

+ ```python
  >>>a = ['a', 'b', 'c']
  >>> n = [1, 2, 3]
  >>> x = [a, n]
  >>> x
  [['a', 'b', 'c'], [1, 2, 3]]
  >>> x[0]
  ['a', 'b', 'c']
  >>> x[0][1]
  'b'
  ```

### 列表函数&方法

+ 列表包含以下函数

+ | 序号 | 函数                                                         |
  | :--- | :----------------------------------------------------------- |
  | 1    | [len(list)](https://www.runoob.com/python3/python3-att-list-len.html) 列表元素个数 |
  | 2    | [max(list)](https://www.runoob.com/python3/python3-att-list-max.html) 返回列表元素最大值 |
  | 3    | [min(list)](https://www.runoob.com/python3/python3-att-list-min.html) 返回列表元素最小值 |
  | 4    | [list(seq)](https://www.runoob.com/python3/python3-att-list-list.html) 将元组转换为列表 |

+ 列表包含以下方法

+ | 序号 | 方法                                                         |
  | :--- | :----------------------------------------------------------- |
  | 1    | [list.append(obj)](https://www.runoob.com/python3/python3-att-list-append.html) 在列表末尾添加新的对象 |
  | 2    | [list.count(obj)](https://www.runoob.com/python3/python3-att-list-count.html) 统计某个元素在列表中出现的次数 |
  | 3    | [list.extend(seq)](https://www.runoob.com/python3/python3-att-list-extend.html) 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表） |
  | 4    | [list.index(obj)](https://www.runoob.com/python3/python3-att-list-index.html) 从列表中找出某个值第一个匹配项的索引位置 |
  | 5    | [list.insert(index, obj)](https://www.runoob.com/python3/python3-att-list-insert.html) 将对象插入列表 |
  | 6    | [list.pop([index=-1\])](https://www.runoob.com/python3/python3-att-list-pop.html) 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值 |
  | 7    | [list.remove(obj)](https://www.runoob.com/python3/python3-att-list-remove.html) 移除列表中某个值的第一个匹配项 |
  | 8    | [list.reverse()](https://www.runoob.com/python3/python3-att-list-reverse.html) 反向列表中元素 |
  | 9    | [list.sort( key=None, reverse=False)](https://www.runoob.com/python3/python3-att-list-sort.html) 对原列表进行排序 |
  | 10   | [list.clear()](https://www.runoob.com/python3/python3-att-list-clear.html) 清空列表 |
  | 11   | [list.copy()](https://www.runoob.com/python3/python3-att-list-copy.html) 复制列表 |

## 元组-tuple

### 修改元组

+ 元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，如下实例:

  + ```python
    #!/usr/bin/python3
     
    tup1 = (12, 34.56)
    tup2 = ('abc', 'xyz')
     
    # 以下修改元组元素操作是非法的。
    # tup1[0] = 100
     
    # 创建一个新的元组
    tup3 = tup1 + tup2
    print (tup3)
    
    # 输出结果：
    (12, 34.56, 'abc', 'xyz')
    ```

### 删除元组

+ 元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组，如下实例:

  + ```python
    #!/usr/bin/python3
     
    tup = ('Google', 'Runoob', 1997, 2000)
     
    print (tup)
    del tup
    print ("删除后的元组 tup : ")
    print (tup)
    
    # 以上实例元组被删除后，输出变量会有异常信息，输出如下所示：
    '''
    删除后的元组 tup : 
    Traceback (most recent call last):
      File "test.py", line 8, in <module>
        print (tup)
    NameError: name 'tup' is not defined
    '''
    ```

### 元组运算符

+ 与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。

+ | Python 表达式                  | 结果                         | 描述         |
  | :----------------------------- | :--------------------------- | :----------- |
  | len((1, 2, 3))                 | 3                            | 计算元素个数 |
  | (1, 2, 3) + (4, 5, 6)          | (1, 2, 3, 4, 5, 6)           | 连接         |
  | ('Hi!',) * 4                   | ('Hi!', 'Hi!', 'Hi!', 'Hi!') | 复制         |
  | 3 in (1, 2, 3)                 | True                         | 元素是否存在 |
  | for x in (1, 2, 3): print (x,) | 1 2 3                        | 迭代         |

### 元组索引&截取

+ | Python 表达式 | 结果                                            | 描述                                             |
  | :------------ | :---------------------------------------------- | :----------------------------------------------- |
  | tup[1]        | 'Runoob'                                        | 读取第二个元素                                   |
  | tup[-2]       | 'Weibo'                                         | 反向读取，读取倒数第二个元素                     |
  | tup[1:]       | ('Runoob', 'Taobao', 'Wiki', 'Weibo', 'Weixin') | 截取元素，从第二个开始后的所有元素。             |
  | tup[1:4]      | ('Runoob', 'Taobao', 'Wiki')                    | 截取元素，从第二个开始到第四个元素（索引为 3）。 |

+ ```python
  >>> tup = ('Google', 'Runoob', 'Taobao', 'Wiki', 'Weibo','Weixin')
  >>> tup[1]
  'Runoob'
  >>> tup[-2]
  'Weibo'
  >>> tup[1:]
  ('Runoob', 'Taobao', 'Wiki', 'Weibo', 'Weixin')
  >>> tup[1:4]
  ('Runoob', 'Taobao', 'Wiki')
  >>>
  ```

### 元组内置函数

+ | 序号 | 方法及描述                               | 实例                                                         |
  | :--- | :--------------------------------------- | :----------------------------------------------------------- |
  | 1    | len(tuple) 计算元组元素个数。            | `>>> tuple1 = ('Google', 'Runoob', 'Taobao') >>> len(tuple1) 3 >>> ` |
  | 2    | max(tuple) 返回元组中元素最大值。        | `>>> tuple2 = ('5', '4', '8') >>> max(tuple2) '8' >>> `      |
  | 3    | min(tuple) 返回元组中元素最小值。        | `>>> tuple2 = ('5', '4', '8') >>> min(tuple2) '4' >>> `      |
  | 4    | tuple(iterable) 将可迭代系列转换为元组。 | `>>> list1= ['Google', 'Taobao', 'Runoob', 'Baidu'] >>> tuple1=tuple(list1) >>> tuple1 ('Google', 'Taobao', 'Runoob', 'Baidu')` |

### *关于元组是不可变的

+ 所谓元组的不可变指的是元组所指向的内存中的内容不可变。

+ ```python
  >>> tup = ('r', 'u', 'n', 'o', 'o', 'b')
  >>> tup[0] = 'g'     # 不支持修改元素
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: 'tuple' object does not support item assignment
  >>> id(tup)     # 查看内存地址
  4440687904
  >>> tup = (1,2,3)
  >>> id(tup)
  4441088800    # 内存地址不一样了
  
  # 从以上实例可以看出，重新赋值的元组 tup，绑定到新的对象了，不是修改了原来的对象。
  ```

## 字典-dict

### 修改字典

+ 向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:

  + ```python
    #!/usr/bin/python3
     
    dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
     
    dict['Age'] = 8               # 更新 Age
    dict['School'] = "菜鸟教程"  # 添加信息
     
     
    print ("dict['Age']: ", dict['Age'])
    print ("dict['School']: ", dict['School'])
    
    # 输出结果：
    '''
    dict['Age']:  8
    dict['School']:  菜鸟教程
    '''
    ```

### 删除字典元素

+ 删除单一元素、删除整个字典、清空字典，如下实例：

  + ```python
    #!/usr/bin/python3
     
    dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
     
    del dict['Name'] # 删除键 'Name'
    dict.clear()     # 清空字典
    del dict         # 删除字典
     
    print ("dict['Age']: ", dict['Age'])
    print ("dict['School']: ", dict['School'])
    
    # 但这会引发一个异常，因为用执行 del 操作后字典不再存在：
    '''
    Traceback (most recent call last):
      File "test.py", line 9, in <module>
        print ("dict['Age']: ", dict['Age'])
    TypeError: 'type' object is not subscriptable
    '''
    ```

### 字典键的特性

+ tip: 字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。

+ 1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：

  + ```python
    #!/usr/bin/python3
     
    dict = {'Name': 'Runoob', 'Age': 7, 'Name': '小菜鸟'}
    print ("dict['Name']: ", dict['Name'])
    
    # 输出结果
    '''
    dict['Name']:  小菜鸟
    '''
    ```

+ 2）键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如下实例：

  + ```python
    #!/usr/bin/python3
     
    dict = {['Name']: 'Runoob', 'Age': 7}
    print ("dict['Name']: ", dict['Name'])
    
    # 输出结果：
    '''
    Traceback (most recent call last):
      File "test.py", line 3, in <module>
        dict = {['Name']: 'Runoob', 'Age': 7}
    TypeError: unhashable type: 'list'
    '''
    ```

### 字典内置函数&方法

+ 字典包含了以下内置函数：

+ | 序号 | 函数及描述                                                   | 实例                                                         |
  | :--- | :----------------------------------------------------------- | :----------------------------------------------------------- |
  | 1    | len(dict) 计算字典元素个数，即键的总数。                     | `>>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'} >>> len(dict) 3` |
  | 2    | str(dict) 输出字典，以可打印的字符串表示。                   | `>>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'} >>> str(dict) "{'Name': 'Runoob', 'Class': 'First', 'Age': 7}"` |
  | 3    | type(variable) 返回输入的变量类型，如果变量是字典就返回字典类型。 | `>>> dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'} >>> type(dict) <class 'dict'>` |

+ 字典包含了以下内置方法：

+ | 序号 | 函数及描述                                                   |
  | :--- | :----------------------------------------------------------- |
  | 1    | [radiansdict.clear()](https://www.runoob.com/python3/python3-att-dictionary-clear.html) 删除字典内所有元素 |
  | 2    | [radiansdict.copy()](https://www.runoob.com/python3/python3-att-dictionary-copy.html) 返回一个字典的浅复制 |
  | 3    | [radiansdict.fromkeys()](https://www.runoob.com/python3/python3-att-dictionary-fromkeys.html) 创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值 |
  | 4    | [radiansdict.get(key, default=None)](https://www.runoob.com/python3/python3-att-dictionary-get.html) 返回指定键的值，如果键不在字典中返回 default 设置的默认值 |
  | 5    | [key in dict](https://www.runoob.com/python3/python3-att-dictionary-in.html) 如果键在字典dict里返回true，否则返回false |
  | 6    | [radiansdict.items()](https://www.runoob.com/python3/python3-att-dictionary-items.html) 以列表返回可遍历的(键, 值) 元组数组 |
  | 7    | [radiansdict.keys()](https://www.runoob.com/python3/python3-att-dictionary-keys.html) 返回一个迭代器，可以使用 list() 来转换为列表 |
  | 8    | [radiansdict.setdefault(key, default=None)](https://www.runoob.com/python3/python3-att-dictionary-setdefault.html) 和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default |
  | 9    | [radiansdict.update(dict2)](https://www.runoob.com/python3/python3-att-dictionary-update.html) 把字典dict2的键/值对更新到dict里 |
  | 10   | [radiansdict.values()](https://www.runoob.com/python3/python3-att-dictionary-values.html) 返回一个迭代器，可以使用 list() 来转换为列表 |
  | 11   | [pop(key[,default\])](https://www.runoob.com/python3/python3-att-dictionary-pop.html) 删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。 |
  | 12   | [popitem()](https://www.runoob.com/python3/python3-att-dictionary-popitem.html) 随机返回并删除字典中的最后一对键和值。 |

### 字典&字符串转换

+ ```python
  dict1 = {"Name": "Runoob", "Class": "First", "Age": 7}
  str1 = str(dict1)
  eval1 = eval(str1)
  
  print(type(dict1),dict1)
  print(type(str1),str1)
  print(type(eval1),eval1)
  
  # 输出结果
  '''
  <class 'dict'> {'Name': 'Runoob', 'Class': 'First', 'Age': 7}
  <class 'str'> {'Name': 'Runoob', 'Class': 'First', 'Age': 7}
  <class 'dict'> {'Name': 'Runoob', 'Class': 'First', 'Age': 7}
  '''
  ```

## 集合-set

### 定义

+ 集合（set）是一个无序的不重复元素序列。

+ 可以使用大括号 **{ }** 或者 **set()** 函数创建集合，注意：创建一个空集合必须用 **set()** 而不是 **{ }**，因为 **{ }** 是用来创建一个空字典。

  + ```python
    parame = {value1,value2,...}
    或者
    parame = set(value)
    ```

+ 实例

  + ```python
    #!/usr/bin/python3
    
    sites = {'Google', 'Taobao', 'Runoob', 'Facebook', 'Zhihu', 'Baidu'}
    
    print(sites)   # 输出集合，重复的元素被自动去掉
    
    # 成员测试
    if 'Runoob' in sites :
        print('Runoob 在集合中')
    else :
        print('Runoob 不在集合中')
    
    
    # set可以进行集合运算
    a = set('abracadabra')  # {'b', 'c', 'a', 'r', 'd'}
    b = set('alacazam')     # {'l', 'c', 'a', 'z', 'm'}
    
    print(a)  # {'b', 'c', 'a', 'r', 'd'}
    
    print(a - b)     # a 和 b 的差集: {'r', 'b', 'd'}
    
    print(a | b)     # a 和 b 的并集: {'b', 'c', 'a', 'z', 'm', 'r', 'l', 'd'}
    
    print(a & b)     # a 和 b 的交集: {'c', 'a'}
    
    print(a ^ b)     # a 和 b 中不同时存在的元素: {'z', 'b', 'm', 'r', 'l', 'd'}
    
    # output
    '''
    {'Zhihu', 'Baidu', 'Taobao', 'Runoob', 'Google', 'Facebook'}
    Runoob 在集合中
    '''
    ```
  
+ 类似列表推导式，同样集合支持集合推导式(Set comprehension):

  + ```python
    >>> a = {x for x in 'abracadabra' if x not in 'abc'}
    >>> a
    
    # 输出结果
    {'r', 'd'}
    ```

### 添加元素

+ 将元素 x 添加到集合 s 中，如果元素已存在，则不进行任何操作。

  + ```python
    >>> thisset = set(("Google", "Runoob", "Taobao"))
    >>> thisset.add("Facebook")
    >>> print(thisset)
    
    # 输出结果
    {'Taobao', 'Facebook', 'Google', 'Runoob'}
    ```

+ 还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式如下：

  + ```python
    # s.update( x )
    >>> thisset = set(("Google", "Runoob", "Taobao"))
    >>> thisset.update({1,3})
    >>> print(thisset)
    # 输出结果
    {1, 3, 'Google', 'Taobao', 'Runoob'}
    
    # x 可以有多个，用逗号分开。
    >>> thisset.update([1,4],[5,6])  
    >>> print(thisset)
    # 输出结果
    {1, 3, 4, 5, 6, 'Google', 'Taobao', 'Runoob'}
    ```

### 移除元素

+ 将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误。

  + ```python
    # s.remove( x )
    >>> thisset = set(("Google", "Runoob", "Taobao"))
    >>> thisset.remove("Taobao")
    >>> print(thisset)
    {'Google', 'Runoob'}
    
    # 如果元素不存在会发生错误
    >>> thisset.remove("Facebook")   
    
    # 输出结果
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    KeyError: 'Facebook'
    ```

+ 此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误。格式如下所示：

  + ```python
    # s.discard(x)
    >>> thisset = set(("Google", "Runoob", "Taobao"))
    >>> thisset.discard("Facebook")  # 不存在不会发生错误
    >>> print(thisset)
    {'Taobao', 'Google', 'Runoob'}
    ```

+ 随机删除集合中的一个元素（set 集合的 pop 方法会对集合进行无序的排列，然后将这个无序排列集合的左面第一个元素进行删除。）

  + ```python
    thisset = set(("Google", "Runoob", "Taobao", "Facebook"))
    x = thisset.pop()  # 随机删除某个元素
    print(x)
    
    # 输出结果（随机的）
    '''
    Runoob
    '''
    ```

### 清空集合

+ 实例：

  + ```python
    # s.clear()
    >>> thisset = set(("Google", "Runoob", "Taobao"))
    >>> thisset.clear()
    >>> print(thisset)
    
    # 输出结果
    set()
    ```

### 判断元素是否在集合中存在

+ 判断元素 x 是否在集合 s 中，存在返回 True，不存在返回 False。

  + ```python
    # x in s
    >>> thisset = set(("Google", "Runoob", "Taobao"))
    >>> "Runoob" in thisset
    True
    >>> "Facebook" in thisset
    False
    ```

### 集合所有内置方法

+ | 方法                                                         | 描述                                                         |
  | :----------------------------------------------------------- | :----------------------------------------------------------- |
  | [add()](https://www.runoob.com/python3/ref-set-add.html)     | 为集合添加元素                                               |
  | [clear()](https://www.runoob.com/python3/ref-set-clear.html) | 移除集合中的所有元素                                         |
  | [copy()](https://www.runoob.com/python3/ref-set-copy.html)   | 拷贝一个集合                                                 |
  | [difference()](https://www.runoob.com/python3/ref-set-difference.html) | 返回多个集合的差集                                           |
  | [difference_update()](https://www.runoob.com/python3/ref-set-difference_update.html) | 移除集合中的元素，该元素在指定的集合也存在。                 |
  | [discard()](https://www.runoob.com/python3/ref-set-discard.html) | 删除集合中指定的元素                                         |
  | [intersection()](https://www.runoob.com/python3/ref-set-intersection.html) | 返回集合的交集                                               |
  | [intersection_update()](https://www.runoob.com/python3/ref-set-intersection_update.html) | 返回集合的交集。                                             |
  | [isdisjoint()](https://www.runoob.com/python3/ref-set-isdisjoint.html) | 判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。 |
  | [issubset()](https://www.runoob.com/python3/ref-set-issubset.html) | 判断指定集合是否为该方法参数集合的子集。                     |
  | [issuperset()](https://www.runoob.com/python3/ref-set-issuperset.html) | 判断该方法的参数集合是否为指定集合的子集                     |
  | [pop()](https://www.runoob.com/python3/ref-set-pop.html)     | 随机移除元素                                                 |
  | [remove()](https://www.runoob.com/python3/ref-set-remove.html) | 移除指定元素                                                 |
  | [symmetric_difference()](https://www.runoob.com/python3/ref-set-symmetric_difference.html) | 返回两个集合中不重复的元素集合。                             |
  | [symmetric_difference_update()](https://www.runoob.com/python3/ref-set-symmetric_difference_update.html) | 移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。 |
  | [union()](https://www.runoob.com/python3/ref-set-union.html) | 返回两个集合的并集                                           |
  | [update()](https://www.runoob.com/python3/ref-set-update.html) | 给集合添加元素                                               |

## ----------------------------------------------

## 算数运算符

+ 注意：不同类型的数混合运算时会将整数转换为浮点数

+ //  取整除 - 向下取接近商的整数

  + ```python
    >>> 9//2
    4
    >>> -9//2
    -5
    
    # result:取小不取大
    ```
    
  + **注意：****//** 得到的并不一定是整数类型的数，它与分母分子的数据类型有关系。
  
  + ```python
    >>> 7//2
    3
    >>> 7.0//2
    3.0
    >>> 7//2.0
    3.0
    >>> 
    ```

## 赋值运算符

+ :=  海象运算符，可在表达式内部为变量赋值。**Python3.8 版本新增运算符**。

  + ```python
    if (n := len(a)) > 10:
        print(f"List is too long ({n} elements, expected <= 10)")
    ```

## 数制相互转换

+ 数制对照表
  
+ ​	![image-20210102134336942](C:\Users\87143\AppData\Roaming\Typora\typora-user-images\image-20210102134336942.png)
  
+ 十进制转换成其它进制

  + ```python
    # 十进制=>二进制
    >>>bin(10)
    '0b1010'
    
    # 十进制=>八进制
    >>>oct(10)
    '0o12'
    
    # 十进制=>十六进制
    >>>hex(10)
    '0xa'
    ```

+ 其它进制转换成10进制

  + ```python
    # 二进制=>十进制
    >>>int('1010',2)  #或 int('0b1010',2)
    '10'
    
    # 八进制=>十进制
    >>>int('12',8)  #或 int('0o12',8)
    '10'
    
    # 16进制=>十进制
    >>>int('a',16)  #或 int('0xa',16)
    '10'
    ```

## 位运算符

+ 示例

  + | 运算符 | 描述                                                         | 实例                                                         |
    | :----- | :----------------------------------------------------------- | :----------------------------------------------------------- |
    | &      | 按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0 | (a & b) 输出结果 12 ，二进制解释： 0000 1100                 |
    | \|     | 按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。 | (a \| b) 输出结果 61 ，二进制解释： 0011 1101                |
    | ^      | 按位异或运算符：当两对应的二进位相异时，结果为1              | (a ^ b) 输出结果 49 ，二进制解释： 0011 0001                 |
    | ~      | 按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。**~x** 类似于 **-x-1** | (~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。 |
    | <<     | 左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。 | a << 2 输出结果 240 ，二进制解释： 1111 0000                 |
    | >>     | 右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数 | a >> 2 输出结果 15 ，二进制解释： 0000 1111                  |

  + ```python
    #!/usr/bin/python3
     
    a = 60            # 60 = 0011 1100 
    b = 13            # 13 = 0000 1101 
    c = 0
     
    c = a & b        # 12 = 0000 1100
    print ("1 - c 的值为：", c)
     
    c = a | b        # 61 = 0011 1101 
    print ("2 - c 的值为：", c)
     
    c = a ^ b        # 49 = 0011 0001
    print ("3 - c 的值为：", c)
     
    c = ~a           # -61 = 1100 0011
    print ("4 - c 的值为：", c)
     
    c = a << 2       # 240 = 1111 0000
    print ("5 - c 的值为：", c)
     
    c = a >> 2       # 15 = 0000 1111
    print ("6 - c 的值为：", c)
    
    # result
    '''
    1 - c 的值为： 12
    2 - c 的值为： 61
    3 - c 的值为： 49
    4 - c 的值为： -61
    5 - c 的值为： 240
    6 - c 的值为： 15
    '''
    ```

## 成员运算符

+ | 运算符 | 描述                                                    | 实例                                              |
  | :----- | :------------------------------------------------------ | :------------------------------------------------ |
  | in     | 如果在指定的序列中找到值返回 True，否则返回 False。     | x 在 y 序列中 , 如果 x 在 y 序列中返回 True。     |
  | not in | 如果在指定的序列中没有找到值返回 True，否则返回 False。 | x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。 |

+ 示例

  + ```python
    #!/usr/bin/python3
     
    a = 10
    b = 20
    list = [1, 2, 3, 4, 5 ]
     
    if ( a in list ):
       print ("1 - 变量 a 在给定的列表中 list 中")
    else:
       print ("1 - 变量 a 不在给定的列表中 list 中")
     
    if ( b not in list ):
       print ("2 - 变量 b 不在给定的列表中 list 中")
    else:
       print ("2 - 变量 b 在给定的列表中 list 中")
     
    # 修改变量 a 的值
    a = 2
    if ( a in list ):
       print ("3 - 变量 a 在给定的列表中 list 中")
    else:
       print ("3 - 变量 a 不在给定的列表中 list 中")
    
    #result
    '''
    1 - 变量 a 不在给定的列表中 list 中
    2 - 变量 b 不在给定的列表中 list 中
    3 - 变量 a 在给定的列表中 list 中
    '''
    ```

## 身份运算符

+ 身份运算符用于比较两个对象的存储单元

  + 

  | 运算符 | 描述                                        | 实例                                                         |
  | :----- | :------------------------------------------ | :----------------------------------------------------------- |
  | is     | is 是判断两个标识符是不是引用自一个对象     | **x is y**, 类似 **id(x) == id(y)** , 如果引用的是同一个对象则返回 True，否则返回 False |
  | is not | is not 是判断两个标识符是不是引用自不同对象 | **x is not y** ， 类似 **id(a) != id(b)**。如果引用的不是同一个对象则返回结果 True，否则返回 False。 |

- 示例

  - ```python
    #!/usr/bin/python3
     
    a = 20
    b = 20
     
    if ( a is b ):
       print ("1 - a 和 b 有相同的标识")
    else:
       print ("1 - a 和 b 没有相同的标识")
     
    if ( id(a) == id(b) ):
       print ("2 - a 和 b 有相同的标识")
    else:
       print ("2 - a 和 b 没有相同的标识")
     
    # 修改变量 b 的值
    b = 30
    if ( a is b ):
       print ("3 - a 和 b 有相同的标识")
    else:
       print ("3 - a 和 b 没有相同的标识")
     
    if ( a is not b ):
       print ("4 - a 和 b 没有相同的标识")
    else:
       print ("4 - a 和 b 有相同的标识")
    
    
    '''
    result:
    1 - a 和 b 有相同的标识
    2 - a 和 b 有相同的标识
    3 - a 和 b 没有相同的标识
    4 - a 和 b 没有相同的标识
    '''
    ```

+ 补充：

  + is 与 == 区别：

    is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。

  + ```python
    >>>a = [1, 2, 3]
    >>> b = a
    >>> b is a 
    True
    >>> b == a
    True
    >>> b = a[:]
    >>> b is a
    False
    >>> b == a
    True
    ```

## 运算符优先级

+ 以下表格列出了从最高到最低优先级的所有运算符：

  + | 运算符                   | 描述                                                   |
    | :----------------------- | :----------------------------------------------------- |
    | **                       | 指数 (最高优先级)                                      |
    | ~ + -                    | 按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@) |
    | * / % //                 | 乘，除，求余数和取整除                                 |
    | + -                      | 加法减法                                               |
    | >> <<                    | 右移，左移运算符                                       |
    | &                        | 位 'AND'                                               |
    | ^ \|                     | 位运算符                                               |
    | <= < > >=                | 比较运算符                                             |
    | == !=                    | 等于运算符                                             |
    | = %= /= //= -= += *= **= | 赋值运算符                                             |
    | is is not                | 身份运算符                                             |
    | in not in                | 成员运算符                                             |
    | not and or               | 逻辑运算符                                             |

+ 示例

  + ```python
    #!/usr/bin/python3
     
    a = 20
    b = 10
    c = 15
    d = 5
    e = 0
     
    e = (a + b) * c / d       #( 30 * 15 ) / 5
    print ("(a + b) * c / d 运算结果为：",  e)
     
    e = ((a + b) * c) / d     # (30 * 15 ) / 5
    print ("((a + b) * c) / d 运算结果为：",  e)
     
    e = (a + b) * (c / d)    # (30) * (15/5)
    print ("(a + b) * (c / d) 运算结果为：",  e)
     
    e = a + (b * c) / d      #  20 + (150/5)
    print ("a + (b * c) / d 运算结果为：",  e)
    
    
    '''
    result:
    (a + b) * c / d 运算结果为： 90.0
    ((a + b) * c) / d 运算结果为： 90.0
    (a + b) * (c / d) 运算结果为： 90.0
    a + (b * c) / d 运算结果为： 50.0
    '''
    ```

+ and 拥有更高优先级

  + ```python
    x = True
    y = False
    z = False
     
    if x or y and z:
        print("yes")
    else:
        print("no")
        
        
    '''
    result:
    yes
    '''
    ```

## ----------------------------------------------

## 1. 编程第一步

### 1.1 斐波那契数列

+ ```python
  #!/usr/bin/python3
   
  # Fibonacci series: 斐波纳契数列
  # 两个元素的总和确定了下一个数
  a, b = 1, 1
  count = 0
  # 输出前六个斐波那契数
  while b < 6:
      print(a, end=',')
      a, b = b, a+b
      count += 1
  
  # 执行结果: 1,1,2,3,5,8,
  
  '''
  其中代码 a, b = b, a+b 的计算方式为先计算右边表达式，然后同时赋值给左边，等价于：
  m = b
  n = a + b 
  a = m
  b = n
  '''
  ```

## 2. 条件控制

### 2.1 *注意

1. 每个条件后面要使用冒号 **:**，表示接下来是满足条件后要执行的语句块。
2. 使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块。
3. 在Python中没有switch – case语句。

### 2.2 if 中常用的操作运算符

+ | 操作符 | 描述                     |
  | :----- | :----------------------- |
  | `<`    | 小于                     |
  | `<=`   | 小于或等于               |
  | `>`    | 大于                     |
  | `>=`   | 大于或等于               |
  | `==`   | 等于，比较两个值是否相等 |
  | `!=`   | 不等于                   |

### 实例1：狗的年龄计算判断

+ ```python
  #!/usr/bin/python3
   
  age = int(input("请输入你家狗狗的年龄: "))
  print("")
  if age <= 0:
      print("你是在逗我吧!")
  elif age == 1:
      print("相当于 14 岁的人。")
  elif age == 2:
      print("相当于 22 岁的人。")
  elif age > 2:
      human = 22 + (age -2)*5
      print("对应人类年龄: ", human)
   
  ### 退出提示
  input("点击 enter 键退出")
  
  # output result:
  '''
  请输入你家狗狗的年龄: 1
  
  相当于 14 岁的人。
  点击 enter 键退出
  '''
  ```

### 实例2：数字猜谜小游戏

+ ```python
  answer = 7
  print('***数字猜谜小游戏***')
  while True:
      guess = int(input('请输入猜测的数字:'))
      if guess > answer:
          print('猜大了...\n')
      elif guess < answer:
          print('猜小了...\n')
      else:
          print('猜对了！')
          break
  
  # output result
  '''
  ***数字猜谜小游戏***
  ***数字猜谜小游戏***
  请输入猜测的数字:5
  猜小了...
  
  请输入猜测的数字:9
  猜大了...
  
  请输入猜测的数字:7
  猜对了！
  '''      
  ```

### 实例3：if 嵌套

+ ```python
  # !/usr/bin/python3
   
  num=int(input("输入一个数字："))
  if num%2==0:
      if num%3==0:
          print ("你输入的数字可以整除 2 和 3")
      else:
          print ("你输入的数字可以整除 2，但不能整除 3")
  else:
      if num%3==0:
          print ("你输入的数字可以整除 3，但不能整除 2")
      else:
          print  ("你输入的数字不能整除 2 和 3")
          
  # output result:
  '''
  输入一个数字：6
  你输入的数字可以整除 2 和 3
  '''
  ```

## 3. 循环语句

### 3.1 while 循环

#### *注意

+ 需要注意冒号和缩进。另外，在 Python 中没有 do..while 循环。

#### 实例1：使用了 while 来计算 1 到 100 的总和

+ ```python
  #!/usr/bin/env python3
   
  n = 100
   
  sum = 0
  counter = 1
  while counter <= n:
      sum = sum + counter
      counter += 1
   
  print("1 到 %d 之和为: %d" % (n,sum))
  
  # output
  '''
  1 到 100 之和为: 5050
  '''
  ```

#### 实例2：while无限循环

+ ```python
  #!/usr/bin/python3
   
  var = 1
  while var == 1 :  # 表达式永远为 true
     num = int(input("输入一个数字  :"))
     print ("你输入的数字是: ", num)
   
  print ("Good bye!")
  
  # output
  '''
  输入一个数字  :5
  你输入的数字是:  5
  输入一个数字  :
  '''
  
  
  ```

+ tip1: 你可以使用 **CTRL+C** 来退出当前的无限循环。

+ tip2: 无限循环在服务器上客户端的实时请求非常有用。

#### 实例3：while 循环使用 else 语句

+ 在 while … else 在条件语句为 false 时执行 else 的语句块。

+ ```python
  #!/usr/bin/python3
   
  count = 0
  while count < 5:
     print (count, " 小于 5")
     count = count + 1
  else:
     print (count, " 大于或等于 5")
  
  # output
  '''
  0  小于 5
  1  小于 5
  2  小于 5
  3  小于 5
  4  小于 5
  5  大于或等于 5
  '''
  ```

#### 实例4：简单语句组

+ 类似if语句的语法，如果你的while循环体中**只有一条**语句，你可以将该语句与while写在同一行中， 如下所示：

+ ```python
  #!/usr/bin/python
   
  flag = 1
  
  while (flag): print ('欢迎访问菜鸟教程!')
   
  print ("Good bye!")
  
  # 注意：以上的无限循环你可以使用 CTRL+C 来中断循环。
  # output
  '''
  欢迎访问菜鸟教程!
  欢迎访问菜鸟教程!
  欢迎访问菜鸟教程!
  欢迎访问菜鸟教程!
  欢迎访问菜鸟教程!
  '''
  ```

### 3.2 for 循环

#### *注意

+ Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。

#### 实例1：break 跳出for 循环

+ ```python
  #!/usr/bin/python3
   
  sites = ["Baidu", "Google","Runoob","Taobao"]
  for site in sites:
      if site == "Runoob":
          print("菜鸟教程!")
          break
      print("循环数据 " + site)
  else:
      print("没有循环数据!")
  print("完成循环!")
  
  # output
  '''
  循环数据 Baidu
  循环数据 Google
  菜鸟教程!
  完成循环!
  '''
  ```

#### 实例2：range() 函数设置步长（步长可以为负数）

+ ```python
  for i in range(0, 10, 3) :
      print(i, end=' ')
  
  # output
  '''
  0 3 6 9
  '''
  
  for i in range(-2, -11, -2):
      print(i, end=' ')
      
  # output
  '''
  -2 -4 -6 -8 -10 
  '''
  ```

####  实例3：结合range()和len()函数以遍历一个序列的索引

+ ```python
  a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
  for i in range(len(a)):
  	print(i, a[i])
      
  # output
  '''
  0 Google
  1 Baidu
  2 Runoob
  3 Taobao
  4 QQ
  '''
  ```

#### 实例4：使用range() 函数创建一个列表

+ ```python
  >>>list[range(5)]
  [0, 1, 2, 3, 4]
  ```

### 3.3 break 和 continue 语句及循环中的 else 子句

#### *注意

+ **break** 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。
+ **continue** 语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。

#### 实例1：循环语句中使用break

+ ```python
  #!/usr/bin/python3
   
  for letter in 'Runoob':     # 第一个实例
     if letter == 'b':
        break
     print ('当前字母为 :', letter)
    
  var = 10                    # 第二个实例
  while var > 0:              
     print ('当期变量值为 :', var)
     var = var -1
     if var == 5:
        break
   
  print ("Good bye!")
  
  ```

#### 实例2：循环语句中使用continue

+ ```python
  #!/usr/bin/python3
   
  for letter in 'Runoob':     # 第一个实例
     if letter == 'o':        # 字母为 o 时跳过输出
        continue
     print ('当前字母 :', letter)
   
  var = 10                    # 第二个实例
  while var > 0:              
     var = var -1
     if var == 5:             # 变量为 5 时跳过输出
        continue
     print ('当前变量值 :', var)
  print ("Good bye!")
  ```

#### 实例3：循环语句中使用else字句（适用场景：要全部遍历完才能得出结论的）

+ 循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行，但循环被 break 终止时不执行。

+ ```python
  #!/usr/bin/python3
   
  for n in range(2, 10):
      for x in range(2, n):
          if n % x == 0:
              print(n, '等于', x, '*', n//x)
              break
      else:
          # 循环中没有找到元素
          print(n, ' 是质数')
          
  # output
  '''
  2  是质数
  3  是质数
  4 等于 2 * 2
  5  是质数
  6 等于 2 * 3
  7  是质数
  8 等于 2 * 4
  9 等于 3 * 3
  '''
  ```

### 3.4 pass 语句

#### *注意

+ Python的pass是空语句，是为了保持程序结构的完整性。
+ pass 不做任何事情，一般用做占位语句

#### 实例1：常用场景

```python
>>>while True:
...     pass  # 等待键盘中断 (Ctrl+C)
```

#### 实例2：最小的类

```python
>>>class MyEmptyClass:
...     pass
```

#### 实例3：在字母为 o 时 执行 pass 语句块

```python
#!/usr/bin/python3
 
for letter in 'Runoob': 
   if letter == 'o':
      pass
      print ('执行 pass 块')
   print ('当前字母 :', letter)
 
print ("Good bye!")

# output
'''
当前字母 : R
当前字母 : u
当前字母 : n
执行 pass 块
当前字母 : o
执行 pass 块
当前字母 : o
当前字母 : b
Good bye!
'''
```

## 4. 迭代器与生成器

### 4.1 迭代器

#### *注意

+ 迭代是Python最强大的功能之一，是访问集合元素的一种方式。
+ 迭代器是一个可以记住遍历的位置的对象。
+ 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
+ 迭代器有两个基本的方法：**iter()** 和 **next()**。

#### 实例1：字符串，列表或元组对象都可用于创建迭代器。

+ ```python
  >>> list=[1,2,3,4]
  >>> it = iter(list)    # 创建迭代器对象
  >>> print (next(it))   # 输出迭代器的下一个元素
  1
  >>> print (next(it))
  2
  >>>
  ```

#### 实例2：迭代器对象可以使用常规for语句进行遍历。

+ ```python
  #!/usr/bin/python3
   
  list1=[1,2,3,4]
  iter1 = iter(list1)    # 创建迭代器对象
  # 迭代器只能用for循环整体遍历一次
  for i in iter1:
      print (i, end=" ")
      
  # output
  '''
  1 2 3 4
  '''
      
  # tip1: 直接遍历列表可以用for循环多次遍历全部元素；
  # tip2：遍历iter迭代器，只能用for循环遍历全部元素一次。
  '''
  # once
  for i in list1:
      print(i)
  # twice
  for i in list1:
      print(i)
  # more
  '''
  ```

#### 实例3：使用next()函数遍历整个迭代器

+ ```python
  #!/usr/bin/python3
  
  import sys         # 引入 sys 模块
  
  list1 = [1,2,3,4]
      iter1 = iter(list1)
      while True:
          try:
              print(next(iter1), end=' ')
          except StopIteration:
              print('\n迭代器所有元素遍历完成！')
              sys.exit()
  # output
  '''
  1 2 3 4 
  迭代器所有元素遍历完成！
  '''
  ```

### 4.2 创建一个迭代器

#### *注意

+ 把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
+ __iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。
+ __next__() 方法（Python 2 里是 next()）会返回下一个迭代器对象。

#### 实例1：创建一个返回数字的迭代器，初始值为 1，逐步递增 1

+ ```python
  class MyNumbers:
      def __iter__(self):
          self.a = 1
          return self
  
      def __next__(self):
          x = self.a
          self.a += 1
          return x
  
  
  if __name__ == "__main__":
      my_number = MyNumbers()
      my_iter = iter(my_number)
  
      print(next(my_iter), end=' ')
      print(next(my_iter), end=' ')
      print(next(my_iter), end=' ')
      print(next(my_iter), end=' ')
      print(next(my_iter), end=' ')
      
  # output
  '''
  1 2 3 4 5 
  '''
  ```

#### 实例2：利用StopIteration异常实现在10次迭代后停止执行

+ StopIteration 异常用于标识迭代的完成，防止出现无限循环的情况，在 __next__() 方法中我们可以设置在完成指定循环次数后触发 StopIteration 异常来结束迭代。

+ ```python
  class MyNumbers:
      def __iter__(self):
          self.a = 1
          return self
  
      def __next__(self):
          x = self.a
          if x <= 10:
              self.a += 1
              return x
          else:
              raise StopIteration
  
  
  if __name__ == "__main__":
      my_number = MyNumbers()
      my_iter = iter(my_number)
  
      for i in my_iter:
          print(i, end=' ')
          
  # output
  '''
  1 2 3 4 5 6 7 8 9 10 
  '''
  ```

### 4.3 生成器

#### *注意

+ 在 Python 中，使用了 yield 的函数被称为生成器（generator）。
+ 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
+ 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
+ 调用一个生成器函数，返回的是一个迭代器对象。

#### 实例1：使用 yield 实现斐波那契数列

+ ```python
  import sys
  
  def feibonacci(count):
      a, b = 1, 1
      while count >= 1:
          yield a
          a, b = b, a+b
          count -= 1
  
  
  if __name__ == "__main__":
      f = feibonacci(10)
      while True:
          try:
              print(next(f), end=' ')
          except StopIteration:
              sys.exit()
              
  # output
  '''
  0 1 1 2 3 5 8 13 21 34 55
  '''
  ```

## 5. 函数

### 5.1 什么是函数

+ 函数是组织好的，可重复使用的，用来实现单一，或相关联功能的代码段。

### 5.2 函数的作用

+ 函数能提高应用的模块性，和代码的重复利用率。你已经知道Python提供了许多内建函数，比如print()。但你也可以自己创建函数，这被叫做用户自定义函数。

### 5.3 定义一个函数

+ 函数代码块以 **def** 关键词开头，后接函数标识符名称和圆括号 **()**。
+ 任何传入参数和自变量必须放在圆括号中间，圆括号之间可以用于定义参数。
+ 函数的第一行语句可以选择性地使用文档字符串—用于存放函数说明。
+ 函数内容以冒号 **:** 起始，并且缩进。
+ **return [表达式]** 结束函数，选择性地返回一个值给调用方，不带表达式的 return 相当于返回 None。

#### 实例1：计算面积

+ ```python
  #!/usr/bin/python3
   
  # 计算面积函数
  def area(width, height):
      return width * height
   
  def print_welcome(name):
      print("Welcome", name)
   
  print_welcome("Runoob")
  w = 4
  h = 5
  print("width =", w, " height =", h, " area =", area(w, h))
  
  # output
  '''
  Welcome Runoob
  width = 4  height = 5  area = 20
  '''
  ```

### 5.4 函数调用

#### 调用方式

+ 这个函数的基本结构完成以后，你可以通过另一个函数调用执行，也可以直接从 Python 命令提示符执行。

#### 实例1：调用print_me()函数

+ ```python
  #!/usr/bin/python3
   
  # 定义函数
  def print_me( str ):
     # 打印任何传入的字符串
     print (str)
     return
   
  # 调用函数
  print_me("我要调用用户自定义函数!")
  print_me("再次调用同一函数")
  
  
  # output
  '''
  我要调用用户自定义函数!
  再次调用同一函数
  '''
  ```

### 5.3 参数传递

#### 实参和形参

+ 实参：是在函数外面定义好的，然后传入函数名后的括号里。
+ 形参：函数（的语句块）执行过程中使用的参数（变量）

#### **注意

+ 在 python 中，类型属于对象，变量是没有类型的

+ ```python
  a=[1,2,3]
  a="Runoob"
  
  '''
  以上代码中，[1,2,3] 是 List 类型，"Runoob" 是 String 类型，而变量 a 是没有类型，她仅仅是一个对象的引用（一个指针），可以是指向 List 类型对象，也可以是指向 String 类型对象。
  '''
  ```

#### 可更改(mutable)与不可更改(immutable)对象

+ 在 python 中，strings, tuples, 和 numbers 是不可更改的对象，而 list,dict 等则是可以修改的对象。

##### *变量更改赋值原理说明

+ **不可变类型：**变量赋值 **a=5** 后再赋值 **a=10**，这里实际是新生成一个 int 值对象 10，再让 a 指向它，而 5 被丢弃，不是改变 a 的值，相当于新生成了 a。
+ **可变类型：**变量赋值 **la=[1,2,3,4]** 后再赋值 **la[2]=5** 则是将 list la 的第三个元素值更改，本身la没有动，只是其内部的一部分值被修改了。

##### python 函数的参数传递

+ **不可变类型：**类似 C++ 的值传递，如 整数、字符串、元组。如 fun(a)，传递的只是 a 的值，没有影响 a 对象本身。如果在 fun(a)）内部修改 a 的值，则是新生成来一个 a。‘
+ **可变类型：**类似 C++ 的引用传递，如 列表，字典。如 fun(la)，则是将 la 真正的传过去，修改后 fun 外部的 la 也会受影响

##### * 强调

+ python 中一切都是对象，严格意义我们不能说值传递还是引用传递，我们应该说传不可变对象和传可变对象。

#### 实例1：传不可变对象

+ 通过 **id()** 函数来查看内存地址变化

+ ```python
  def change(a):
      print(id(a))   # 指向的是同一个对象
      a=10
      print(id(a))   # 一个新对象
   
  a=1
  change(a)
  print(id(a))
  
  # output
  '''
  4379369136 (外部的id)
  4379369136 (内部接收到的id)
  4379369424 (内部修改后的id)
  '''
  ```

+ 可以看见在调用函数前后，形参和实参指向的是同一个对象（对象 id 相同），在函数内部修改形参后，形参指向的是不同的 id。

#### 实例2：传可变对象

+ 可变对象在函数里修改了参数，那么在调用这个函数的函数里，原始的参数也被改变了。

+ ```python
  #!/usr/bin/python3
   
  # 可写函数说明
  def changeme( mylist ):
     "修改传入的列表"
     mylist.append([1,2,3,4])
     print ("函数内取值: ", mylist)
     return
   
  # 调用changeme函数
  mylist = [10,20,30]
  changeme( mylist )
  print ("函数外取值: ", mylist)
  
  # output
  '''
  函数内取值:  [10, 20, 30, [1, 2, 3, 4]]
  函数外取值:  [10, 20, 30, [1, 2, 3, 4]]
  '''
  ```

### 5.4 参数

#### 可使用的参数类型

+ 必需参数
+ 关键字参数
+ 默认参数
+ 不定长参数

#### 必选参数

##### 说明

+ 必需参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。

##### 实例1：调用 printme() 函数，你必须传入一个参数，不然会出现语法错误

```python
#!/usr/bin/python3
 
#可写函数说明
def printme( str ):
   "打印任何传入的字符串"
   print (str)
   return
 
# 调用 printme 函数，不加参数会报错
printme()

# output
'''
Traceback (most recent call last):
  File "test.py", line 10, in <module>
    printme()
TypeError: printme() missing 1 required positional argument: 'str'
'''
```

#### 关键字参数

##### 说明

+ 关键字参数和函数调用关系紧密，函数调用使用关键字参数来确定传入的参数值。
+ 使用关键字参数允许函数调用时参数的顺序与声明时不一致，因为 Python 解释器能够用参数名匹配参数值。

##### 实例1：在函数 printme() 调用时使用参数名

+ ```python
  #!/usr/bin/python3
   
  #可写函数说明
  def printme( str ):
     "打印任何传入的字符串"
     print (str)
     return
   
  #调用printme函数
  printme( str = "菜鸟教程")
  
  # output
  '''
  菜鸟教程
  '''
  ```

##### 实例2：函数参数的使用不需要使用指定顺序

+ ```python
  #!/usr/bin/python3
   
  #可写函数说明
  def printinfo( name, age ):
     "打印任何传入的字符串"
     print ("名字: ", name)
     print ("年龄: ", age)
     return
   
  #调用printinfo函数
  printinfo( age=50, name="runoob" )
  
  # output
  '''
  名字:  runoob
  年龄:  50
  '''
  ```

#### 默认参数

##### 说明

+ 调用函数时，如果没有传递参数，则会使用默认参数。

##### 实例1：如果没有传入 age 参数，则使用默认值。

+ ```python
  #!/usr/bin/python3
   
  #可写函数说明
  def printinfo( name, age = 35 ):
     "打印任何传入的字符串"
     print ("名字: ", name)
     print ("年龄: ", age)
     return
   
  #调用printinfo函数
  printinfo( age=50, name="runoob" )
  print ("------------------------")
  printinfo( name="runoob" )
  
  # output
  '''
  名字:  runoob
  年龄:  50
  ------------------------
  名字:  runoob
  年龄:  35
  '''
  ```

#### 不定长参数

##### 说明

+ 你可能需要一个函数能处理比当初声明时更多的参数。这些参数叫做不定长参数，和上述 2 种参数不同，声明时不会命名。

##### 带*参数的基本语法

+ ```python
  def functionname([formal_args,] *var_args_tuple ):
     "函数_文档字符串"
     function_suite
     return [expression]
  ```

##### 实例1：加了星号 ***** 的参数会以元组(tuple)的形式导入，存放所有未命名的变量参数。

+ ```python
  #!/usr/bin/python3
    
  # 可写函数说明
  def printinfo( arg1, *vartuple ):
     "打印任何传入的参数"
     print ("输出: ")
     print (arg1)
     print (vartuple)
   
  # 调用printinfo 函数
  printinfo( 70, 60, 50 )
  
  # output
  '''
  输出: 
  70
  (60, 50)
  '''
  ```

##### 实例2：在函数调用时没有指定*参数，它就是一个空元组。

+ ```python
  #!/usr/bin/python3
   
  # 可写函数说明
  def printinfo( arg1, *vartuple ):
     "打印任何传入的参数"
     print ("输出: ")
     print (arg1)
     print (vartuple)
     return
   
  # 调用printinfo 函数
  printinfo( 10 )
  printinfo( 70, 60, 50 )
  
  # output
  '''
  输出: 
  10
  ()
  输出: 
  70
  (60, 50)
  '''
  ```

##### 带**参数基本语法

+ ```python
  def functionname([formal_args,] **var_args_dict ):
     "函数_文档字符串"
     function_suite
     return [expression]
  ```

##### 实例3：加了两个星号 ***\*** 的参数会以字典的形式导入

+ ```python
  #!/usr/bin/python3
    
  # 可写函数说明
  def printinfo( arg1, **vardict ):
     "打印任何传入的参数"
     print ("输出: ")
     print (arg1)
     print (vardict)
   
  # 调用printinfo 函数
  printinfo(1, a=2,b=3)
  
  
  # output
  '''
  输出: 
  1
  {'a': 2, 'b': 3}
  '''
  ```

##### 实例4：单独出现星号 ***** 后的参数必须用关键字传入。

+ ```python
  >>> def f(a,b,*,c):
  ...     return a+b+c
  ... 
  >>> f(1,2,3)   # 报错
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: f() takes 2 positional arguments but 3 were given
  >>> f(1,2,c=3) # 正常
  6
  >>>
  ```

### 5.3 匿名函数 lambda

#### 说明

+ python 使用 lambda 来创建匿名函数。

#### 匿名的含义

+ 所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。
  + lambda 只是一个表达式，函数体比 def 简单很多。
  + lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
  + lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
  + 虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。

#### 语法

+ lambda 函数的语法只包含一个语句，如下：

+ ```python
  lambda [arg1 [,arg2,.....argn]]:expression
  ```

#### 实例：lambda的使用

+ ```python
  #!/usr/bin/python3
   
  # 可写函数说明
  sum = lambda arg1, arg2: arg1 + arg2
   
  # 调用sum函数
  print ("相加后的值为 : ", sum( 10, 20 ))
  print ("相加后的值为 : ", sum( 20, 20 ))
  
  # output
  '''
  相加后的值为 :  30
  相加后的值为 :  40
  '''
  ```

### 5.4 return 语句

#### return 的作用

+ **return [表达式]** 语句用于退出函数，选择性地向调用方返回一个表达式。
+ 不带参数值的return语句返回None。

#### 实例：return 语句的用法

+ ```python
  #!/usr/bin/python3
   
  # 可写函数说明
  def sum( arg1, arg2 ):
     # 返回2个参数的和."
     total = arg1 + arg2
     print ("函数内 : ", total)
     return total
   
  # 调用sum函数
  total = sum( 10, 20 )
  print ("函数外 : ", total)
  
  
  # output
  '''
  函数内 :  30
  函数外 :  30
  '''
  ```

### 5.5 强制位置参数（Python3.8）

#### 说明

+ Python3.8 新增了一个函数形参语法 / 用来指明函数形参必须使用指定位置参数，不能使用关键字参数的形式。

#### 实例：形参 a 和 b 必须使用指定位置参数，c 或 d 可以是位置形参或关键字形参，而 e 或 f 要求为关键字形参

+ ```python
  def f(a, b, /, c, d, *, e, f):
      print(a, b, c, d, e, f)
      
  # 正确的使用方法
  f(10, 20, 30, d=40, e=50, f=60)
  
  # 错误的使用方法
  '''
  f(10, b=20, c=30, d=40, e=50, f=60)   # b 不能使用关键字参数的形式
  f(10, 20, 30, 40, 50, f=60)           # e 必须使用关键字参数的形式
  '''
  
  ```

## 6. 数据结构

### 6.1 列表

+ 列表可以修改，而字符串和元组不能

#### 列表拥有的方法

+ | 方法              | 描述                                                         |
  | :---------------- | :----------------------------------------------------------- |
  | list.append(x)    | 把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。        |
  | list.extend(L)    | 通过添加指定列表的所有元素来扩充列表，相当于 a[len(a):] = L。 |
  | list.insert(i, x) | 在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。 |
  | list.remove(x)    | 删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。 |
  | list.pop([i])     | 从列表的指定位置移除元素，并将其返回。如果没有指定索引，a.pop()返回最后一个元素。元素随即从列表中被移除。（方法中 i 两边的方括号表示这个参数是可选的，而不是要求你输入一对方括号，你会经常在 Python 库参考手册中遇到这样的标记。） |
  | list.clear()      | 移除列表中的所有项，等于del a[:]。                           |
  | list.index(x)     | 返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。 |
  | list.count(x)     | 返回 x 在列表中出现的次数。                                  |
  | list.sort()       | 对列表中的元素进行排序。                                     |
  | list.reverse()    | 倒排列表中的元素。                                           |
  | list.copy()       | 返回列表的浅复制，等于a[:]。                                 |

##### 实例：演示列表的大部分方法

+ ```python
  >>> a = [66.25, 333, 333, 1, 1234.5]
  >>> print(a.count(333), a.count(66.25), a.count('x'))
  2 1 0
  >>> a.insert(2, -1)
  >>> a.append(333)
  >>> a
  [66.25, 333, -1, 333, 1, 1234.5, 333]
  >>> a.index(333)
  1
  >>> a.remove(333)
  >>> a
  [66.25, -1, 333, 1, 1234.5, 333]
  >>> a.reverse()
  >>> a
  [333, 1234.5, 1, 333, -1, 66.25]
  >>> a.sort()
  >>> a
  [-1, 1, 66.25, 333, 333, 1234.5]
  ```

+ 注意：类似 insert, remove 或 sort 等修改列表的方法没有返回值。

#### 将列表当作堆栈使用

+ 列表方法使得列表可以很方便的作为一个堆栈来使用，堆栈作为特定的数据结构，最先进入的元素最后一个被释放（**堆栈就像正放的杯子，先进去的后出去，后进先出**）。

##### 实例：用 append() 方法可以把一个元素添加到堆栈顶。用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来。

+ ```python
  >>> stack = [3, 4, 5]
  >>> stack.append(6)
  >>> stack.append(7)
  >>> stack
  [3, 4, 5, 6, 7]
  >>> stack.pop()
  7
  >>> stack
  [3, 4, 5, 6]
  >>> stack.pop()
  6
  >>> stack.pop()
  5
  >>> stack
  [3, 4]
  ```

#### 将列表当作队列使用

+ 可以把列表当做队列用，只是在队列里第一加入的元素，第一个取出来
+ **把列表当做队列用效率不高**。在列表的最后添加或者弹出元素速度快，然而在列表里插入或者从头部弹出速度却不快（因为所有其他的元素都得一个个地向后、移动）。

##### 实例：将列表当作队列使用

+ ```python
  >>> from collections import deque
  >>> queue = deque(["Eric", "John", "Michael"])
  >>> queue.append("Terry")           # Terry arrives
  >>> queue.append("Graham")          # Graham arrives
  >>> queue.popleft()                 # The first to arrive now leaves
  'Eric'
  >>> queue.popleft()                 # The second to arrive now leaves
  'John'
  >>> queue                           # Remaining queue in order of arrival
  deque(['Michael', 'Terry', 'Graham'])
  ```

#### 列表推导式

+ 简单来说就是根据列表现有的元素（通过+ - * /）产生一个新的列表或者元组
+ 列表推导式提供了从序列创建列表的简单途径。通常应用程序将一些操作应用于某个序列的每个元素，用其获得的结果作为生成新列表的元素，或者根据确定的判定条件创建子序列。
+ 每个列表推导式都在 for 之后跟一个表达式，然后有零到多个 for 或 if 子句。返回结果是一个根据表达从其后的 for 和 if 上下文环境中生成出来的列表。如果希望表达式推导出一个元组，就必须使用括号。

##### 实例1：将列表中每个数值乘三，获得一个新的列表

+ ```python
  >>> vec = [2, 4, 6]
  >>> [3*x for x in vec]
  [6, 12, 18]
  ```

##### 实例2：将列表中每个数值平方，获得一个新的列表

+ ```python
  >>> vec = [2, 4, 6]
  >>> [[x, x**2] for x in vec]
  [[2, 4], [4, 16], [6, 36]]
  ```

##### 实例3：对序列里的每一个元素逐个调用某方法

+ ```python
  >>> freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
  >>> [weapon.strip() for weapon in freshfruit]  # strip()方法：去除空格
  ['banana', 'loganberry', 'passion fruit']
  ```

##### 实例4：用if字句作为过滤器

+ ```python
  >>> vec = [2, 4, 6]
  >>> [3*x for x in vec if x > 3]
  [12, 18]
  >>> [3*x for x in vec if x < 2]
  []
  ```

##### 实例5：关于循环和其它技巧的演示。

+ ```python
  >>> vec1 = [2, 4, 6]
  >>> vec2 = [4, 3, -9]
  >>> [x*y for x in vec1 for y in vec2]
  [8, 6, -18, 16, 12, -36, 24, 18, -54]
  >>> [x+y for x in vec1 for y in vec2]
  [6, 5, -7, 8, 7, -5, 10, 9, -3]
  >>> [vec1[i]*vec2[i] for i in range(len(vec1))]
  [8, 12, -54]
  ```

##### 实例6：列表推导式可以使用复杂表达式或嵌套函数

+ ```python
  >>> [str(round(355/113, i)) for i in range(1, 6)]
  ['3.1', '3.14', '3.142', '3.1416', '3.14159']
  ```

#### 嵌套列表解析

+ Python的列表还可以嵌套。

##### 实例1：将3X4的矩阵列表转换为4X3列表

+ ```python
  >>> matrix = [
  ...     [1, 2, 3, 4],
  ...     [5, 6, 7, 8],
  ...     [9, 10, 11, 12],
  ... ]
  
  # 方法一：
  >>> [[row[i] for row in matrix] for i in range(4)]
  [
      [1, 5, 9], 
      [2, 6, 10], 
      [3, 7, 11], 
      [4, 8, 12]
  ]
  
  # 方法二：
  >>> transposed = []
  >>> for i in range(4):
  ...     transposed.append([row[i] for row in matrix])
  ...
  >>> transposed
  [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
  
  # 方法三：
  >>> transposed = []
  >>> for i in range(4):
  ...     # the following 3 lines implement the nested listcomp
  ...     transposed_row = []
  ...     for row in matrix:
  ...         transposed_row.append(row[i])
  ...     transposed.append(transposed_row)
  ...
  >>> transposed
  [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
  
  ```

#### del 语句

+ 使用 del 语句可以从一个列表中依索引而不是值来删除一个元素。
+ 这与使用 pop() 返回一个值不同。

##### 实例：用 del 语句从列表中删除一个切割，或清空整个列表（我们以前介绍的方法是给该切割赋一个空列表）。

+ ```python
  >>> a = [-1, 1, 66.25, 333, 333, 1234.5]
  >>> del a[0]
  >>> a
  [1, 66.25, 333, 333, 1234.5]
  >>> del a[2:4]
  >>> a
  [1, 66.25, 1234.5]
  >>> del a[:]
  >>> a
  []
  
  # 也可以用 del 删除实体变量：
  >>> del a
  ```

#### list 常用操作

+ ```python
  # 1.list 定义
  >>> li = ["a", "b", "mpilgrim", "z", "example"]
  >>> li
  ['a', 'b', 'mpilgrim', 'z', 'example']
  >>> li[1]        
  'b'
  
  # 2.list 负数索引
  >>> li
  ['a', 'b', 'mpilgrim', 'z', 'example']
  >>> li[-1]
  'example'
  >>> li[-3]
  'mpilgrim'
  >>> li
  ['a', 'b', 'mpilgrim', 'z', 'example']
  >>> li[1:3]  
  ['b', 'mpilgrim']
  >>> li[1:-1]
  ['b', 'mpilgrim', 'z']
  >>> li[0:3]  
  ['a', 'b', 'mpilgrim']
  
  # 3.list 增加元素
  >>> li
  ['a', 'b', 'mpilgrim', 'z', 'example']
  >>> li.append("new")
  >>> li
  ['a', 'b', 'mpilgrim', 'z', 'example', 'new']
  >>> li.insert(2, "new")
  >>> li
  ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new']
  >>> li.extend(["two", "elements"])
  >>> li
  ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']
  
  # 4.list 搜索
  >>> li
  ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']
  >>> li.index("example")
  5
  >>> li.index("new")
  2
  >>> li.index("c")
  Traceback (innermost last):
   File "<interactive input>", line 1, in ?
  ValueError: list.index(x): x not in list
  >>> "c" in li
  False
  
  # 5.list 删除元素
  >>> li
  ['a', 'b', 'new', 'mpilgrim', 'z', 'example', 'new', 'two', 'elements']
  >>> li.remove("z")  
  >>> li
  ['a', 'b', 'new', 'mpilgrim', 'example', 'new', 'two', 'elements']
  >>> li.remove("new")    # 删除首次出现的一个值
  >>> li
  ['a', 'b', 'mpilgrim', 'example', 'new', 'two', 'elements']    # 第二个 'new' 未删除
  >>> li.remove("c")     #list 中没有找到值, Python 会引发一个异常
  Traceback (innermost last):
   File "<interactive input>", line 1, in ?
  ValueError: list.remove(x): x not in list
  >>> li.pop()      # pop 会做两件事: 删除 list 的最后一个元素, 然后返回删除元素的值。
  'elements'
  >>> li
  ['a', 'b', 'mpilgrim', 'example', 'new', 'two']
  
  # 6.list 运算符
  >>> li = ['a', 'b', 'mpilgrim']
  >>> li = li + ['example', 'new']
  >>> li
  ['a', 'b', 'mpilgrim', 'example', 'new']
  >>> li += ['two']        
  >>> li
  ['a', 'b', 'mpilgrim', 'example', 'new', 'two']
  >>> li = [1, 2] * 3
  >>> li
  [1, 2, 1, 2, 1, 2]
  
  # 7.使用join链接list成为字符串
  '''
  join 只能用于所有元素都是字符串的 list; 它不进行任何的类型强制转换，join连接的list对象中存在非字符串元素的话将引发异常。
  '''
  >>> params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
  >>> ["%s=%s" % (k, v) for k, v in params.items()]
  ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
  >>> ";".join(["%s=%s" % (k, v) for k, v in params.items()])
  'server=mpilgrim;uid=sa;database=master;pwd=secret'
  
  # 8.list 分割字符串
  '''
  split 与 join 正好相反, 它将一个字符串分割成多元素 list。
  注意, 分隔符 (";") 被完全去掉了, 它没有在返回的 list 中的任意元素中出现。
  split 接受一个可选的第二个参数, 它是要分割的次数。
  '''
  >>> li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
  >>> s = ";".join(li)
  >>> s
  'server=mpilgrim;uid=sa;database=master;pwd=secret'
  >>> s.split(";")  
  ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
  >>> s.split(";", 1)
  ['server=mpilgrim', 'uid=sa;database=master;pwd=secret']
  
  # 9.list 的映射解析
  >>> li = [1, 9, 8, 4]
  >>> [elem*2 for elem in li]   
  [2, 18, 16, 8]
  >>> li
  [1, 9, 8, 4]
  >>> li = [elem*2 for elem in li]
  >>> li
  [2, 18, 16, 8]
  
  # 10.dictionary 中的解析
  >>> params = {"server":"mpilgrim", "database":"master", "uid":"sa", "pwd":"secret"}
  >>> params.keys()
  dict_keys(['server', 'database', 'uid', 'pwd'])
  >>> params.values()
  dict_values(['mpilgrim', 'master', 'sa', 'secret'])
  >>> params.items()
  dict_items([('server', 'mpilgrim'), ('database', 'master'), ('uid', 'sa'), ('pwd', 'secret')])
  >>> [k for k, v in params.items()]
  ['server', 'database', 'uid', 'pwd']
  >>> [v for k, v in params.items()]
  ['mpilgrim', 'master', 'sa', 'secret']
  >>> ["%s=%s" % (k, v) for k, v in params.items()]
  ['server=mpilgrim', 'database=master', 'uid=sa', 'pwd=secret']
  
  # 11.list 过滤
  >>> li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
  >>> [elem for elem in li if len(elem) > 1]
  ['mpilgrim', 'foo']
  >>> [elem for elem in li if elem != "b"]
  ['a', 'mpilgrim', 'foo', 'c', 'd', 'd']
  >>> [elem for elem in li if li.count(elem) == 1]
  ['a', 'mpilgrim', 'foo', 'c']
  ```

+ 

### 6.2 元组和序列

+ 元组由若干逗号分隔的值组成

#### 实例：元组的简单运用

+ ```python
  >>> t = 12345, 54321, 'hello!'
  >>> t[0]
  12345
  >>> t
  (12345, 54321, 'hello!')
  >>> # Tuples may be nested:
  ... u = t, (1, 2, 3, 4, 5)
  >>> u
  ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
  
  # 元组在输出时总是有括号的，以便于正确表达嵌套结构。在输入时可能有或没有括号， 不过括号通常是必须的（如果元组是更大的表达式的一部分）。
  ```

### 6.3 集合

+ 集合是一个无序不重复元素的集。基本功能包括关系测试和消除重复元素。
+ 可以用大括号“{}”创建集合。
+ 注意：如果要创建一个空集合，你必须用 set() 而不是 {} ；后者创建一个空的字典。

#### 实例1：集合的简单运用

+ ```python
  >>> basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
  >>> print(basket)                      # 删除重复的
  {'orange', 'banana', 'pear', 'apple'}
  >>> 'orange' in basket                 # 检测成员
  True
  >>> 'crabgrass' in basket
  False
  
  >>> # 以下演示了两个集合的操作
  ...
  >>> a = set('abracadabra')
  >>> b = set('alacazam')
  >>> a                                  # a 中唯一的字母
  {'a', 'r', 'b', 'c', 'd'}
  >>> a - b                              # 在 a 中的字母，但不在 b 中
  {'r', 'd', 'b'}
  >>> a | b                              # 在 a 或 b 中的字母
  {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
  >>> a & b                              # 在 a 和 b 中都有的字母
  {'a', 'c'}
  >>> a ^ b                              # 在 a 或 b 中的字母，但不同时在 a 和 b 中
  {'r', 'd', 'b', 'm', 'z', 'l'}
  ```

#### 实例2：集合也支持推导式

+ ```python
  >>> a = {x for x in 'abracadabra' if x not in 'abc'}
  >>> a
  {'r', 'd'}
  ```

### 6.4 字典

+ 序列是以连续的整数为索引，与此不同的是，字典以关键字为索引，关键字可以是任意不可变类型，通常用字符串或数值。
+ 理解字典的最佳方式是把它看做**无序的键=>值对集合**。
+ 在同一个字典之内，关键字必须是互不相同。
+ 一对大括号创建一个空的字典：{}。

#### 实例1：字典的简单运用

+ ```python
  >>> tel = {'jack': 4098, 'sape': 4139}
  >>> tel['guido'] = 4127
  >>> tel
  {'sape': 4139, 'guido': 4127, 'jack': 4098}
  >>> tel['jack']
  4098
  >>> del tel['sape']
  >>> tel['irv'] = 4127
  >>> tel
  {'guido': 4127, 'irv': 4127, 'jack': 4098}
  >>> list(tel.keys())
  ['irv', 'guido', 'jack']
  >>> sorted(tel.keys())
  ['guido', 'irv', 'jack']
  >>> 'guido' in tel
  True
  >>> 'jack' not in tel
  False
  ```

#### 实例2：构造函数 dict() 直接从键值对元组列表中构建字典。

+ ```python
  >>> dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
  {'sape': 4139, 'jack': 4098, 'guido': 4127}
  ```

#### 实例3：字典推导可以用来创建任意键和值的表达式词典

+ ```python
  >>> {x: x**2 for x in (2, 4, 6)}
  {2: 4, 4: 16, 6: 36}
  ```

#### 实例4：如果关键字只是简单的字符串，使用关键字参数指定键值对有时候更方便

+ ```python
  >>> dict(sape=4139, guido=4127, jack=4098)
  {'sape': 4139, 'jack': 4098, 'guido': 4127}
  ```

#### 遍历技巧

##### 实例5：在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来

+ ```python
  >>> knights = {'gallahad': 'the pure', 'robin': 'the brave'}
  >>> for k, v in knights.items():
  ...     print(k, v)
  ...
  
  # output
  '''
  gallahad the pure
  robin the brave
  '''
  
  ```

##### 实例6：在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到

+ ```python
  # enumerate: 列举
  >>> for i, v in enumerate(['tic', 'tac', 'toe']):
  ...     print(i, v)
  ...
  0 tic
  1 tac
  2 toe
  ```

##### 实例7：同时遍历两个或更多的序列，可以使用 zip() 组合

+ ```python
  >>> questions = ['name', 'quest', 'favorite color']
  >>> answers = ['lancelot', 'the holy grail', 'blue']
  >>> for q, a in zip(questions, answers):
  ...     print('What is your {0}?  It is {1}.'.format(q, a))
  ... 
  # output
  What is your name?  It is lancelot.
  What is your quest?  It is the holy grail.
  What is your favorite color?  It is blue.
  ```

##### 实例8：要反向遍历一个序列，首先指定这个序列，然后调用 reversed() 函数

+ ```python
  >>> for i in reversed(range(1, 10, 2)):
  ...     print(i)
  ...
  # output
  9
  7
  5
  3
  1
  ```

##### 实例9：要按顺序遍历一个序列，使用 sorted() 函数返回一个已排序的序列，并不修改原值

+ ```python
  >>> basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
  >>> for f in sorted(set(basket)):
  ...     print(f)
  ...
  apple
  banana
  orange
  pear
  ```

## 7. 模块

### 7.1 为什么要用模块

+ 在前面的几个章节中我们脚本上是用 python 解释器来编程，如果你从 Python 解释器退出再进入，那么你定义的所有的方法和变量就都消失了。
+ 为此 Python 提供了一个办法，把这些定义存放在文件中，为一些脚本或者交互式的解释器实例使用，这个文件被称为模块。

### 7.2 什么是模块

+ 模块是一个包含所有你定义的函数和变量的文件，其后缀名是.py。
+ 模块可以被别的程序引入，以使用该模块中的函数等功能。
+ 这也是使用 python 标准库的方法。

#### 实例：使用模块

+ ```python
  #!/usr/bin/python3
  # 文件名: using_sys.py
   
  import sys
   
  print('命令行参数如下:')
  for i in sys.argv:
     print(i)
   
  print('\n\nPython 路径为：', sys.path, '\n')
  
  # 1、import sys 引入 python 标准库中的 sys.py 模块；这是引入某一模块的方法。
  # 2、sys.argv 是一个包含命令行参数的列表。
  # 3、sys.path 包含了一个 Python 解释器自动查找所需模块的路径的列表。
  
  # output
  '''
  命令行参数如下:
  C:/Users/87143/Desktop/Python/Python源码/test.py
  
  Python 路径为： ['C:\\Users\\87143\\Desktop\\Python\\Python源码', 'C:\\Users\\87143\\Desktop\\Python\\Python源码', 'C:\\Users\\87143\\Desktop\\Python\\Python源码\\CrawlerClasses\\第八章：scrapy框架\\serialNumber\\serialNumber', 'D:\\PyCharm 2019.2.1\\plugins\\python\\helpers\\pycharm_display', 'D:\\Virtual\\scrapy\\Scripts\\python37.zip', 'D:\\Virtual\\scrapy\\DLLs', 'D:\\Virtual\\scrapy\\lib', 'D:\\Virtual\\scrapy\\Scripts', 'd:\\python3\\Lib', 'd:\\python3\\DLLs', 'D:\\Virtual\\scrapy', 'D:\\Virtual\\scrapy\\lib\\site-packages', 'D:\\PyCharm 2019.2.1\\plugins\\python\\helpers\\pycharm_matplotlib_backend'] 
  
  '''
  ```

### 7.3 import 语句

+ 使用 Python 源文件，只需在另一个源文件里执行 import 语句
+ 当解释器遇到 import 语句，如果模块在当前的搜索路径就会被导入。
+ 搜索路径是一个解释器会先进行搜索的所有目录的列表。（查看当前收缩路径: sys.path）

#### 实例1：从当前目录导入模块 support

+ 当前路径下新建support.py

+ ```python
  #!/usr/bin/python3
  # Filename: support.py
   
  def print_func( par ):
      print ("Hello : ", par)
      return
  ```

+ 当前路径下新建test.py

+ ```python
  #!/usr/bin/python3
  # Filename: test.py
   
  # 导入模块
  import support
   
  # 现在可以调用模块里包含的函数了
  support.print_func("Runoob")
  
  
  # output
  '''
  hello : Runoob
  '''
  ```

#### 说明

+ 一个模块只会被导入一次，不管你执行了多少次import。（这样可以防止导入模块被一遍又一遍地执行）
+ 在当前目录下存在与要引入模块同名的文件，就会把要引入的模块屏蔽掉。（当前目录下的同名模块优先级大于其它搜索路径下的同名模块 ）
+ 当我们使用import语句的时候，Python解释器是怎样找到对应的文件的呢？
  + Python解释器可以依次从搜索路径中去寻找所引入的模块。

#### 实例2：在解释器的当前目录或者 sys.path 中的一个目录里面来创建一个fibo.py的文件

+ ```python
  # 斐波那契(fibonacci)数列模块
   
  def fib(n):    # 定义到 n 的斐波那契数列
      a, b = 0, 1
      while b < n:
          print(b, end=' ')
          a, b = b, a+b
      print()
   
  def fib2(n): # 返回到 n 的斐波那契数列
      result = []
      a, b = 0, 1
      while b < n:
          result.append(b)
          a, b = b, a+b
      return result
  ```

+ 导入fibo 模块

+ ```python
  >>> import fibo
  
  >>>fibo.fib(1000)
  1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987
  >>> fibo.fib2(100)
  [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  >>> fibo.__name__
  'fibo'
  
  # 如果你打算经常使用一个函数，你可以把它赋给一个本地的名称：
  >>> fib = fibo.fib
  >>> fib(500)
  1 1 2 3 5 8 13 21 34 55 89 144 233 377
  ```

### 7.4 from … import 语句

#### 实例：导入7.3实例2中的fibo的fib函数

+ ```python
  >>> from fibo import fib, fib2
  >>> fib(500)
  1 1 2 3 5 8 13 21 34 55 89 144 233 377
  
  ```

+ 这个声明不会把整个fibo模块导入到当前的命名空间中，它只会将fibo里的fib函数引入进来。

### 7.5 from ... import * 语句

#### 实例：把一个模块的所有内容全都导入到当前的命名空间。

+ ```python
  from ... import *
  ```

+ 种声明不该被过多地使用。

### 7.6 深入模块

#### 说明

+ 模块除了方法定义，还可以包括可执行的代码。这些代码一般用来初始化这个模块。这些代码只有在第一次被导入时才会被执行。
+ 每个模块有各自独立的符号表，在模块内部为所有的函数当作全局符号表来使用。（所以，模块的作者可以放心大胆的在模块内部使用这些全局变量，而不用担心把其他用户的全局变量搞混。）
+ 当你确实知道你在做什么的话，你可以通过：“模块.函数名” 来访问模块内的函数。
+ 模块是可以导入其他模块的（一般在最前面使用 import 来导入一个模块，也可在其他位置）。被导入的模块的名称将被放入当前操作的模块的符号表中。
+ 使用 from modname import itemname 直接把该模块的函数导入到当前操作模块，不会把被导入的模块的名称放在当前的字符表中（直接使用import modname 则会）。

#### 实例1：仅导入模块的函数或变量，而不把模块的名称放在当前操作模块的字符表中。

+ ```python
  >>> from fibo import fib, fib2
  >>> fib(500)
  1 1 2 3 5 8 13 21 34 55 89 144 233 377
  
  # 这种导入的方法不会把被导入的模块的名称放在当前的字符表中（所以在这个例子里面，fibo 这个名称是没有定义的）。
  ```

#### 实例2：一次性的把模块中的所有（函数，变量）名称都导入到当前模块的字符表。

+ ```python
  >>> from fibo import *
  >>> fib(500)
  1 1 2 3 5 8 13 21 34 55 89 144 233 377
  
  # 这将把所有的名字都导入进来，但是那些由单一下划线（_）开头的名字不在此例。
  # 大多数情况， Python程序员不使用这种方法，因为引入的其它来源的命名，很可能覆盖了已有的定义。
  ```

### 7.7 __ name __属性

#### 说明

+ 个模块被另一个程序第一次引入时，其主程序将运行。
+ 如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
+ 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入。

#### 实例：模块限制其他人调用某些方法

+ ```python
  # 被调用方：using_name.py
  
  if __name__ == '__main__':
      print('仅供模块本身调用')
  
      def print_1(par):
          print("Hello : ", par)
          return
  
  else:
      print('所有人均可调用')
  
      def print_2():
          print("Hello, everyone")
          return
  ```

+ ```python
  import using_name
  
  using_name.print_2()
  ```

### 7.8 dir() 函数

+ 内置的函数 dir() 可以找到模块内定义的所有名称。

#### 实例1：以一个字符串列表的形式返回模块内定义的所有名称

+ ```python
  >>> import fibo, sys
  >>> dir(fibo)
  ['__name__', 'fib', 'fib2']
  >>> dir(sys)  
  ['__displayhook__', '__doc__', '__excepthook__', '__loader__', '__name__',
   '__package__', '__stderr__', '__stdin__', '__stdout__',
   '_clear_type_cache', '_current_frames', '_debugmallocstats', '_getframe',
   '_home', '_mercurial', '_xoptions', 'abiflags', 'api_version', 'argv',
   'base_exec_prefix', 'base_prefix', 'builtin_module_names', 'byteorder',
   'call_tracing', 'callstats', 'copyright', 'displayhook',
   'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix',
   'executable', 'exit', 'flags', 'float_info', 'float_repr_style',
   'getcheckinterval', 'getdefaultencoding', 'getdlopenflags',
   'getfilesystemencoding', 'getobjects', 'getprofile', 'getrecursionlimit',
   'getrefcount', 'getsizeof', 'getswitchinterval', 'gettotalrefcount',
   'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info',
   'intern', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path',
   'path_hooks', 'path_importer_cache', 'platform', 'prefix', 'ps1',
   'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit',
   'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout',
   'thread_info', 'version', 'version_info', 'warnoptions']
  ```

#### 实例2：如果dir()没有给定参数，则会罗列出当前定义的所有名称

+ ```python
  >>> a = [1, 2, 3, 4, 5]
  >>> import fibo
  >>> fib = fibo.fib
  >>> dir() # 得到一个当前模块中定义的属性列表
  ['__builtins__', '__name__', 'a', 'fib', 'fibo', 'sys']
  >>> a = 5 # 建立一个新的变量 'a'
  >>> dir()
  ['__builtins__', '__doc__', '__name__', 'a', 'sys']
  >>>
  >>> del a # 删除变量名a
  >>>
  >>> dir()
  ['__builtins__', '__doc__', '__name__', 'sys']
  >>>
  ```

### 7.9 标准模块

#### 说明

+ Python 本身带着一些标准的模块库。
+ 有些模块直接被构建在解析器里，这些虽然不是一些语言内置的功能，但是他却能很高效的使用，甚至是系统级调用也没问题。
+ Python组件会根据不同的操作系统进行不同形式的配置，比如 winreg 这个模块就只会提供给 Windows 系统。
+ 有一个特别的模块 sys ，它内置在每一个 Python 解析器中。

#### 实例：通过变量 sys.ps1 和 sys.ps2 修改主提示符和副提示符所对应的字符串

+ ```python
  >>> import sys
  >>> sys.ps1
  '>>> '
  >>> sys.ps2
  '... '
  >>> sys.ps1 = 'C> '
  C> print('Runoob!')  # 此时提示符从 ‘>>>’ ==> ‘C>’
  Runoob!
  C> 
  ```

### 7.10 包

#### 什么是包

+ 包是一种管理 Python 模块命名空间的形式，采用"点模块名称"。
+ 比如：一个模块的名称是 A.B， 那么他表示一个包 A中的子模块 B 。

#### 包的好处

+ 包采用点模块名称这种形式，就不用担心不同库之间的模块重名的情况，这样不同的作者都可以提供 NumPy 模块，或者是 Python 图形库。

#### 实例：假设设计一套统一处理声音文件和数据的模块（或者称之为一个"包"）。

+ 因为有很多种不同的音频文件格式（例如： .wav，:file:.aiff，:file:.au，），所以你需要有一组不断增加的模块，用来在不同的格式之间转换。

+ 并且针对这些音频数据，还有很多不同的操作（比如混音，添加回声，增加均衡器功能，创建人造立体声效果），所以你还需要一组怎么也写不完的模块来处理这些操作。

+ 这里给出了一种可能的包结构（在分层的文件系统中）:

+ ```python
  sound/                          顶层包(目录)
        __init__.py               初始化 sound 包
        formats/                  文件格式转换子包
                __init__.py
                wavread.py
                wavwrite.py
                aiffread.py
                aiffwrite.py
                auread.py
                auwrite.py
                ...
        effects/                  声音效果子包
                __init__.py
                echo.py
                surround.py
                reverse.py
                ...
        filters/                  filters 子包
                __init__.py
                equalizer.py
                vocoder.py
                karaoke.py
                ...
  ```

+ 在导入一个包的时候，Python 会根据 sys.path 中的目录来寻找这个包中包含的子目录。

+ 目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包，主要是为了避免一些滥俗的名字（比如叫做 string）不小心的影响搜索路径中的有效模块。

+ __init__.py文件可以为空，当然这个文件中也可以包含一些初始化代码或者为 __all__ 变量赋值。



+ 用户可以每次只导入一个包里面的特定模块，比如:

+ ```python
  import sound.effects.echo
  ```

+ 这将会导入子模块:sound.effects.echo。 他必须使用全名去访问:

  ```python
  sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)
  ```

  还有一种导入子模块的方法是:

  ```python
  from sound.effects import echo
  ```

  这同样会导入子模块: echo，并且他不需要那些冗长的前缀，所以他可以这样使用:

  ```python
  echo.echofilter(input, output, delay=0.7, atten=4)
  ```

  还有一种变化就是直接导入一个函数或者变量:

  ```python
  from sound.effects.echo import echofilter
  ```

  同样的，这种方法会导入子模块: echo，并且可以直接使用他的 echofilter() 函数:

  ```python
  echofilter(input, output, delay=0.7, atten=4)
  ```

#### 注意

+ 当使用 **from package import item** 这种形式的时候，对应的 item 既可以是包里面的子模块（子包），或者包里面定义的其他名称，比如函数，类或者变量。
+ import 语法会首先把 item 当作一个包定义的名称，如果没找到，再试图按照一个模块去导入。如果还没找到，抛出一个 **:exc:ImportError** 异常。
+ 如果使用形如 **import item.subitem.subsubitem** 这种导入形式，**除了最后一项，都必须是包**，而最后一项则可以是模块或者是包，但是不可以是类，函数或者变量的名字。

#### 从一个包中导入 *

##### windows使用该方法的弊端

+ 使用 from sound.effects import *，Python 会进入文件系统，找到这个包里面所有的子模块，一个一个的把它们都导入进来。

+ 但是很不幸，这个方法在 Windows平台上工作在这类平台上，没有人敢担保一个叫做 ECHO.py 的文件导入为模块 echo 还是 Echo 甚至 ECHO。

  （例如，Windows 95就很讨厌的把每一个文件的首字母大写显示）而且 DOS 的 8+3 命名规则对长模块名称的处理会把问题搞得更纠结。的就不是非常好，因为Windows是一个大小写不区分的系统。

##### 解决方法

+ 包作者提供一个精确的包的索引
  + 导入语句遵循如下规则：如果包定义文件 __init__.py 存在一个叫做 __all__ 的列表变量，那么在使用 from package import * 的时候就把这个列表中的所有名字作为包内容导入。
  + 包的作者应该在更新包之后保证 __all__ 也更新了。

##### 实例1：在:file:sounds/effects/__init__.py中包含如下代码

+ ```python
  __all__ = ["echo", "surround", "reverse"]
  ```

+ 这表示使用from sound.effects import *这种用法时，只会导入包里面这三个子模块。

+ 如果 **__all__** 真的没有定义，那么使用**from sound.effects import \***这种语法的时候，就不会导入包 sound.effects 里的任何子模块。他只是把包sound.effects和它里面定义的所有内容导入进来（可能运行__init__.py里定义的初始化代码）。

##### 实例2：使用 * 方法导入模块之前，导入的所有明确指定的模块

+ 这会把 __init__.py 里面定义的所有名字导入进来。并且他不会破坏掉我们在这句话之前导入的所有明确指定的模块。

+ ```python
  import sound.effects.echo
  import sound.effects.surround
  from sound.effects import *
  
  # 这个例子中，在执行 from...import 前，包 sound.effects 中的 echo 和 surround 模块都被导入到当前的命名空间中了。（当然如果定义了 __all__ 就更没问题了）
  ```

##### 注意

+ 通常我们并不主张使用 ***** 这种方法来导入模块，因为这种方法经常会导致代码的可读性降低。
  + 不过这样倒的确是可以省去不少敲键的功夫，而且一些模块都设计成了只能通过特定的方法导入。
+ 使用 **from Package import specific_submodule** 这种方法永远不会有错。
  + 事实上，这也是推荐的方法。除非是你要导入的子模块有可能和其他包的子模块重名。

##### 解决导入的子模块和其他包的子模块重名

+ ```python
  import sound.effects.test as sound_test
  import game.effects.test as game_test
  ```

##### 实例3：使用相对路径导包

+ ```python
  from . import echo
  from .. import formats
  from ..filters import equalizer
  ```

+ 如果在结构中包是一个子包（比如这个例子中对于包sound来说），而你又想导入兄弟包（同级别的包）你就得使用导入绝对的路径来导入。

  + 比如，如果模块sound.filters.vocoder 要使用包 sound.effects 中的模块 echo，你就要写成 from sound.effects import echo。

##### 补充

+ 无论是隐式的还是显式的相对导入都是从当前模块开始的。
+ 主模块的名字永远是"__main__"，一个Python应用程序的主模块，应当总是使用绝对路径引用。
+ 包还提供一个额外的属性__path__。
  + 这是一个目录列表，里面每一个包含的目录都有为这个包服务的__init__.py，你得在其他__init__.py被执行前定义哦。
  + 可以修改这个变量，用来影响包含在包里面的模块和子包。
  + 这个功能并不常用，一般用来扩展包里面的模块。

## 8 输入和输出

### 8.1 输出格式美化

+ 输出值的方式
  + 表达式语句
  + print() 函数
  + 第三种方式是使用文件对象的 write() 方法，标准输出文件可以用 sys.stdout 引用。
+ 如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
+ 如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
  + **str()：** 返回一个用户易读的表达形式。
  + **repr()：** 返回一个解释器易读的表达形式。

#### 实例1：str(), repr()函数的简单使用

+ ```python
  >>> s = 'Hello, Runoob'
  >>> str(s)
  'Hello, Runoob'
  
  >>> repr(s)
  "'Hello, Runoob'"
  
  >>> str(1/7)
  '0.14285714285714285'
  
  >>> x = 10 * 3.25
  >>> y = 200 * 200
  >>> s = 'x 的值为： ' + repr(x) + ',  y 的值为：' + repr(y) + '...'
  >>> print(s)
  x 的值为： 32.5,  y 的值为：40000...
  
  >>> #  repr() 函数可以转义字符串中的特殊字符
  ... hello = 'hello, runoob\n'
  >>> hellos = repr(hello)
  >>> print(hellos)
  'hello, runoob\n'
  
  >>> # repr() 的参数可以是 Python 的任何对象
  ... repr((x, y, ('Google', 'Runoob')))
  "(32.5, 40000, ('Google', 'Runoob'))"
  ```

#### 实例2：两种方式输出一个平方与立方的表

+ ```python
  >>> for x in range(1, 11):
  ...     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
  ...     # 注意前一行 'end' 的使用
  ...     print(repr(x*x*x).rjust(4))
  ...
   1   1    1
   2   4    8
   3   9   27
   4  16   64
   5  25  125
   6  36  216
   7  49  343
   8  64  512
   9  81  729
  10 100 1000
  
  >>> for x in range(1, 11):
  ...     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
  ...
   1   1    1
   2   4    8
   3   9   27
   4  16   64
   5  25  125
   6  36  216
   7  49  343
   8  64  512
   9  81  729
  10 100 1000
  
  # 注意：
  在第一个例子中, 每列间的空格由 print() 添加。
  这个例子展示了字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。
  还有类似的方法, 如 ljust() 和 center()。 这些方法并不会写任何东西, 它们仅仅返回新的字符串。
  ```

#### 实例3：在数字的左边填充0的zfill()函数

+ ```python
  >>> '12'.zfill(5)
  '00012'
  >>> '-3.14'.zfill(7)
  '-003.14'
  >>> '3.14159265359'.zfill(5)
  '3.14159265359'
  ```

#### 实例4：字符串.format()的基本使用

+ ```python
  # 括号及其里面的字符 (称作格式化字段) 将会被 format() 中的参数替换。
  >>> print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))
  菜鸟教程网址： "www.runoob.com!"
  
  # 在括号中的数字用于指向传入对象在 format() 中的位置，如下所示：
  >>> print('{0} 和 {1}'.format('Google', 'Runoob'))
  Google 和 Runoob
  >>> print('{1} 和 {0}'.format('Google', 'Runoob'))
  Runoob 和 Google
  
  # 如果在 format() 中使用了关键字参数, 那么它们的值会指向使用该名字的参数。
  >>> print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))
  菜鸟教程网址： www.runoob.com
  
  # 位置及关键字参数可以任意的结合:
  >>> print('站点列表 {0}, {1}, 和 {other}。'.format('Google', 'Runoob', other='Taobao'))
  站点列表 Google, Runoob, 和 Taobao。
  
  # !a (使用 ascii()), !s (使用 str()) 和 !r (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
  >>> import math
  >>> print('常量 PI 的值近似为： {}。'.format(math.pi))
  常量 PI 的值近似为： 3.141592653589793。
  >>> print('常量 PI 的值近似为： {!r}。'.format(math.pi))
  常量 PI 的值近似为： 3.141592653589793。
  
  # 可选项 : 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。 下面的例子将 Pi 保留到小数点后三位：
  >>> import math
  >>> print('常量 PI 的值近似为 {0:.3f}。'.format(math.pi))
  常量 PI 的值近似为 3.142。
  
  # 在 : 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
  >>> table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
  >>> for name, number in table.items():
  ...     print('{0:10} ==> {1:10d}'.format(name, number))
  ...
  Google     ==>          1
  Runoob     ==>          2
  Taobao     ==>          3
  
  # 如果你有一个很长的格式化字符串, 而你不想将它们分开, 那么在格式化时通过变量名而非位置会是很好的事情。
  >>> table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
  >>> print('Runoob: {0[Runoob]:d}; Google: {0[Google]:d}; Taobao: {0[Taobao]:d}'.format(table))
  # print('Runoob: {table[Runoob]:d}; Google: {table[Google]:d}; Taobao: {table[Taobao]:d}'.format(table))
  Runoob: 2; Google: 1; Taobao: 3
  
  # 也可以通过在 table 变量前使用 ** 来实现相同的功能
  >>> table = {'Google': 1, 'Runoob': 2, 'Taobao': 3}
  >>> print('Runoob: {Runoob:d}; Google: {Google:d}; Taobao: {Taobao:d}'.format(**table))
  Runoob: 2; Google: 1; Taobao: 3
  ```

### 8.2 旧式字符串格式化

+ 它将左边的参数作为类似 **sprintf()** 式的格式化字符串, 而将右边的代入, 然后返回格式化后的字符串

#### 字符串格式化：旧式 VS 新式

+ 因为 str.format() 是比较新的函数， 大多数的 Python 代码仍然使用 % 操作符。但是因为这种旧式的格式化最终会从该语言中移除, 应该更多的使用 str.format()。

#### 实例：**%** 操作符实现字符串格式化

+ ```python
  >>> import math
  >>> print('常量 PI 的值近似为：%5.3f。' % math.pi)
  常量 PI 的值近似为：3.142。
  ```

### 8.3 读取键盘输入

+ Python提供了 input() 内置函数从标准输入读入一行文本，默认的标准输入是键盘。

#### 实例：input 接收一个Python表达式作为输入，并将运算结果返回。

+ ```python
  #!/usr/bin/python3
  
  str = input("请输入：");
  print ("你输入的内容是: ", str)
  
  # output
  '''
  请输入：菜鸟教程
  你输入的内容是:  菜鸟教程
  '''
  ```

### 8.4 读 / 写文件

#### open() 函数的用法

+ open() 将会返回一个 file 对象，基本语法格式如下

  + ```python
    open(filename, mode)
    
    # filename：包含了你要访问的文件名称的字符串值。
    # mode：决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
    ```

#### 打开文件的所有模式

+ | 模式 | 描述                                                         |
  | :--- | :----------------------------------------------------------- |
  | r    | 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。 |
  | rb   | 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。 |
  | r+   | 打开一个文件用于读写。文件指针将会放在文件的开头。           |
  | rb+  | 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。 |
  | w    | 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
  | wb   | 以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
  | w+   | 打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
  | wb+  | 以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
  | a    | 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
  | ab   | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
  | a+   | 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。 |
  | ab+  | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。 |

+ |    模式    |  r   |  r+  |  w   |  w+  |  a   |  a+  |
  | :--------: | :--: | :--: | :--: | :--: | :--: | :--: |
  |     读     |  +   |  +   |      |  +   |      |  +   |
  |     写     |      |  +   |  +   |  +   |  +   |  +   |
  |    创建    |      |      |  +   |  +   |  +   |  +   |
  |    覆盖    |      |      |  +   |  +   |      |      |
  | 指针在开始 |  +   |  +   |  +   |  +   |      |      |
  | 指针在结尾 |      |      |      |      |  +   |  +   |

#### 实例：将字符串写入到文件 foo.txt 中。

+ ```python
  #!/usr/bin/python3
  
  # 打开一个文件
  f = open("/tmp/foo.txt", "w")
  f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
  # 关闭打开的文件
  f.close()
  
  # output
  '''
  $ cat /tmp/foo.txt 
  Python 是一个非常好的语言。
  是的，的确非常好!!
  '''
  
  
  # 第一个参数为要打开的文件名。
  # 第二个参数描述文件如何使用的字符。 mode 可以是 'r' 如果文件只读, 'w' 只用于写 (如果存在同名文件则将被删除), 和 'a' 用于追加文件内容; 所写的任何数据都会被自动增加到末尾. 'r+' 同时用于读写。 mode 参数是可选的; 'r' 将是默认值。
  
  ```

### 8.5 文件对象的方法

#### f.read()

+ 为了读取一个文件的内容，调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回。
+ size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回。

##### 实例：读取8.4创建的foo.txt中的全部内容

+ ```python
  #!/usr/bin/python3
  
  # 打开一个文件
  f = open("/tmp/foo.txt", "r")
  str = f.read()
  print(str)
  
  # 关闭打开的文件
  f.close()
  
  #output
  '''
  Python 是一个非常好的语言。
  是的，的确非常好!!
  '''
  ```

#### f.readline()

+ f.readline() 会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。

##### 实例：逐行读取8.4创建的foo.txt中的内容

+ ```python
  #!/usr/bin/python3
  
  # 打开一个文件
  f = open("/tmp/foo.txt", "r")
  str = f.readline()
  print(str)
  
  # 关闭打开的文件
  f.close()
  
  # output
  '''
  Python 是一个非常好的语言。
  '''
  ```

#### f.readlines()

+ .readlines() 将返回一个**列表**，该列表会包含文件内容的所有行。
+ 如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。

##### 实例：读取8.4创建的foo.txt中的所有行，并返回一个列表。

+ ```python
  #!/usr/bin/python3
  
  # 打开一个文件
  f = open("/tmp/foo.txt", "r")
  str = f.readlines()
  print(str)
  
  # 关闭打开的文件
  f.close()
  
  # output
  '''
  ['Python 是一个非常好的语言。\n', '是的，的确非常好!!\n']
  '''
  ```

#### 其它读取文件内容方式

##### 实例：迭代一个文件对象然后读取每行

+ 这个方法很简单, 但是并没有提供一个很好的控制。 因为两者的处理机制不同, 最好不要混用。

+ ```python
  #!/usr/bin/python3
  
  # 打开一个文件
  f = open("/tmp/foo.txt", "r")
  for line in f:
      print(line, end='')
  
  # 关闭打开的文件
  f.close()
  
  # output
  '''
  Python 是一个非常好的语言。
  是的，的确非常好!!
  '''
  ```

#### f.write(string)

##### 实例1： 把内容 写入到文件中, 然后返回写入的字符数。

+ ```python
  #!/usr/bin/python3
  
  # 打开一个文件
  f = open("/tmp/foo.txt", "w")
  num = f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
  print(num)
  
  # 关闭打开的文件
  f.close()
  
  # output
  '''
  29
  '''
  ```

##### 实例2：写入不是字符串的内容要先进行转换。

+ ```python
  #!/usr/bin/python3
  
  # 打开一个文件
  f = open("/tmp/foo1.txt", "w")
  
  value = ('www.runoob.com', 14)
  s = str(value)
  f.write(s)
  
  # 关闭打开的文件
  f.close()
  
  # output
  '''
  $ cat /tmp/foo1.txt 
  ('www.runoob.com', 14)
  '''
  ```

#### f.tell()

+ f.tell() 返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数。

#### f.seek()

+ 如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。(from_what 值为默认为0，即文件开头。)
+ from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：
  + seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
  + seek(x,1) ： 表示从当前位置往后移动x个字符
  + seek(-x,2)：表示从文件的结尾往前移动x个字符

##### 实例：使用f.seek()改变读取的文件当前位置

+ ```python
  >>> f = open('/tmp/foo.txt', 'rb+')
  >>> f.write(b'0123456789abcdef')
  16
  >>> f.seek(5)     # 移动到文件的第六个字节
  5
  >>> f.read(1)
  b'5'
  >>> f.seek(-3, 2) # 移动到文件的倒数第三字节
  13
  >>> f.read(1)
  b'd'
  ```

#### f.close()

+ 在文本文件中 (那些打开文件的模式下没有 b 的), 只会相对于文件起始位置进行定位。

##### 实例：关闭文件对象

+ ```python
  # 当你处理完一个文件后, 调用 f.close() 来关闭文件并释放系统的资源，如果再调用已关闭的文件对象，则会抛出异常。
  >>> f.close()
  >>> f.read()
  Traceback (most recent call last):
    File "<stdin>", line 1, in ?
  ValueError: I/O operation on closed file
  
  # 当处理一个文件对象时, 使用 with 关键字是非常好的方式。在结束后, 它会帮你正确的关闭文件
  # 在结束后, 它会帮你正确的关闭文件。
  # 而且写起来也比 try - finally 语句块要简短
  >>> with open('/tmp/foo.txt', 'r') as f:
  ...     read_data = f.read()
  >>> f.closed
  True
  ```

##### 补充

+ 文件对象还有其他方法, 如 isatty() 和 trucate(), 但这些通常比较少用。

### 8.6 pickle模块

#### pickle的作用

+ pickle模块实现了基本的数据序列和反序列化。

+ pickle.dump(obj, file, [,protocol]) 
  + 通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
+ pickle.load(file)
  + 通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
  + **注解：**从 file 中读取一个字符串，并将它重构为原来的python对象。
  + **file:** 类文件对象，有read()和readline()接口。

#### 实例1：使用pickle模块将数据对象保存到文件

+ ```python
  #!/usr/bin/python3
  import pickle
  
  # 使用pickle模块将数据对象保存到文件
  data1 = {'a': [1, 2.0, 3, 4+6j],
           'b': ('string', u'Unicode string'),
           'c': None}
  
  selfref_list = [1, 2, 3]
  selfref_list.append(selfref_list)
  
  output = open('data.pkl', 'wb')
  
  # Pickle dictionary using protocol 0.
  pickle.dump(data1, output)
  
  # Pickle the list using the highest protocol available.
  pickle.dump(selfref_list, output, -1)
  
  output.close()
  ```

#### 实例2：使用pickle模块从文件中重构python对象

+ ```python
  #!/usr/bin/python3
  import pprint, pickle
  
  #使用pickle模块从文件中重构python对象
  pkl_file = open('data.pkl', 'rb')
  
  data1 = pickle.load(pkl_file)
  pprint.pprint(data1)
  
  data2 = pickle.load(pkl_file)
  pprint.pprint(data2)
  
  pkl_file.close()
  ```

## 9. File(文件) 

### 9.1 open() 方法

+ Python open() 方法用于打开一个文件，并返回文件对象，在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError。

#### 注意

+ 使用 open() 方法一定要保证关闭文件对象，即调用 close() 方法。

+ open() 函数常用形式是接收两个参数：文件名(file)和模式(mode)。

+ 完整的语法格式

  + ```python
    open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    
    # 参数说明:
    file: 必需，文件路径（相对或者绝对路径）。
    mode: 可选，文件打开模式
    buffering: 设置缓冲
    encoding: 一般使用utf8
    errors: 报错级别
    newline: 区分换行符
    closefd: 传入的file参数类型
    opener: 设置自定义开启器，开启器的返回值必须是一个打开的文件描述符。
    ```

#### mode参数一览表

+ | 模式 | 描述                                                         |
  | :--- | :----------------------------------------------------------- |
  | t    | 文本模式 (默认)。                                            |
  | x    | 写模式，新建一个文件，如果该文件已存在则会报错。             |
  | b    | 二进制模式。                                                 |
  | +    | 打开一个文件进行更新(可读可写)。                             |
  | U    | 通用换行模式（**Python 3 不支持**）。                        |
  | r    | 以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。 |
  | rb   | 以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。一般用于非文本文件如图片等。 |
  | r+   | 打开一个文件用于读写。文件指针将会放在文件的开头。           |
  | rb+  | 以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。一般用于非文本文件如图片等。 |
  | w    | 打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
  | wb   | 以二进制格式打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。 |
  | w+   | 打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。 |
  | wb+  | 以二进制格式打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。一般用于非文本文件如图片等。 |
  | a    | 打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
  | ab   | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。 |
  | a+   | 打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。 |
  | ab+  | 以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。 |

### 9.2 file 对象

+ file 对象使用 open 函数来创建

#### file 对象常用的函数一览表

+ | 序号 | 方法及描述                                                   |
  | :--- | :----------------------------------------------------------- |
  | 1    | [file.close()](https://www.runoob.com/python3/python3-file-close.html)关闭文件。关闭后文件不能再进行读写操作。 |
  | 2    | [file.flush()](https://www.runoob.com/python3/python3-file-flush.html)刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。 |
  | 3    | [file.fileno()](https://www.runoob.com/python3/python3-file-fileno.html)返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。 |
  | 4    | [file.isatty()](https://www.runoob.com/python3/python3-file-isatty.html)如果文件连接到一个终端设备返回 True，否则返回 False。 |
  | 5    | [file.next()](https://www.runoob.com/python3/python3-file-next.html)**Python 3 中的 File 对象不支持 next() 方法。**返回文件下一行。 |
  | 6    | [file.read([size\])](https://www.runoob.com/python3/python3-file-read.html)从文件读取指定的字节数，如果未给定或为负则读取所有。 |
  | 7    | [file.readline([size\])](https://www.runoob.com/python3/python3-file-readline.html)读取整行，包括 "\n" 字符。 |
  | 8    | [file.readlines([sizeint\])](https://www.runoob.com/python3/python3-file-readlines.html)读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比 sizeint 较大, 因为需要填充缓冲区。 |
  | 9    | [file.seek(offset[, whence\])](https://www.runoob.com/python3/python3-file-seek.html)移动文件读取指针到指定位置 |
  | 10   | [file.tell()](https://www.runoob.com/python3/python3-file-tell.html)返回文件当前位置。 |
  | 11   | [file.truncate([size\])](https://www.runoob.com/python3/python3-file-truncate.html)从文件的首行首字符开始截断，截断文件为 size 个字符，无 size 表示从当前位置截断；截断之后后面的所有字符被删除，其中 windows 系统下的换行代表2个字符大小。 |
  | 12   | [file.write(str)](https://www.runoob.com/python3/python3-file-write.html)将字符串写入文件，返回的是写入的字符长度。 |
  | 13   | [file.writelines(sequence)](https://www.runoob.com/python3/python3-file-writelines.html)向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。 |

## 10. OS 文件/目录方法

+ **os** 模块提供了非常丰富的方法用来处理文件和目录。

### 常用的方法如下表所示

+ | 序号 | 方法及描述                                                   |
  | :--- | :----------------------------------------------------------- |
  | 1    | [os.access(path, mode)](https://www.runoob.com/python3/python3-os-access.html) 检验权限模式 |
  | 2    | [os.chdir(path)](https://www.runoob.com/python3/python3-os-chdir.html) 改变当前工作目录 |
  | 3    | [os.chflags(path, flags)](https://www.runoob.com/python3/python3-os-chflags.html) 设置路径的标记为数字标记。 |
  | 4    | [os.chmod(path, mode)](https://www.runoob.com/python3/python3-os-chmod.html) 更改权限 |
  | 5    | [os.chown(path, uid, gid)](https://www.runoob.com/python3/python3-os-chown.html) 更改文件所有者 |
  | 6    | [os.chroot(path)](https://www.runoob.com/python3/python3-os-chroot.html) 改变当前进程的根目录 |
  | 7    | [os.close(fd)](https://www.runoob.com/python3/python3-os-close.html) 关闭文件描述符 fd |
  | 8    | [os.closerange(fd_low, fd_high)](https://www.runoob.com/python3/python3-os-closerange.html) 关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略 |
  | 9    | [os.dup(fd)](https://www.runoob.com/python3/python3-os-dup.html) 复制文件描述符 fd |
  | 10   | [os.dup2(fd, fd2)](https://www.runoob.com/python3/python3-os-dup2.html) 将一个文件描述符 fd 复制到另一个 fd2 |
  | 11   | [os.fchdir(fd)](https://www.runoob.com/python3/python3-os-fchdir.html) 通过文件描述符改变当前工作目录 |
  | 12   | [os.fchmod(fd, mode)](https://www.runoob.com/python3/python3-os-fchmod.html) 改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。 |
  | 13   | [os.fchown(fd, uid, gid)](https://www.runoob.com/python3/python3-os-fchown.html) 修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。 |
  | 14   | [os.fdatasync(fd)](https://www.runoob.com/python3/python3-os-fdatasync.html) 强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。 |
  | 15   | [os.fdopen(fd[, mode[, bufsize\]])](https://www.runoob.com/python3/python3-os-fdopen.html) 通过文件描述符 fd 创建一个文件对象，并返回这个文件对象 |
  | 16   | [os.fpathconf(fd, name)](https://www.runoob.com/python3/python3-os-fpathconf.html) 返回一个打开的文件的系统配置信息。name为检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。 |
  | 17   | [os.fstat(fd)](https://www.runoob.com/python3/python3-os-fstat.html) 返回文件描述符fd的状态，像stat()。 |
  | 18   | [os.fstatvfs(fd)](https://www.runoob.com/python3/python3-os-fstatvfs.html) 返回包含文件描述符fd的文件的文件系统的信息，Python 3.3 相等于 statvfs()。 |
  | 19   | [os.fsync(fd)](https://www.runoob.com/python3/python3-os-fsync.html) 强制将文件描述符为fd的文件写入硬盘。 |
  | 20   | [os.ftruncate(fd, length)](https://www.runoob.com/python3/python3-os-ftruncate.html) 裁剪文件描述符fd对应的文件, 所以它最大不能超过文件大小。 |
  | 21   | [os.getcwd()](https://www.runoob.com/python3/python3-os-getcwd.html) 返回当前工作目录 |
  | 22   | [os.getcwdu()](https://www.runoob.com/python3/python3-os-getcwdu.html) 返回一个当前工作目录的Unicode对象 |
  | 23   | [os.isatty(fd)](https://www.runoob.com/python3/python3-os-isatty.html) 如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。 |
  | 24   | [os.lchflags(path, flags)](https://www.runoob.com/python3/python3-os-lchflags.html) 设置路径的标记为数字标记，类似 chflags()，但是没有软链接 |
  | 25   | [os.lchmod(path, mode)](https://www.runoob.com/python3/python3-os-lchmod.html) 修改连接文件权限 |
  | 26   | [os.lchown(path, uid, gid)](https://www.runoob.com/python3/python3-os-lchown.html) 更改文件所有者，类似 chown，但是不追踪链接。 |
  | 27   | [os.link(src, dst)](https://www.runoob.com/python3/python3-os-link.html) 创建硬链接，名为参数 dst，指向参数 src |
  | 28   | [os.listdir(path)](https://www.runoob.com/python3/python3-os-listdir.html) 返回path指定的文件夹包含的文件或文件夹的名字的列表。 |
  | 29   | [os.lseek(fd, pos, how)](https://www.runoob.com/python3/python3-os-lseek.html) 设置文件描述符 fd当前位置为pos, how方式修改: SEEK_SET 或者 0 设置从文件开始的计算的pos; SEEK_CUR或者 1 则从当前位置计算; os.SEEK_END或者2则从文件尾部开始. 在unix，Windows中有效 |
  | 30   | [os.lstat(path)](https://www.runoob.com/python3/python3-os-lstat.html) 像stat(),但是没有软链接 |
  | 31   | [os.major(device)](https://www.runoob.com/python3/python3-os-major.html) 从原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。 |
  | 32   | [os.makedev(major, minor)](https://www.runoob.com/python3/python3-os-makedev.html) 以major和minor设备号组成一个原始设备号 |
  | 33   | [os.makedirs(path[, mode\])](https://www.runoob.com/python3/python3-os-makedirs.html) 递归文件夹创建函数。像mkdir(), 但创建的所有intermediate-level文件夹需要包含子文件夹。 |
  | 34   | [os.minor(device)](https://www.runoob.com/python3/python3-os-minor.html) 从原始的设备号中提取设备minor号码 (使用stat中的st_dev或者st_rdev field )。 |
  | 35   | [os.mkdir(path[, mode\])](https://www.runoob.com/python3/python3-os-mkdir.html) 以数字mode的mode创建一个名为path的文件夹.默认的 mode 是 0777 (八进制)。 |
  | 36   | [os.mkfifo(path[, mode\])](https://www.runoob.com/python3/python3-os-mkfifo.html) 创建命名管道，mode 为数字，默认为 0666 (八进制) |
  | 37   | [os.mknod(filename[, mode=0600, device\])](https://www.runoob.com/python3/python3-os-mknod.html) 创建一个名为filename文件系统节点（文件，设备特别文件或者命名pipe）。 |
  | 38   | [os.open(file, flags[, mode\])](https://www.runoob.com/python3/python3-os-open.html) 打开一个文件，并且设置需要的打开选项，mode参数是可选的 |
  | 39   | [os.openpty()](https://www.runoob.com/python3/python3-os-openpty.html) 打开一个新的伪终端对。返回 pty 和 tty的文件描述符。 |
  | 40   | [os.pathconf(path, name)](https://www.runoob.com/python3/python3-os-pathconf.html) 返回相关文件的系统配置信息。 |
  | 41   | [os.pipe()](https://www.runoob.com/python3/python3-os-pipe.html) 创建一个管道. 返回一对文件描述符(r, w) 分别为读和写 |
  | 42   | [os.popen(command[, mode[, bufsize\]])](https://www.runoob.com/python3/python3-os-popen.html) 从一个 command 打开一个管道 |
  | 43   | [os.read(fd, n)](https://www.runoob.com/python3/python3-os-read.html) 从文件描述符 fd 中读取最多 n 个字节，返回包含读取字节的字符串，文件描述符 fd对应文件已达到结尾, 返回一个空字符串。 |
  | 44   | [os.readlink(path)](https://www.runoob.com/python3/python3-os-readlink.html) 返回软链接所指向的文件 |
  | 45   | [os.remove(path)](https://www.runoob.com/python3/python3-os-remove.html) 删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory。 |
  | 46   | [os.removedirs(path)](https://www.runoob.com/python3/python3-os-removedirs.html) 递归删除目录。 |
  | 47   | [os.rename(src, dst)](https://www.runoob.com/python3/python3-os-rename.html) 重命名文件或目录，从 src 到 dst |
  | 48   | [os.renames(old, new)](https://www.runoob.com/python3/python3-os-renames.html) 递归地对目录进行更名，也可以对文件进行更名。 |
  | 49   | [os.rmdir(path)](https://www.runoob.com/python3/python3-os-rmdir.html) 删除path指定的空目录，如果目录非空，则抛出一个OSError异常。 |
  | 50   | [os.stat(path)](https://www.runoob.com/python3/python3-os-stat.html) 获取path指定的路径的信息，功能等同于C API中的stat()系统调用。 |
  | 51   | [os.stat_float_times([newvalue\])](https://www.runoob.com/python3/python3-os-stat_float_times.html) 决定stat_result是否以float对象显示时间戳 |
  | 52   | [os.statvfs(path)](https://www.runoob.com/python3/python3-os-statvfs.html) 获取指定路径的文件系统统计信息 |
  | 53   | [os.symlink(src, dst)](https://www.runoob.com/python3/python3-os-symlink.html) 创建一个软链接 |
  | 54   | [os.tcgetpgrp(fd)](https://www.runoob.com/python3/python3-os-tcgetpgrp.html) 返回与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组 |
  | 55   | [os.tcsetpgrp(fd, pg)](https://www.runoob.com/python3/python3-os-tcsetpgrp.html) 设置与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组为pg。 |
  | 56   | os.tempnam([dir[, prefix]]) **Python3 中已删除。**返回唯一的路径名用于创建临时文件。 |
  | 57   | os.tmpfile() **Python3 中已删除。**返回一个打开的模式为(w+b)的文件对象 .这文件对象没有文件夹入口，没有文件描述符，将会自动删除。 |
  | 58   | os.tmpnam() **Python3 中已删除。**为创建一个临时文件返回一个唯一的路径 |
  | 59   | [os.ttyname(fd)](https://www.runoob.com/python3/python3-os-ttyname.html) 返回一个字符串，它表示与文件描述符fd 关联的终端设备。如果fd 没有与终端设备关联，则引发一个异常。 |
  | 60   | [os.unlink(path)](https://www.runoob.com/python3/python3-os-unlink.html) 删除文件路径 |
  | 61   | [os.utime(path, times)](https://www.runoob.com/python3/python3-os-utime.html) 返回指定的path文件的访问和修改的时间。 |
  | 62   | os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])                                                                                         输出在文件夹中的文件名通过在树中游走，向上或者向下。 |
  | 63   | [os.write(fd, str)](https://www.runoob.com/python3/python3-os-write.html) 写入字符串到文件描述符 fd中. 返回实际写入的字符串长度 |
  | 64   | [os.path 模块](https://www.runoob.com/python3/python3-os-path.html) 获取文件的属性信息。 |
  | 65   | [os.pardir()](https://www.runoob.com/python3/python3-os-pardir.html) 获取当前目录的父目录，以字符串形式显示目录名。 |

## 11. 错误和异常

### 11.1 语法错误

+ Python 的语法错误或者称之为解析错

#### 实例：语法错误

+ ```python
  >>> while True print('Hello world')
    File "<stdin>", line 1, in ?
      while True print('Hello world')
                     ^
  SyntaxError: invalid syntax
  ```

### 11.2 异常

+ 即便 Python 程序的语法是正确的，在运行它的时候，也有可能发生错误。运行期检测到的错误被称为异常。

#### 实例：大多数的异常都不会被程序处理，而是以错误信息的形式展现

+ ```python
  >>> 10 * (1/0)             # 0 不能作为除数，触发异常
  Traceback (most recent call last):
    File "<stdin>", line 1, in ?
  ZeroDivisionError: division by zero
  >>> 4 + spam*3             # spam 未定义，触发异常
  Traceback (most recent call last):
    File "<stdin>", line 1, in ?
  NameError: name 'spam' is not defined
  >>> '2' + 2               # int 不能与 str 相加，触发异常
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: can only concatenate str (not "int") to str
      
  # 异常以不同的类型出现，这些类型都作为信息的一部分打印出来: 
  # 例子中的类型有 ZeroDivisionError，NameError 和 TypeError。
  # 错误信息的前面部分显示了异常发生的上下文，并以调用栈的形式显示具体信息。
  ```

### 11.3 异常处理

#### 异常处理语句概述

+ try: 执行代码
+ except: 发生异常时执行的代码
+ else: 没有异常时执行的代码
+ finally: 不管有无异常都会执行的代码

#### try/except

+ 异常捕捉可以使用 **try/except** 语句。

##### try 语句的工作方式

+ 首先，执行 try 子句（在关键字 try 和关键字 except 之间的语句）。
+ 如果没有异常发生，忽略 except 子句，try 子句执行后结束。
+ 如果在执行 try 子句的过程中发生了异常，那么 try 子句余下的部分将被忽略。如果异常的类型和 except 之后的名称相符，那么对应的 except 子句将被执行。
+ 如果一个异常没有与任何的 except 匹配，那么这个异常将会传递给上层的 try 中。

##### 注意

+ 一个 try 语句可能包含多个except子句，分别来处理不同的特定的异常。最多只有一个分支会被执行。
+ 处理程序将只针对对应的 try 子句中的异常进行处理，而不是其他的 try 的处理程序中的异常。

##### 实例1：使用 **try/except** 语句

+ ```python
  # 以下例子中，让用户输入一个合法的整数，但是允许用户中断这个程序（使用 Control-C 或者操作系统提供的方法）。用户中断的信息会引发一个 KeyboardInterrupt 异常。
  
  while True:
      try:
          x = int(input("请输入一个数字: "))
          break
      except ValueError:
          print("您输入的不是数字，请再次尝试输入！")
  ```

##### 实例2：一个except子句可以同时处理多个异常，这些异常将被放在一个括号里成为一个元组

+ ```python
  except (RuntimeError, TypeError, NameError):
      pass
  ```

##### 实例3：最后一个except子句可以忽略异常的名称，它将被当作通配符使用。你可以使用这种方法打印一个错误信息，然后再次把异常抛出。

+ ```python
  import sys
  
  try:
      f = open('myfile.txt')
      s = f.readline()
      i = int(s.strip())
  except OSError as err:
      print("OS error: {0}".format(err))
  except ValueError:
      print("Could not convert data to an integer.")
  except:
      print("Unexpected error:", sys.exc_info()[0])
      raise
  ```

#### try/except...else

+ **try/except** 语句还有一个可选的 **else** 子句，如果使用这个子句，那么必须放在所有的 except 子句之后。
+ else 子句将在 try 子句没有发生任何异常的时候执行。

##### else 子句的好处

+ 使用 else 子句比把所有的语句都放在 try 子句里面要好，这样可以避免一些意想不到，而 except 又无法捕获的异常。

##### 实例1：在 try 语句中判断文件是否可以打开，如果打开文件时正常的没有发生异常则执行 else 部分的语句，读取文件内容

+ ```python
  import sys
  
  for arg in sys.argv[1:]:
      try:
          f = open(arg, 'r')
      except IOError:
          print('cannot open', arg)
      else:
          print(arg, 'has', len(f.readlines()), 'lines')
          f.close()
  ```

##### 实例2：异常处理能处理子句中调用的函数（甚至间接调用的函数）里抛出的异常。

+ ```python
  >>> def this_fails():
          x = 1/0
     
  >>> try:
          this_fails()
      except ZeroDivisionError as err:
          print('Handling run-time error:', err)
  
  # error output
  '''
  Handling run-time error: int division or modulo by zero
  '''
  ```

#### try-finally 语句

+ try-finally 语句无论是否发生异常都将执行最后的代码。

##### 实例： finally 语句无论异常是否发生都会执行

+ ```python
  try:
      runoob()
  except AssertionError as error:
      print(error)
  else:
      try:
          with open('file.log') as file:
              read_data = file.read()
      except FileNotFoundError as fnf_error:
          print(fnf_error)
  finally:
      print('这句话，无论异常是否发生都会执行。')
  ```

### 11.4 抛出异常

+ Python 使用 raise 语句抛出一个指定的异常。
+ raise 后面只能跟一个异常的实例或者是异常的类（也就是 Exception 的子类）。

#### raise语法格式

```python
raise [Exception [, args [, traceback]]]
```

#### 实例1：如果 x 大于 5 就触发异常

+ ```python
  # 执行该代码会触发异常：
  x = 10
  if x > 5:
      raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
      
  # output
  '''
  Traceback (most recent call last):
    File "test.py", line 3, in <module>
      raise Exception('x 不能大于 5。x 的值为: {}'.format(x))
  Exception: x 不能大于 5。x 的值为: 10
  '''
  ```

#### 实例2：try语句有语法错误时不会抛出异常，这时候可以在except中使用一个简单的 raise 语句就可以再次把它抛出。

+ ```python
  >>> try:
          raise NameError('HiThere')
      except NameError:
          print('An exception flew by!')
          raise
     
  # error
  An exception flew by!
  Traceback (most recent call last):
    File "<stdin>", line 2, in ?
  NameError: HiThere
  ```

### 11.5 用户自定义异常

+ 可以通过创建一个新的异常类来自定义异常。
+ 异常类继承自 Exception 类，可以直接继承，或者间接继承。

#### 实例1：自定义异常，类 Exception 默认的 __init__() 被覆盖

+ ```python
  >>> class MyError(Exception):
          def __init__(self, value):
              self.value = value
          def __str__(self):
              return repr(self.value)
     
  >>> try:
          raise MyError(2*2)
      except MyError as e:
          print('My exception occurred, value:', e.value)
  
  # error
  My exception occurred, value: 4
  >>> raise MyError('oops!')
  Traceback (most recent call last):
    File "<stdin>", line 1, in ?
  __main__.MyError: 'oops!'
  ```

#### 实例2：先创建一个基础异常类，然后基于这个基础类为不同的错误情况创建不同的子类

+ 当创建一个模块有可能抛出多种不同的异常时，一种通常的做法是为这个包建立一个基础异常类，然后基于这个基础类为不同的错误情况创建不同的子类

+ ```python
  class Error(Exception):
      """Base class for exceptions in this module."""
      pass
  
  class InputError(Error):
      """Exception raised for errors in the input.
  
      Attributes:
          expression -- input expression in which the error occurred
          message -- explanation of the error
      """
  
      def __init__(self, expression, message):
          self.expression = expression
          self.message = message
  
  class TransitionError(Error):
      """Raised when an operation attempts a state transition that's not
      allowed.
  
      Attributes:
          previous -- state at beginning of transition
          next -- attempted new state
          message -- explanation of why the specific transition is not allowed
      """
  
      def __init__(self, previous, next, message):
          self.previous = previous
          self.next = next
          self.message = message
  ```

### 11.6 定义清理行为

+ 可以通过finally语句执行清理行为

#### 如何执行清理行为

+ 如果一个异常在 try 子句里（或者在 except 和 else 子句里）被抛出，而又没有任何的 except 把它截住，那么这个异常会在 finally 子句执行后被抛出。

#### 实例1：try 子句里面有没有发生异常，finally 子句都会执行。

+ ```python
  >>> try:
  ...     raise KeyboardInterrupt
  ... finally:
  ...     print('Goodbye, world!')
  ...
  Goodbye, world!
  Traceback (most recent call last):
    File "<stdin>", line 2, in <module>
  KeyboardInterrupt
  ```

#### 实例2：在同一个 try 语句里包含 except 和 finally 子句

+ ```python
  >>> def divide(x, y):
          try:
              result = x / y
          except ZeroDivisionError:
              print("division by zero!")
          else:
              print("result is", result)
          finally:
              print("executing finally clause")
     
  >>> divide(2, 1)
  result is 2.0
  executing finally clause
  >>> divide(2, 0)
  division by zero!
  executing finally clause
  >>> divide("2", "1")
  executing finally clause
  Traceback (most recent call last):
    File "<stdin>", line 1, in ?
    File "<stdin>", line 3, in divide
  TypeError: unsupported operand type(s) for /: 'str' and 'str'
  ```

### 11.7 预定义的清理行为

+ 一些对象定义了标准的清理行为，无论系统是否成功的使用了它，一旦不需要它了，那么这个标准的清理行为就会执行。

#### 如何实现预定义的清理行为

+ 关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法

#### 实例：尝试打开一个文件，然后把内容打印到屏幕上

+ ```python
  for line in open("myfile.txt"):
      print(line, end="")
  # 以上这段代码的问题是，当执行完毕后，文件会保持打开状态，并没有被关闭。
  
  with open("myfile.txt") as f:
      for line in f:
          print(line, end="")
  # 以上这段代码执行完毕后，就算在处理过程中出问题了，文件 f 总是会关闭。
  ```

## 12. 面向对象

+ Python中的类提供了面向对象编程的所有基本功能：类的继承机制允许多个基类，派生类可以覆盖基类中的任何方法，方法中可以调用基类中的同名方法。
+ 对象可以包含任意数量和类型的数据。

### 12.1 面向对象技术简介

+ **类(Class):** 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
+ **方法：**类中定义的函数。
+ **类变量：**类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
+ **数据成员：**类变量或者实例变量用于处理类及其实例对象的相关的数据。
+ **方法重写：**如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
+ **局部变量：**定义在方法中的变量，只作用于当前实例的类。
+ **实例变量：**在类的声明中，属性是用变量来表示的，这种变量就称为实例变量，实例变量就是一个用 self 修饰的变量。
+ **继承：**即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
+ **实例化：**创建一个类的实例，类的具体对象。
+ **对象：**通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

### 12.2 类定义

#### 语法格式

+ ```python
  class ClassName:
      <statement-1>
      .
      .
      .
      <statement-N>
  ```

+ 类**实例化后**，可以使用其属性，实际上，创建一个类之后，可以通过类名访问其属性。

### 12.3 类对象

#### 类对象支持两种操作

+ 属性引用
  + 属性引用使用和 Python 中所有的属性引用一样的标准语法：**obj.name**。
+ 实例化

##### 实例1：创建了一个新的类实例并将该对象赋给局部变量 x，x 为空的对象。

+ ```python
  #!/usr/bin/python3
   
  class MyClass:
      """一个简单的类实例"""
      i = 12345
      def f(self):
          return 'hello world'
   
  # 实例化类
  x = MyClass()
   
  # 访问类的属性和方法
  print("MyClass 类的属性 i 为：", x.i)
  print("MyClass 类的方法 f 输出为：", x.f())
  
  
  # output
  '''
  MyClass 类的属性 i 为： 12345
  MyClass 类的方法 f 输出为： hello world
  '''
  ```

##### 实例2：类的__init()__方法

+ ```python
  # 类有一个名为 __init__() 的特殊方法（构造方法），该方法在类实例化时会自动调用
  def __init__(self):
      self.data = []
      
  # 类定义了 __init__() 方法，类的实例化操作会自动调用 __init__() 方法。如下实例化类 MyClass，对应的 __init__() 方法就会被调用:
  class MyClass:
      def __init__():
          pass
  
  x = MyClass()
  
  # __init__() 方法可以有参数，参数通过 __init__() 传递到类的实例化操作上。
  class Complex:
      def __init__(self, realpart, imagpart):
          self.r = realpart
          self.i = imagpart
          
  x = Complex(3.0, -4.5)
  print(x.r, x.i)   # 输出结果：3.0 -4.5
  ```

#### self 代表类的实例，而非类

+ 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的**第一个参数名称**, 按照惯例它的名称是 self。

##### 实例1：类的方法的第一个参数名称

+ ```python
  class Test:
      def prt(self):
          print(self)
          print(self.__class__)
   
  t = Test()
  t.prt()
  
  
  # output
  '''
  <__main__.Test instance at 0x100771878>
  __main__.Test
  '''
  # 从执行结果可以很明显的看出，self 代表的是类的实例，代表当前对象的地址，而 self.class 则指向类。
  ```

##### 实例2：self 不是 python 关键字，我们把他换成 runoob 也是可以正常执行的

+ ```python
  class Test:
      def prt(runoob):
          print(runoob)
          print(runoob.__class__)
   
  t = Test()
  t.prt()
  
  
  # output
  '''
  <__main__.Test instance at 0x100771878>
  __main__.Test
  '''
  ```

### 12.4 类的方法

+ 在类的内部，使用 **def** 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self, 且为第一个参数，self 代表的是类的实例。

#### 实例：写一个类的方法并调用（包含如何定义私有属性）

+ ```python
  #!/usr/bin/python3
   
  #类定义
  class people:
      #定义基本属性
      name = ''
      age = 0
      #定义私有属性,私有属性在类外部无法直接进行访问
      __weight = 0
      #定义构造方法
      def __init__(self,n,a,w):
          self.name = n
          self.age = a
          self.__weight = w
      def speak(self):
          print("%s 说: 我 %d 岁。" %(self.name,self.age))
   
  # 实例化类
  p = people('runoob',10,30)
  p.speak()
  
  
  # output
  '''
  runoob 说: 我 10 岁。
  '''
  ```

### 12.5 继承

+ Python 同样支持类的继承，如果一种语言不支持继承，类就没有什么意义。

#### 实例1：派生类的定义

+ ```python
  class DerivedClassName(BaseClassName1):
      <statement-1>
      .
      .
      .
      <statement-N>
      
  # BaseClassName（示例中的基类名）必须与派生类定义在一个作用域内。除了类，还可以用表达式，基类定义在另一个模块中时这一点非常有用:
  class DerivedClassName(modname.BaseClassName):
  ```

#### 实例2：子类继承父类并重写方法

+ ```python
  #!/usr/bin/python3
   
  #类定义
  class people:
      #定义基本属性
      name = ''
      age = 0
      #定义私有属性,私有属性在类外部无法直接进行访问
      __weight = 0
      #定义构造方法
      def __init__(self,n,a,w):
          self.name = n
          self.age = a
          self.__weight = w
      def speak(self):
          print("%s 说: 我 %d 岁。" %(self.name,self.age))
   
  #单继承示例
  class student(people):
      grade = ''
      def __init__(self,n,a,w,g):
          #调用父类的构函
          people.__init__(self,n,a,w)
          self.grade = g
      #覆写父类的方法
      def speak(self):
          print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
   
   
   
  s = student('ken',10,60,3)
  s.speak()
  
  
  # output
  '''
  ken 说: 我 10 岁了，我在读 3 年级
  '''
  ```

### 12.6 多继承

#### 实例1：多继承类的定义

+ ```python
  class DerivedClassName(Base1, Base2, Base3):
      <statement-1>
      .
      .
      .
      <statement-N>
      
  ```

+ 需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法。

#### 实例2：多重继承

+ ```python
  #!/usr/bin/python3
   
  #类定义
  class people:
      #定义基本属性
      name = ''
      age = 0
      #定义私有属性,私有属性在类外部无法直接进行访问
      __weight = 0
      #定义构造方法
      def __init__(self,n,a,w):
          self.name = n
          self.age = a
          self.__weight = w
      def speak(self):
          print("%s 说: 我 %d 岁。" %(self.name,self.age))
   
  #单继承示例
  class student(people):
      grade = ''
      def __init__(self,n,a,w,g):
          #调用父类的构函
          people.__init__(self,n,a,w)
          self.grade = g
      #覆写父类的方法
      def speak(self):
          print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
   
  #另一个类，多重继承之前的准备
  class speaker():
      topic = ''
      name = ''
      def __init__(self,n,t):
          self.name = n
          self.topic = t
      def speak(self):
          print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))
   
  #多重继承
  class sample(speaker,student):
      a =''
      def __init__(self,n,a,w,g,t):
          student.__init__(self,n,a,w,g)
          speaker.__init__(self,n,t)
   
  test = sample("Tim",25,80,4,"Python")
  test.speak()   #方法名同，默认调用的是在括号中排前地父类的方法
  
  
  # output
  '''
  我叫 Tim，我是一个演说家，我演讲的主4题是 Python
  '''
  ```

### 12.7 方法重写

#### 实例：如果父类方法的功能不能满足需求，可以在子类重写你父类的方法

+ ```python
  #!/usr/bin/python3
   
  class Parent:        # 定义父类
     def myMethod(self):
        print ('调用父类方法')
   
  class Child(Parent): # 定义子类
     def myMethod(self):
        print ('调用子类方法')
   
  c = Child()          # 子类实例
  c.myMethod()         # 子类调用重写方法
  super(Child,c).myMethod() #用子类对象调用父类已被覆盖的方法
  
  # super() 函数是用于调用父类(超类)的一个方法。
  
  # output
  '''
  调用子类方法
  调用父类方法
  '''
  ```

### 12.8 类属性与方法

#### 类的私有属性

+ **__private_attrs**：两个下划线开头，声明该属性为私有，不能在类的外部被使用或直接访问。在类内部的方法中使用时 **self.__private_attrs**。

##### 实例：类的私有属性

+ ```python
  #!/usr/bin/python3
   
  class JustCounter:
      __secretCount = 0  # 私有变量
      publicCount = 0    # 公开变量
   
      def count(self):
          self.__secretCount += 1
          self.publicCount += 1
          print (self.__secretCount)
   
  counter = JustCounter()
  counter.count()
  counter.count()
  print (counter.publicCount)
  print (counter.__secretCount)  # 报错，实例不能访问私有变量
  
  
  # output
  '''
  1
  2
  2
  Traceback (most recent call last):
    File "test.py", line 16, in <module>
      print (counter.__secretCount)  # 报错，实例不能访问私有变量
  AttributeError: 'JustCounter' object has no attribute '__secretCount'
  '''
  ```

#### 类的方法

+ 在类的内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 **self**，且为第一个参数，**self** 代表的是类的实例。
+ **self** 的名字并不是规定死的，也可以使用 **this**，但是最好还是按照约定是用 **self**。

#### 类的私有方法

+ **__private_method**：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，不能在类的外部调用。**self.__private_methods**。

##### 实例：类的私有方法

+ ```python
  #!/usr/bin/python3
   
  class Site:
      def __init__(self, name, url):
          self.name = name       # public
          self.__url = url   # private
   
      def who(self):
          print('name  : ', self.name)
          print('url : ', self.__url)
   
      def __foo(self):          # 私有方法
          print('这是私有方法')
   
      def foo(self):            # 公共方法
          print('这是公共方法')
          self.__foo()
   
  x = Site('菜鸟教程', 'www.runoob.com')
  x.who()        # 正常输出
  x.foo()        # 正常输出
  x.__foo()      # 报错
  
  
  # output
  '''
  name  :  菜鸟教程
  url :  www.runoob.com
  这是公共方法
  这是私有方法
  Traceback (most recent call last):
    File "C:/Users/87143/Desktop/Python/Python源码/test.py", line 31, in <module>
      x.__foo()  # 报错
  AttributeError: 'Site' object has no attribute '__foo'
  '''
  ```

#### * 类的专有方法

+ **__init__ :** 构造函数，在生成对象时调用
+ **__del__ :** 析构函数，释放对象时使用
+ **__repr__ :** 打印，转换
+ **__setitem__ :** 按照索引赋值
+ **__getitem__:** 按照索引获取值
+ **__len__:** 获得长度
+ **__cmp__:** 比较运算
+ **__call__:** 函数调用
+ **__add__:** 加运算
+ **__sub__:** 减运算
+ **__mul__:** 乘运算
+ **__truediv__:** 除运算
+ **__mod__:** 求余运算
+ **__pow__:** 乘方

#### 运算符重载

##### 实例：Python支持运算符重载，我们可以对类的专有方法进行重载

+ ```python
  #!/usr/bin/python3
   
  class Vector:
     def __init__(self, a, b):
        self.a = a
        self.b = b
   
     def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)
     
     def __add__(self,other):
        return Vector(self.a + other.a, self.b + other.b)
   
  v1 = Vector(2,10)
  v2 = Vector(5,-2)
  print (v1 + v2)
  
  # output
  '''
  Vector(7,8)
  '''
  ```

## 13. 命名空间和作用域

### 13.1 命名空间

#### 什么是命名空间

+ 命名空间(Namespace)是从名称到对象的映射，大部分的命名空间都是通过 Python 字典来实现的。
+ 命名空间提供了在项目中避免名字冲突的一种方法。各个命名空间是独立的，没有任何关系的，所以一个命名空间中不能有重名，但不同的命名空间是可以重名而没有任何影响。
  +  例如：一个文件夹(目录)中可以包含多个文件夹，每个文件夹中不能有相同的文件名，但不同文件夹中的文件可以重名。

#### 三种命名空间

+ **内置名称（built-in names**）， Python 语言内置的名称，比如函数名 abs、char 和异常名称 BaseException、Exception 等等。
+ **全局名称（global names）**，模块中定义的名称，记录了模块的变量，包括函数、类、其它导入的模块、模块级的变量和常量。
+ **局部名称（local names）**，函数中定义的名称，记录了函数的变量，包括函数的参数和局部定义的变量。（类中定义的也是）

#### 命名空间查找顺序

+ 假设我们要使用变量 runoob，则 Python 的查找顺序为：**局部的命名空间去 -> 全局命名空间 -> 内置命名空间**。

  + 如果找不到变量 runoob，它将放弃查找并引发一个 NameError 异常:

  + ```python
    NameError: name 'runoob' is not defined。
    ```

#### 命名空间的生命周期

+ 命名空间的生命周期取决于对象的作用域，如果对象执行完成，则该命名空间的生命周期就结束。

  + 因此，我们无法从外部命名空间访问内部命名空间的对象

  + ```python
    # var1 是全局名称
    var1 = 5
    def some_func():
     
        # var2 是局部名称
        var2 = 6
        def some_inner_func():
     
            # var3 是内嵌的局部名称
            var3 = 7
    ```

### 13.2 作用域

#### 什么是作用域

+ 作用域就是一个 Python 程序可以直接访问命名空间的正文区域。
+ 在一个 python 程序中，直接访问一个变量，会从内到外依次访问所有的作用域直到找到，否则会报未定义的错误。
+ Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。

#### 四种作用域

+ **L（Local）**：最内层，包含局部变量，比如一个函数/方法内部。
+ **E（Enclosing）**：包含了非局部(non-local)也非全局(non-global)的变量。比如两个嵌套函数，一个函数（或类） A 里面又包含了一个函数 B ，那么对于 B 中的名称来说 A 中的作用域就为 non-local。
+ **G（Global）**：当前脚本的最外层，比如当前模块的全局变量。
+ **B（Built-in）**： 包含了内建的变量/关键字等，最后被搜索。

##### 规则顺序

+ **L –> E –> G –>B**。
+ 在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内置中找。
+ ![img](https://www.runoob.com/wp-content/uploads/2014/05/1418490-20180906153626089-1835444372.png)

#### 查看内置作用域

+ 内置作用域是通过一个名为 builtin 的标准模块来实现的，但是这个变量名自身并没有放入内置作用域内，所以必须导入这个文件才能够使用它。

+ ```python
  >>> import builtins
  >>> dir(builtins)
  ```

#### 不会引入新作用域的语句块

+ Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域

+ 其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问。

+ ```python
  >>> if True:
  ...  msg = 'I am from Runoob'
  ... 
  >>> msg
  'I am from Runoob'
  >>> 
  ```

#### 实例：不同作用域下的变量

+ ```python
  g_count = 0  # 全局作用域
  def outer():
      o_count = 1  # 闭包函数外的函数中
      def inner():
          i_count = 2  # 局部作用域
          
          
  # 如果将变量 msg 定义在函数中，则它就是局部变量，外部不能访问
  def test():
  	msg_inner = 'I am from Runoob'
      
  print(msg_inner)
  
  # output（从报错的信息上看，说明了 msg_inner 未定义，无法使用，因为它是局部变量，只有在函数内可以使用。）
  '''
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  NameError: name 'msg_inner' is not defined
  '''
  ```

### 13.3 全局变量和局部变量

+ 定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
+ 局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。

#### 实例：调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。

+ ```python
  #!/usr/bin/python3
   
  total = 0 # 这是一个全局变量
  # 可写函数说明
  def sum( arg1, arg2 ):
      #返回2个参数的和."
      total = arg1 + arg2 # total在这里是局部变量.
      print ("函数内是局部变量 : ", total)
      return total
   
  #调用sum函数
  sum( 10, 20 )
  print ("函数外是全局变量 : ", total)
  
  
  # output
  '''
  函数内是局部变量 :  30
  函数外是全局变量 :  0
  '''
  ```

### 13.4 global 和 nonlocal 关键字

+ 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。

#### 实例1：修改全局变量num

+ ```python
  #!/usr/bin/python3
   
  num = 1
  def fun1():
      global num  # 需要使用 global 关键字声明
      print(num) 
      num = 123
      print(num)
  fun1()
  print(num)
  
  
  # output
  '''
  1
  123
  123
  '''
  ```

#### 实例2：使用 nonlocal 关键字修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量。

+ ```python
  #!/usr/bin/python3
   
  def outer():
      num = 10
      def inner():
          nonlocal num   # nonlocal关键字声明
          num = 100
          print(num)
      inner()
      print(num)
  outer()
  
  
  # output
  '''
  100
  100
  '''
  ```

#### 实例3：特殊情况局部变量和全局变量重名

+ 这种情况看作用域顺序：**L –> E –> G –>B**。

+ ```python
  #!/usr/bin/python3
   
  a = 10
  def test():
      a = a + 1
      print(a)
  test()
  
  # error
  # 错误信息为局部作用域引用错误，因为 test 函数中的 a 使用的是局部，未定义，无法修改。
  '''
  Traceback (most recent call last):
    File "test.py", line 7, in <module>
      test()
    File "test.py", line 5, in test
      a = a + 1
  UnboundLocalError: local variable 'a' referenced before assignment
  '''
  
  # 修改 a 为全局变量
   
  a = 10
  def test():
      global a
      a = a + 1
      print(a)
  test()
  
  # output
  '''
  11
  '''
  
  
  # 也可以通过函数参数传递
  
  a = 10
  def test(a):
      a = a + 1
      print(a)
  test(a)
  
  # output
  '''
  11
  '''
  ```

## 14. 标准库概览

### 14.1 操作系统接口

#### os 模块

+ os模块提供了不少与操作系统相关联的函数
+ 使用 "import os" 风格而非 "from os import *"。
  + 这样可以保证随操作系统不同而有所变化的 os.open() 不会覆盖内置函数 open()。

##### 实例1：使用os模块

+ ```python
  >>> import os
  >>> os.getcwd()      # 返回当前的工作目录
  'C:\\Python34'
  >>> os.chdir('/server/accesslogs')   # 修改当前的工作目录
  >>> os.system('mkdir today')   # 执行系统命令 mkdir 
  0
  ```

##### 实例2：使用 os 这样的大型模块时内置的 dir() 和 help() 函数非常有用

+ ```python
  >>> import os
  >>> dir(os)
  <returns a list of all module functions>
  >>> help(os)
  <returns an extensive manual page created from the module's docstrings>
  ```

#### shutil 模块

##### 实例：针对日常的文件和目录管理任务，shutil 模块提供了一个易于使用的高级接口

+ ```python
  >>> import shutil
  >>> shutil.copyfile('data.db', 'archive.db')
  >>> shutil.move('/build/executables', 'installdir')
  ```

### 14.2 文件通配符

#### 实例：glob模块提供了一个函数用于从目录通配符搜索中生成文件列表

+ ```python
  >>> import glob
  >>> glob.glob('*.py')
  ['primes.py', 'random.py', 'quote.py']
  ```

### 14.3 命令行参数

+ 通用工具脚本经常调用命令行参数。
+ 这些命令行参数以链表形式存储于 sys 模块的 argv 变量。

#### 实例：在命令行中执行 "python demo.py one two three" 后可以得到以下输出结果

+ ```python
  >>> import sys
  >>> print(sys.argv)
  ['demo.py', 'one', 'two', 'three']
  ```

### 14.4 错误输出重定向和程序终止

#### 实例1：错误输出重定向

+ ```python
  >>> sys.stderr.write('Warning, log file not found starting a new one\n')
  Warning, log file not found starting a new one
  ```

#### 实例2：程序终止

+ ```python
  >>> sys.exit()
  ```

### 14.5 字符串正则匹配

+ re模块为高级字符串处理提供了正则表达式工具。对于复杂的匹配和处理，正则表达式提供了简洁、优化的解决方案:

#### 实例1：使用re模块

+ ```python
  >>> import re
  >>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
  ['foot', 'fell', 'fastest']
  >>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
  'cat in the hat'
  ```

#### 实例2：使用字符串内置函数

+ 如果只需要简单的功能，应该首先考虑字符串方法，因为它们非常简单，易于阅读和调试:

+ ```python
  >>> 'tea for too'.replace('too', 'two')
  'tea for two'
  ```

### 14.6 数学相关模块

#### 实例1：math模块为浮点运算提供了对底层C函数库的访问

+ ```python
  >>> import math
  >>> math.cos(math.pi / 4)
  0.70710678118654757
  >>> math.log(1024, 2)
  10.0
  ```

#### 实例2：random提供了生成随机数的工具。

+ ```python
  >>> import random
  >>> random.choice(['apple', 'pear', 'banana'])
  'apple'
  >>> random.sample(range(100), 10)   # sampling without replacement
  [30, 83, 16, 4, 8, 81, 41, 50, 18, 33]
  >>> random.random()    # random float
  0.17970987693706186
  >>> random.randrange(6)    # random integer chosen from range(6)
  4
  ```

### 14.7 访问互联网

#### 实例1：使用 urllib 模块的 request() 方法处理从网站接收的数据

+ ```python
  >>> from urllib.request import urlopen
  >>> for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
  ...     line = line.decode('utf-8')  # Decoding the binary data to text.
  ...     if 'EST' in line or 'EDT' in line:  # look for Eastern Time
  ...         print(line)
  ```

#### 实例2：使用 smtplib 模块发送电子邮件

+ ```python
  >>> import smtplib
  >>> server = smtplib.SMTP('localhost')  # 这里需要本地有一个在运行的邮件服务器。
  >>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
  ... """To: jcaesar@example.org
  ... From: soothsayer@example.org
  ...
  ... Beware the Ides of March.
  ... """)
  >>> server.quit()
  ```

### 14.8 日期和时间

+ datetime模块为日期和时间处理同时提供了简单和复杂的方法。
  + 支持日期和时间算法的同时，实现的重点放在更有效的处理和格式化输出。
  + 该模块还支持时区处理
+ 常用时间处理方法
  - 今天 `today = datetime.date.today()`
  - 昨天 `yesterday = today - datetime.timedelta(days=1)`
  - 上个月 `last_month = today.month - 1 if today.month - 1 else 12`
  - 当前时间戳 `time_stamp = time.time()`
  - 时间戳转datetime `datetime.datetime.fromtimestamp(time_stamp)`
  - datetime转时间戳 `int(time.mktime(today.timetuple()))`
  - datetime转字符串 `today_str = today.strftime("%Y-%m-%d")`
  - 字符串转datetime `today = datetime.datetime.strptime(today_str, "%Y-%m-%d")`
  - 补时差 `today + datetime.timedelta(hours=8)`

#### 实例：date对象常用方法

+ ```python
  >>> # dates are easily constructed and formatted
  >>> from datetime import date
  >>> now = date.today()
  >>> now
  datetime.date(2003, 12, 2)
  >>> now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")
  '12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'
  
  >>> # dates support calendar arithmetic  date对象支持日历算法
  >>> birthday = date(1964, 7, 31)
  >>> age = now - birthday
  >>> age.days
  14368
  ```

### 14.9 数据压缩

+ 以下模块直接支持通用的数据打包和压缩格式：zlib，gzip，bz2，zipfile，以及 tarfile。

#### 实例：使用zlib模块打包数据

+ ```python
  >>> import zlib
  >>> s = b'witch which has which witches wrist watch'
  >>> len(s)
  41
  >>> t = zlib.compress(s)
  >>> len(t)
  37
  >>> zlib.decompress(t)
  b'witch which has which witches wrist watch'
  >>> zlib.crc32(s)
  226805979
  ```

### 14.10 性能度量

+ 使用 timeit 模块测试不同方法之间的性能差异

#### 实例：使用元组封装和拆封来交换元素 VS 传统方法。

+ ```python
  >>> from timeit import Timer
  >>> Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
  0.57535828626024577
  >>> Timer('a,b = b,a', 'a=1; b=2').timeit()
  0.54962537085770791
  ```

#### 补充

+ 相对于 timeit 的细粒度，profile 和 pstats 模块提供了针对更大代码块的时间度量工具。

### 14.11 测试模块

+ 开发高质量软件的方法之一是为每一个函数开发测试代码，并且在开发过程中经常进行测试
+ doctest 模块提供了一个工具，扫描模块并根据程序中内嵌的文档字符串执行测试。
+ 测试构造如同简单的将它的输出结果剪切并粘贴到文档字符串中。

#### 实例1：通过用户提供的例子，它强化了文档，允许 doctest 模块确认代码的结果是否与文档一致

+ ```python
  def average(values):
      """Computes the arithmetic mean of a list of numbers.
  
      >>> print(average([20, 30, 70]))
      40.0
      """
      return sum(values) / len(values)
  
  import doctest
  doctest.testmod()   # 自动验证嵌入测试
  ```

#### 实例2：unittest模块不像 doctest模块那么容易使用，不过它可以在一个独立的文件里提供一个更全面的测试集

+ ```python
  import unittest
  
  class TestStatisticalFunctions(unittest.TestCase):
  
      def test_average(self):
          self.assertEqual(average([20, 30, 70]), 40.0)
          self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
          self.assertRaises(ZeroDivisionError, average, [])
          self.assertRaises(TypeError, average, 20, 30, 70)
  
  unittest.main() # Calling from the command line invokes all tests
  ```

