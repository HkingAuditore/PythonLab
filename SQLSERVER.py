from random import choice

import numpy as np
import pyodbc
from faker import Faker


def GenerateStaff():
    fake = Faker("zh_CN")
    Faker.seed(np.random.randint(0, 99999))

    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=localhost;'
                          'Database=GameStudio;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()

    def GetPwd():
        return fake.password(length=10)

    Pwd = GetPwd()

    def GetGender():
        return np.random.randint(0, 2)

    Gender = GetGender()

    def GetName():
        return fake.name_male() if Gender == 1 else fake.name_female()

    Name = GetName()

    def GetBirthDay():
        return fake.date(pattern="%Y-%m-%d")

    BirthDay = GetBirthDay()

    def GetAddress():
        return fake.address()

    Address = GetAddress()

    def GetOccupation():
        l = ['策划', '程序', '美术', '音乐', 'HR', '技术美术']
        return choice(l)

    Occupation = GetOccupation()

    def GetLevel():
        l = ['实习', '总监', '助理', '初级', '中级', '高级']
        return choice(l)

    Level = GetLevel()

    def GetPhone():
        return fake.phone_number()

    Phone = GetPhone()

    def GetSalary():
        return fake.pyint(min_value=5000, max_value=30000)

    Salary = GetSalary()

    def GetOnWorkTime():
        return '09:00:00'

    OnWorkTime = GetOnWorkTime()

    def GetOffWorkTime():
        return '17:00:00'

    OffWorkTime = GetOffWorkTime()

    def GetWorkDayLength():
        return 5

    # WorkDayLength = GetWorkDayLength()
    # sql = 'declare @result int ' \
    #       'exec @result = insert_staff ?,?,?,?,?,?,?,?,?,?,?,?'
    # parms = (
    #     Pwd, Name, Gender, BirthDay, Address, Occupation, Level, Phone, Salary, OnWorkTime, OffWorkTime, WorkDayLength)
    #
    # cursor.execute(sql, parms)
    # cursor.commit()


# for i in range(0, 100):
#     GenerateStaff()


def GenerateGame():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=localhost;'
                          'Database=GameStudio;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()

    fake = Faker("zh_CN")
    Faker.seed(np.random.randint(0, 99999))
    l = ['传说', '战争', '模拟器', '信条', '末日', '战神', '幻想']
    name = fake.company_prefix() + fake.first_name() + choice(l)
    sql = 'declare @result int ' \
          'exec @result = insert_game ?,?'
    parms = (str(1000 + np.random.randint(13, 22))[-3:], name)

    print(name)
    cursor.execute(sql, parms)
    cursor.commit()


def GenerateOffWorkLog():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=localhost;'
                          'Database=GameStudio;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()

    fake = Faker("zh_CN")
    Faker.seed(np.random.randint(0, 99999))
    sender = str(100000 + np.random.randint(19, 119))[-5:]
    t = fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None)
    text = fake.paragraph()
    sql = 'declare @result int ' \
          'exec @result = insert_offWorkLog ?,?,?'
    parms = (sender, t, text)

    print(t.strftime("%Y-%m-%d"))
    cursor.execute(sql, parms)
    cursor.commit()


def GenerateCheckLog():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=localhost;'
                          'Database=GameStudio;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()
    sender = str(100000 + np.random.randint(19, 119))[-5:]
    Faker.seed(np.random.randint(0, 99999))
    sql = 'declare @result int ' \
          'exec @result = insert_checkLog ?,?'
    parms = (sender, np.random.randint(0, 5))

    print(sender)
    cursor.execute(sql, parms)
    cursor.commit()


def ChangeStaffGroup():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=localhost;'
                          'Database=GameStudio;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()
    for i in range(19, 119):
        sql = "UPDATE StaffInfo SET StaffGroupId = \'" + str(1000 + np.random.randint(13, 22))[
                                                         -3:] + "\' WHERE StaffID = \'" + str(100000 + i)[-5:] + "\'"
        print(sql)
        cursor.execute(sql)
        cursor.commit()


def GenerateWorkLog():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=localhost;'
                          'Database=GameStudio;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()
    Faker.seed(np.random.randint(0, 99999))
    fake = Faker("zh_CN")
    sender = str(100000 + np.random.randint(19, 119))[-5:]
    description = fake.text()
    game = str(100000 + np.random.randint(1, 21))[-5:]
    sql = 'declare @result int ' \
          'exec @result = insert_workLog ?,?,?'
    parms = (sender, description, game)

    # print(description)
    cursor.execute(sql, parms)
    cursor.commit()


def GenerateWorkPlan():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=localhost;'
                          'Database=GameStudio;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()
    Faker.seed(np.random.randint(0, 99999))
    fake = Faker("zh_CN")

    title = ''.join(fake.words(nb=4))
    originator = str(100000 + np.random.randint(19, 119))[-5:]
    receiver = str(100000 + np.random.randint(19, 119))[-5:]
    state = np.random.randint(0, 9)
    explanation = fake.text()
    game = str(100000 + np.random.randint(1, 21))[-5:]

    game = str(100000 + np.random.randint(1, 21))[-5:]
    sql = 'declare @result int ' \
          'exec @result = insert_workPlan ?,?,?,?,?,?'
    parms = (title, originator, receiver, state, explanation, game)

    # print(description)
    cursor.execute(sql, parms)
    cursor.commit()

def GenerateResume():
    conn = pyodbc.connect('Driver={SQL Server};'
                          'Server=localhost;'
                          'Database=GameStudio;'
                          'Trusted_Connection=yes;')

    cursor = conn.cursor()
    Faker.seed(np.random.randint(0, 99999))
    fake = Faker("zh_CN")

    phone=fake.phone_number()
    name=fake.name()
    occupation=fake.job()
    age=np.random.randint(20, 50)
    sql = 'declare @result int ' \
          'exec @result = insert_resume ?,?,?,?'
    parms = (phone, name, occupation, age)

    # print(description)
    cursor.execute(sql, parms)
    cursor.commit()


# for i in range(1, 20):
#     GenerateOffWorkLog()
Faker.seed(np.random.randint(0, 99999))
fake = Faker()
print(fake.name_male())
