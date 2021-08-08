# _*_ coding : utf-8 _*_
# __author__ : YiXuan
# __date__ : 2019/10/15 10:11
# __software__ : PyCharm


def Tower_of_Hanoi(start, auxiliary, end, number):
    global step
    if number == 1:
        step += 1
        print(f'第{step}步: {start} ==> {end}')
    elif number == 2:
        step += 1
        print(f'第{step}步: {start} ==> {auxiliary}')

        step += 1
        print(f'第{step}步: {start} ==> {end}')

        step += 1
        print(f'第{step}步: {auxiliary} ==> {end}')
    else:
        Tower_of_Hanoi(start=start, auxiliary=end, end=auxiliary, number=number - 1)
        Tower_of_Hanoi(start=start, auxiliary=auxiliary, end=end, number=1)
        Tower_of_Hanoi(start=auxiliary, auxiliary=start, end=end, number=number - 1)


if __name__ == "__main__":
    start = 'x'
    auxiliary = 'y'
    end = 'z'
    step = 0

    Tower_of_Hanoi(start, auxiliary, end, 4)