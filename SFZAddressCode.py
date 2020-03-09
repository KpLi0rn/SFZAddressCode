num = input("请输入身份证前四位:")
try:
    res = []
    with open('lib/dict.txt','r+') as file:
        lines = file.readlines()
        for value in lines:
            if value.startswith(num) and len(num) == 4:
                value = value.strip('\n')
                print(value)
                res.append(value)
        if len(res) == 0:
            print("您的输入有误或您输入的前四位不是合法的身份证开头")
except Exception as e:
    print(e)
