import re

# 分组：
# text = "apple price is $99,orange price is $88"
# result = re.search('.+(\$\d+).+(\$\d+)',text)
# print(result.groups())

# group()/group(0)：匹配整个分组
# group(1)：匹配第一个分组
# group(2)：匹配第二个分组
# groups()：获取所有的分组


# findall：查找所有满足条件的
# text = "apple price is $99,orange price is $88"
# result = re.findall(r'\$\d+',text)
# print(result)

# sub：根据规则替换其他字符串
# text = "nihao zhongguo,hello world"
# new_text = text.replace(" ","\n")
# new_text = re.sub(r' |,','\n',text)
# print(new_text)
html = """
<div class="job-detail">
    <p>1. 3年以上相关开发经验 ，全日制统招本科以上学历</p>
    <p>2. 精通一门或多门开发语言(Python,C,Java等)，其中至少有一门有3年以上使用经验</p>
    <p>3. 熟练使用ES/mysql/mongodb/redis等数据库；</p>
    <p>4. 熟练使用django、tornado等web框架，具备独立开发 Python/Java 后端开发经验；</p>
    <p>5. 熟悉 Linux / Unix 操作系统&nbsp;</p>
    <p>6. 熟悉 TCP/IP，http等网络协议</p>
    <p>福利：</p>
    <p>1、入职购买六险一金（一档医疗+公司全额购买商业险）+开门红+全额年终奖（1年13薪，一般会比一个月高）</p>
    <p>2、入职满一年有2次调薪调级机会</p>
    <p>3、项目稳定、团队稳定性高，团队氛围非常好（汇合员工占招行总员工比例接近50%）；</p>
    <p>4、有机会转为招商银行内部员工；</p>
    <p>5、团队每月有自己的活动经费，法定节假日放假安排；</p>
    <p>6、办公环境优良，加班有加班费（全额工资为计算基数，加班不超过晚上10点，平日加班为时薪1.5倍，周末加班为日薪2倍，周末加班也可优先选择调休，管理人性化）。</p>
</div>
"""
# new_html = re.sub(r'<.+?>', "", html)
# print(new_html)


# split：根据规则分割字符串
# text = "nihao zhongguo,hello world"
# result = re.split(r' |,',text)
# print(result)


# compile：编译正则表达式
text = "apple 22.1 price is 34.56"

# result = re.findall('\d+\.?\d*',text)
# print(result)

# result = re.search('\d+\.?\d*',text)
# print(result.group())

# r = re.compile(r"""
# \d+ # 整数部分
# \.? # 小数点
# \d* # 小数部分
# """,re.VERBOSE)
# result = re.search(r,text)
# result = re.search(r"""
# \d+ # 整数部分
# \.? # 小数点
# \d* # 小数部分
# """,text,re.VERBOSE)
# print(result.group())













