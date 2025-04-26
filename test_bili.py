import sys
import json

# 设置控制台输出编码为utf-8
sys.stdout.reconfigure(encoding='utf-8')

from langchain_community.document_loaders import BiliBiliLoader
SESSDATA ="0cf36899%2C1761196327%2Cb3e9f%2A42CjAhJV1ni9yR7H5WSqkiuO9wLsXjGEJGa1ph2mhCjAbvlWonDblumLBfS-BKkNqefm0SVkxlY3dXX3QxRmdTREhIb3VtaXZ6N2dYUlk2OXZnb1RPd1pWRkx5LVA3TFh5bUVQZ25LQmkyd3pCcmpTTnRyTmtfaUplZWtmcF9yMEZOOG1KQXFUTVFnIIEC"
BUVID3 = "68549F81-0DC0-A6AF-7165-30F929349E7E03047infoc"
BILI_JCT = "47813e66747aaff9931d0c173813cc42"
bv_id = "BV1iGpueKE26"
loader = BiliBiliLoader(
    [
        f"https://www.bilibili.com/video/BV15ioeYiEtj/",
    ],
    sessdata=SESSDATA,
    bili_jct=BILI_JCT,
    buvid3=BUVID3,
)
docs = loader.load()
# 使用json格式化输出，确保中文正确显示
print(json.dumps(docs[0].__dict__, ensure_ascii=False, indent=2))