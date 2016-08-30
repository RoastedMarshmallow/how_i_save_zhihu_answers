from tornado import httpclient
import answerparser
import time
from imagebuilder import ImageBuilder
from answerdrawer import AnswerDraw

test_answer_url = "https://www.zhihu.com/question/27651324/answer/118906589"

def __saveAnswerRaw(s):
    timestamp = time.strftime(r"%Y%m%d%H%M%S", time.localtime())
    with open("c:/Users/Administrator/Desktop/a/content" + timestamp + ".txt", "w", encoding='utf-8') as f:
        f.write(s)
        f.close()

def __getPageContent(url):
    client = httpclient.HTTPClient()
    try:
        response = client.fetch(url)
    except httpclient.HTTPError as e:
        print("Error: " + str(e))
    except Exception as e:
        print("Error: " + str(e))
    client.close()

    if response:
        s = str(response.body, 'utf-8')
        __saveAnswerRaw(s)
        return s

def test(url = test_answer_url):
    s = __getPageContent(url)
    return answerparser.parseAnswer(s)



answerdrawer = AnswerDraw(test(), ImageBuilder(), config)
answerdrawer.draw()




