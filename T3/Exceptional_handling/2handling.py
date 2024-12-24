# # IMP MCQ
# def f():
#     try:
#         print('1')
#         return 'vishal9'
#     finally:
#         print('2')
#         return 'vishal10' #priority return of finally
# print(f())



# #Possibility combination you can use
# try-finally
# try-Except
# try-except-else
# try-except-finally



# # The Begining
# try:
#     a=7
#     b=0
#     c=a/b
# except:
#     print("Error: Kuch to gadbad hai daya!!!")
# else:
#     print(c)
# finally:
#     print("Yeh to hona hii tha!!")



# try:
#     a=7
#     b=0
#     c=a/b
# except Exception as e:
#     print(e)
# else:
#     print(c)
# finally:
#     print("Yeh to hona hii tha!!")



# try:
#     a=7
#     b=0
#     c='7'+7
# except TypeError:  #only handles TypeError
#     print("Not possible")
# finally:
#     print("Yeh to hona hii tha!!")



# try:
#     a=7
#     b=0
#     # d=a/b  #zero division error
#     # c='7'+7
#     c='7'+7
#     d=a/b  #Not possible
# except TypeError:
#     print("Not possible")
# finally:
#     print("Yeh to hona hii tha!!")



# try:
#     a=7
#     b=0
#     # d=a/b  #zero division error
#     # c='7'+7
#     c='7'+7
#     d=a/b  #Not possible
# except TypeError:
#     print("Not possible")
# except ZeroDivisionError:
#     print("Division Error")
# finally:
#     print("Yeh to hona hii tha!!")



# # IMP MCQ
# try:
#     a=7
#     print(a)
#     l=[1,2,3]
#     print(l[100])
#     l+='vishal10'
# except TypeError:
#     print("Not Possible")
# except ZeroDivisionError:
#     print('zero error')
# finally:
#     print("Yeh to hoga hii")
# # 7
# # yeh to hoga hii
# # IndexError: list index out of range



# try:
#     money=7000
#     withdraw=9000
#     if (money-withdraw)<=0:
#         raise Exception('Paisa pati gaya')
# except Exception as e:
#     print(e)



# # Extra (Out of syllabus)
# class jaynil(Exception):
#     def __init__(self,msg):
#         self.msg=msg
# try:
#     money=7000
#     withdraw=9000
#     if (money-withdraw)<=0:
#         raise jaynil('Paisa pati gaya')
# except Exception as e:
#     print(e)

        