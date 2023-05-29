import requests
import os
import sys
import json
import urllib.request as urlreq

url = "https://itestcloud.unipus.cn/utest/itest-mobile-api/all-role/report/detail"

se = requests.Session()

id_list = {}

# Unit1
epid = "1031468857"
# 短对话,长对话,短文
id_list[epid]=["8956d4kn","tx22srct","qr108c4b"]

# Unit2
epid = "1031473753"
# 短对话,长对话,短文
id_list[epid]=["8956d4kn","tx22srct","qr108c4b"]

# Unit3
epid = "1031484805"
# 短对话,长对话,短文
id_list[epid]=["8956d4kn","tx22srct","qr108c4b"]

# Unit4
epid = "1031485174"
# 短对话,长对话,短文
id_list[epid]=["8956d4kn","tx22srct","qr108c4b"]

# Unit5
epid = "1031486508"
# 短对话,长对话,短文
id_list[epid]=["8956d4kn","tx22srct","qr108c4b"]

# Unit6
epid = "1031496512"
# 短对话,长对话,短文
id_list[epid]=["8956d4kn","tx22srct","qr108c4b"]

# Unit7
epid = "1031651651"
# 短对话,长对话,短文
id_list[epid]=["8956d4kn","tx22srct","qr108c4b"]

# Unit8
epid = "1031652026"
# 长对话,短文
id_list[epid]=["w3fibsyr","6uv45paz"]

# Unit9
epid = "1031652351"
# 长对话,短文
id_list[epid]=["w3fibsyr","6uv45paz"]

# Unit10
epid = "1031841219"
# 长对话,短文
id_list[epid]=["w3fibsyr","6uv45paz"]

# Unit11
epid = "1031842897"
# 长对话,短文
id_list[epid]=["w3fibsyr","6uv45paz"]

# Unit12
epid = "1031872435"
# 长对话,短文
id_list[epid]=["w3fibsyr","6uv45paz"]

# Unit13
epid = "1032030869"
# 长对话,短文
id_list[epid]=["w3fibsyr","6uv45paz"]

# Unit14
epid = "1032031164"
# 长对话,短文
id_list[epid]=["w3fibsyr","6uv45paz"]

# Unit15
epid = "1032033571"
# 长对话,短文
id_list[epid]=["w3fibsyr","6uv45paz"]

with open('cookie.txt', 'rt', encoding='utf-8') as f:
    cookie = f.read().strip()
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Cookie': cookie
}

i = 1

all_right_option = ""
os.makedirs("./Listen/",exist_ok=True)

for epid in id_list.keys():
    print(epid)
    if os.path.exists(f"./Listen/Unit{i}.md"):
        i += 1
        continue
    all_right_option += f"# Unit {i} {epid}\n"
    to_write_inmd = ""
    to_write_inmd += f"# Unit {i} {epid}\n"
    j = 1
    os.makedirs(f"Unit{i}/",exist_ok=True)
    for nodeId in id_list[epid]:
        to_write_inmd += f"## Part {j} {nodeId}\n"
        data_unit1 = {"epid": epid, "nodeId": nodeId}
        if not os.path.exists(f"{i}_{j}_{epid}{nodeId}.json"):
            resp = se.post(url=url, json=data_unit1,headers=DEFAULT_REQUEST_HEADERS)

            print(resp.status_code)

            resj = json.loads(resp.text)

            code = resj['code']

            result = resj['rs']

            with open(f"{i}_{j}_{epid}{nodeId}.json",'w',encoding='utf8') as fw:
                json.dump(result,fw,ensure_ascii=False)
        else:
            with open(f"{i}_{j}_{epid}{nodeId}.json",'r',encoding='utf8') as fr:
                result = json.load(fr)

        quesGroups = result['quesGroups']
        subScores = result['subScores']
        quesInfos = quesGroups[0]['quesInfos']
        questions = quesGroups[0]['questions']
        for quesInfo in quesInfos:
            quesId = quesInfo['quesId']
            print(quesId)
            to_write_inmd += f"### Question {quesId}\n"
            subQuesInfos = quesInfo['subQuesInfos']
            resPath = quesInfo['resPath']
            resTitle = quesInfo['resTitle']
            if subQuesInfos:
                try:
                    urlreq.urlretrieve(resPath,f"Unit{i}/{quesId}.mp3")
                except Exception as e:
                    print(e)
                    print(resPath)
                to_write_inmd += f"全文资源：{resTitle}\n音频："+ f'<audio id="audio" controls="" preload="none"><source id="mp3" src="{resPath}"></audio>' + f"\n本地缓存路径：Unit{i}/{quesId}.mp3\n"
                for subQuesInfo in subQuesInfos:
                    options = subQuesInfo['options']# 选项
                    qparse = subQuesInfo['qparse']
                    resPath = subQuesInfo['resPath']
                    resTitle = subQuesInfo['resTitle']
                    startIndex = subQuesInfo['startIndex']
                    # <audio id="audio" controls="" preload="none">
                    #     <source id="mp3" src="音频地址">
                    # </audio>
                    all_right_option += f"{startIndex} : "
                    to_write_inmd += f"\nQuestion：{resTitle}\n音频：" + f'<audio id="audio" controls="" preload="none"><source id="mp3" src="{resPath}"></audio>'+ f"\n本地缓存路径：Unit{i}/{quesId}.mp3\n"
                    for option in options:
                        if option['right']:
                            to_write_inmd += f"***{option['optionName']} : {option['optionValue']}***\n"
                            all_right_option += f" ***{option['optionValue']}***\n"
                        else:
                            to_write_inmd += f"{option['optionName']} : {option['optionValue']}\n"
                    to_write_inmd += f"解析：{qparse}\n"
                    try:
                        urlreq.urlretrieve(resPath,f"Unit{i}/{quesId}_{startIndex}.mp3")
                    except Exception as e:
                        print(e)
                        print(resPath)
            else:
                startIndex = quesInfo['startIndex']
                all_right_option += f"{startIndex} : "
                try:
                    urlreq.urlretrieve(resPath,f"Unit{i}/{quesId}_{startIndex}.mp3")
                except Exception as e:
                    print(e)
                    print(resPath)
                to_write_inmd += f"短对话文本：{resTitle}\n音频：" + f'<audio id="audio" controls="" preload="none"><source id="mp3" src="{resPath}"></audio>'+ f"\n本地缓存路径：Unit{i}/{quesId}.mp3\n"
                options = quesInfo['options']# 选项
                qparse = quesInfo['qparse']
                for option in options:
                    if option['right']:
                        to_write_inmd += f"***{option['optionName']} : {option['optionValue']}***\n"
                        all_right_option += f" ***{option['optionValue']}***\n"
                    else:
                        to_write_inmd += f"{option['optionName']} : {option['optionValue']}\n"
                to_write_inmd += f"解析：{qparse}\n"
        j += 1
    with open(f"./Listen/Unit{i}.md",'w',encoding='utf8') as fww:
        fww.write(to_write_inmd)
    
    i += 1
    
with open("./Listen/Options.md",'w',encoding='utf8') as fwww:
    fwww.write(all_right_option)