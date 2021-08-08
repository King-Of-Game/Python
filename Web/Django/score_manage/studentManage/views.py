from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.clickjacking import xframe_options_exempt
from django.http import HttpResponse, JsonResponse
from django.db import connection
from studentManage.models import ChooseSub
from studentManage.models import Student
from studentManage.models import Score
from studentManage.models import User
from studentManage.models import Teacher



# Create your views here.

''' 后台管理主界面 '''
# 跳转后台管理主界面
def studentManage(request):
    return render(request, 'studentManage/studentManage.html')

''' 接口管理 '''

# 得到 session 对象中的用户信息
def getSession(request):
    data = {}
    if request.method == 'GET':
        data['account'] = request.session['account']
        data['nickname'] = request.session['nickname']
        data['roleID'] = request.session['roleID']
        # print(data['account'])
        # print(data['nickname'])
        # print(data['roleID'])

    return JsonResponse(data)

# 清除 session 对象中的用户信息
def clearSession(request):
    data = {}
    if request.method == 'POST':
        request.session['account'] = ''
        request.session['nickname'] = ''
        request.session['roleID'] = ''
        data['account'] = request.session['account']
        data['nickname'] = request.session['nickname']
        data['roleID'] = request.session['roleID']
    return JsonResponse(data)

# 得到可供选择的课程
def getChooseSubject(request):
    # 返回数据格式{"code":0,"data":[{},{},{}]}
    data = {}
    list = []
    sql = "SELECT scb.subjectID, sub.subjectName, scb.isChoose\
    from studentmanage_choosesub scb, studentmanage_subject sub\
    where scb.subjectID = sub.subjectID\
    and studentID = '%s'\
    order by subjectID" % request.session['account']
    cursor = connection.cursor()
    cursor.execute(sql)
    rawData = cursor.fetchall()
    # print(rawData)
    for i in rawData:
        json = {}
        json['subjectID'] = i[0]
        json['subjectName'] = i[1]
        json['isChoose'] = '否' if i[2] == 0 else '是'
        list.append(json)
    if request.method == 'GET':
        data['code'] = 0
        data['count'] = len(list)
        data['data'] = list
        # print(data)
    return JsonResponse(data)

# 确认选课并填加一条对应课程的成绩数据（成绩默认为：0）
def confirmSubject(request):
    if(request.method == "POST"):
        studentID = request.session["account"]
        subjectID = request.POST["subjectID"]
        classID = Student.objects.filter(studentID=studentID).values('classID')[0]['classID']
        # 修改对应选课状态为True
        ChooseSub.objects.filter(subjectID=subjectID).update(isChoose=True)
        # 选课后增加一条对应的课程成绩
        obj = Score(studentID=studentID, subjectID=subjectID, classID=classID, score=0)
        obj.save()
        return HttpResponse("success")

# 取消选课并删除该课程的成绩数据
def cancelSubject(request):
    if(request.method == "POST"):
        studentID = request.session["account"]
        subjectID = request.POST["subjectID"]
        # 修改对应选课状态为False
        ChooseSub.objects.filter(subjectID=subjectID).update(isChoose=False)
        # 取消选课后删除对应的课程成绩
        obj = Score.objects.filter(studentID=studentID, subjectID=subjectID)
        obj.delete()
        return HttpResponse("success")

# 根据登录角色ID得到对应的成绩信息
def getScoreByRole(request):
    # 返回数据格式{"code":0,"count":0,"data":[{},{},{}]}
    data = {}
    list = []

    sql = ''
    # 如果登录角色是学生
    if request.session["roleID"] == 2:
        sql = "select ssu.subjectID, subjectName, sst.studentID, sst.`name`, sst.classID, score\
           from studentmanage_score ssc, studentmanage_student sst, studentmanage_subject ssu\
           where ssc.studentID = sst.studentID and ssu.subjectID = ssc.subjectID and sst.studentID = '%s'\
           order by subjectID" % request.session['account']
    # 如果登录角色是管理员
    elif request.session["roleID"] == 0:
        sql = "select ssu.subjectID, subjectName, sst.studentID, sst.`name`, sst.classID, score\
           from studentmanage_score ssc, studentmanage_student sst, studentmanage_subject ssu\
           where ssc.studentID = sst.studentID and ssu.subjectID = ssc.subjectID\
           order by subjectID"
    # 如果登陆角色是老师
    else:
        sql = "select ssu.subjectID, subjectName, sst.studentID, sst.`name`, sst.classID, score\
           from studentmanage_score ssc, studentmanage_student sst, studentmanage_subject ssu, studentmanage_teacher ste\
           where ssc.studentID = sst.studentID and ssu.subjectID = ssc.subjectID and ste.teacherID = ssu.teacherID and ste.teacherID = '%s'\
           order by subjectID" % request.session['account']


    cursor = connection.cursor()
    cursor.execute(sql)
    rawData = cursor.fetchall()
    # print(rawData)
    for i in rawData:
        json = {}
        json['subjectID'] = i[0]
        json['subjectName'] = i[1]
        json['studentID'] = i[2]
        json['studentName'] = i[3]
        json['classID'] = i[4]
        json['score'] = i[5]
        list.append(json)
    if request.method == 'GET':
        data['code'] = 0
        data['count'] = len(list)
        data['data'] = list
        # print(data)
    return JsonResponse(data)

