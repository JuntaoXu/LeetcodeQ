import os
import requests, json
import re
import datetime

Remove = ["</?p>", "</?ul>", "</?ol>", "</li>", "</sup>"]
Replace = [["&nbsp;", " "], ["&quot;", '"'], ["&lt;", "<"], ["&gt;", ">"],
           ["&le;", "≤"], ["&ge;", "≥"], ["<sup>", "^"], ["&#39", "'"],
           ["&times;", "x"], ["&ldquo;", "“"], ["&rdquo;", "”"],
           [" *<strong> *", " **"], [" *</strong> *", "** "],
           [" *<code> *", " `"], [" *</code> *", "` "], ["<pre>", "```\n"],
           ["</pre>", "\n```\n"], ["<em> *</em>", ""], [" *<em> *", " *"],
           [" *</em> *", "* "], ["</?div.*?>", ""], ["	*</?li>", "- "]]


def convert(src):
    # pre内部预处理
    def remove_label_in_pre(matched):
        tmp = matched.group()
        tmp = re.sub("<[^>p]*>", "", tmp)  # 不匹配>与p
        return tmp

    src = re.sub("<pre>[\s\S]*?</pre>", remove_label_in_pre,
                 src)  # 注意此处非贪心匹配，因为可能有多个示例
    # 可以直接删除的标签
    for curPattern in Remove:
        src = re.sub(curPattern, "", src)
    # 需要替换内容的标签
    for curPattern, curRepl in Replace:
        src = re.sub(curPattern, curRepl, src)
    return src


# 根据题目的 id 获取题目的名字，内容，代码块，标签，返回 json 格式的 dict 对象。
def get_all(slug):
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36"
    session = requests.Session()
    url = "https://leetcode-cn.com/graphql"
    params = {
        'operationName':
        "getQuestionDetail",
        'variables': {
            'titleSlug': slug
        },
        'query':
        '''query getQuestionDetail($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                questionId
                questionFrontendId
                title
                titleSlug
                content
                translatedTitle
                translatedContent
                difficulty
                topicTags {
                    name
                    slug
                    translatedName
                    __typename
                }
                codeSnippets {
                    lang
                    langSlug
                    code
                    __typename
                }
                __typename
            }
        }'''
    }
    json_data = json.dumps(params).encode('utf8')
    headers = {
        'User-Agent': user_agent,
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Referer': 'https://leetcode-cn.com/problems/' + slug
    }
    resp = session.post(url, data=json_data, headers=headers, timeout=10)
    resp.encoding = 'utf8'
    content = resp.json()
    # 题目详细信息
    # print(content)
    question = content['data']['question']
    return question


def get_problem_content(slug):
    question = get_all(slug)
    res = convert(question['translatedContent'])
    # 在正文后面填上标签
    res += "\n \n**标签**\n"
    tags = question['topicTags']
    for tag in tags:
        if tag['translatedName'] != None:
            tagName = tag['translatedName']
        else:
            tagName = tag['name']
        res += "`" + tagName + "` "

    return res + "\n"

# 生成 markdown 文件
def gen_markdown(path, content, title, url):
    file = open(path, 'a', encoding="utf-8")
    markdowncontenct = """# {titlename}
[{Url}]({Url})
## 原题
{Content}

##
```go

```
>
""".format(titlename=title, Url=url, Content=content)
    file.write(markdowncontenct)
    print(path)
    file.close()


url = "https://leetcode-cn.com/problems/simple-bank-system/"

slug = url.replace("https://leetcode-cn.com/problems/", "", 1).strip('/')
question = get_all(slug=slug)


current = datetime.datetime.now()
print(current)
date = str(current).split(" ")[0]

title = date + '.' + question['questionFrontendId'] + '.' + question['translatedTitle']

content = get_problem_content(slug)

content = re.sub(r'\n\n\n\n*', "\n", content)  # 替换掉多个换行符

base_dir = os.getcwd()
newfolder = os.path.join(base_dir, title.replace(". ", ".").replace(" ", "-"))
if not os.path.exists(newfolder):
    os.makedirs(newfolder)
    print("create new folder ", newfolder)
else:
    print("already exist folder:", newfolder)

f0 = os.path.join(base_dir, newfolder, 'solution_juntao.py')
f1 = os.path.join(base_dir, newfolder, 'solution_stacey.py')

open(f0, 'a').close()
open(f1, 'a').close()

# 生成 markdown 文件
filepath = os.path.join(base_dir, newfolder, "README.md")
gen_markdown(filepath, content, title, url)