# 修改学生对应课程的成绩
def updateScore(request):
    if(request.method == "POST"):
        subjectID = request.POST["subjectID"]
        studentID = request.POST["studentID"]
        score = request.POST["score"]
        try:
            score = float(score)
            if score >=0 and score <= 100:
                Score.objects.filter(subjectID=subjectID, studentID=studentID).update(score=score)
                return HttpResponse("Modified Successfully!")
            else:
                return HttpResponse("分数区间为：0~100")
        except BaseException:
            return HttpResponse("请输入正确的分数!")

# 根据登录角色ID得到对应的用户信息
def getUserByRole(request):
    if request.method == 'GET':
        aOrN = request.GET['aOrN']
        aOrN = '%' + aOrN + '%'

        # 返回数据格式{"code":0,"count":0,"data":[{},{},{}]}
        data = {}
        list = []

        sql = ''
        # 如果登录角色是学生
        if request.session["roleID"] == 2:
            sql = "SELECT account, `password`, nickname, sex, birthday, phone, address, roleID \
                    from studentmanage_user\
                    where account = '%s'" % request.session['account']
        # 如果登录角色是老师
        elif request.session["roleID"] == 1:
            sql = "SELECT account, `password`, nickname, sex, birthday, phone, address, roleID \
                    from studentmanage_user\
                    where (roleID = 2 or account ='%s') and (account like '%s' or nickname like'%s') \
                    order by roleID" % (request.session['account'], aOrN, aOrN)
        # 如果登陆角色是管理员
        else:
            sql = "SELECT account, `password`, nickname, sex, birthday, phone, address, roleID \
                    from studentmanage_user \
                    where account like '%s' or nickname like'%s' \
                    order by roleID" % (aOrN, aOrN)
        # print(sql)

        cursor = connection.cursor()
        cursor.execute(sql)
        rawData = cursor.fetchall()
        # print(rawData)
        for i in rawData:
            json = {}
            json['account'] = i[0]
            json['password'] = i[1]
            json['nickname'] = i[2]
            json['sex'] = '男' if i[3] == 0 else '女'
            json['birthday'] = i[4]
            json['phone'] = i[5]
            json['address'] = i[6]
            if i[7] == 0:
                json['roleID'] = '管理员'
            elif i[7] == 1:
                json['roleID'] = '教师'
            else:
                json['roleID'] = '学生'

            list.append(json)
            data['code'] = 0
            data['count'] = len(list)
            data['data'] = list

    return JsonResponse(data)

# 修改密码
def updatePwd(request):
    if (request.method == "POST"):
        account = request.POST['account']
        password = request.POST['password']
        User.objects.filter(account=account).update(password=password)
        if request.session['account'] == account:
            clearSession(request)
    return HttpResponse('Update Successfully!')

# 重置密码
def resetPwd(request):
    if (request.method == "POST"):
        account = request.POST['account']
        roleID = request.POST['roleID']
        if roleID == "管理员":
            User.objects.filter(account=account).update(password='admin')
        elif roleID == "教师":
            User.objects.filter(account=account).update(password='666666')
        else:
            User.objects.filter(account=account).update(password='123456')
        if request.session['account'] == account:
            clearSession(request)
    return HttpResponse('Reset Successfully!')

# 添加用户
def addUser(request):
    if(request.method == "POST"):
        account = request.POST['account']
        password = request.POST['password']
        nickname = request.POST['nickname']
        sex = request.POST['sex']
        birthday = request.POST['birthday']
        phone = request.POST['phone']
        address = request.POST['address']
        roleID = request.POST['roleID']
        name = request.POST['name']

        user = User.objects.filter(account=account)
        if len(user) > 0:
            return HttpResponse('This account has been registered!')
        else:
            # 先给用户表添加数据
            obj = User(account=account, password=password, nickname=nickname, sex=sex, birthday=birthday,
                       phone=phone, address=address, roleID=roleID)
            obj.save()

            if roleID == "2":   # 如果是学生，则添加数据到学生表
                classID = request.POST['classID']
                obj = Student(studentID=account, classID=classID, name= name)
                obj.save()

                # 填加学生选课信息
                for i in range(1, 7):
                    obj = ChooseSub(subjectID=i, studentID=account, isChoose=0)
                    obj.save()

            else:   # 如果是教师，则添加数据到学生表
                isHeadmaster = request.POST['isHeadmaster']
                if isHeadmaster == "1":     # 如果是班主任就添加所管理的班级号
                    classID = request.POST['classID']
                    obj = Teacher(teacherID=account, name=name, classID=classID, isHeadmaster=isHeadmaster)
                    obj.save()
                else:
                    obj = Teacher(teacherID=account, name=name, isHeadmaster=isHeadmaster)
                    obj.save()
            return HttpResponse('Add Account Successfully!')

    return HttpResponse('Add User Successfully!')


''' 接口管理 '''





''' iframe 跳转管理 '''
# 欢迎用户界面
@xframe_options_exempt
def welcome(request):
    return render(request, 'studentManage/welcome.html')

# 开始选课界面
@xframe_options_exempt
def chooseSubject(requset):
    return render(requset, 'studentManage/chooseSubject.html')

# 成绩查询界面
@xframe_options_exempt
def scoreDetail(request):
    return render(request, 'studentManage/scoreDetail.html')

# 用户查询界面
@xframe_options_exempt
def userDetail(request):
    return render(request, 'studentManage/userDetail.html')

# 添加用户界面
@xframe_options_exempt
def addAccount(request):
    return render(request, 'studentManage/addAccount.html')

''' iframe 跳转管理 '''
