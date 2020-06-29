#-*-coding: utf-8 -*-

import argparse
#import sys
#sys.path.append('/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages')

import gensim
from konlpy.tag import Twitter

# argparse
parser = argparse.ArgumentParser()

parser.add_argument('input', type=str, help="ex) '안녕하세요 ~~', 사용자로부터 고민 데이터를 입력받는다. -- 나중에 생각해주어야 하는 것은 어느정도 길이까지 입력이 가능한지 제한을 풀어주어야 한다.")


args = parser.parse_args()


user_input = args.input

pos_in = ['Noun','Verb','Adjective', 'Suffix']##,'URL','Verb','Unknown','Alpha','Foreign','Eomi','Josa','Suffix','Number','Hashtag','Eomi','Adjective']

tagged = []
sentence = [] 

#고통(pain)
sentence.append(("매일매일 너무 스트레스 받아서 힘들고 고통스럽습니다. 이럴 땐 어떻게 해야 하나요?","고통"))
sentence.append(("삶이 힘들고 고통스러워요, 하루에도 몇번씩 죽고싶다는 생각이 듭니다 어떻게 해야하나요?","고통"))
sentence.append(("힘든 고통속에서 허우적거리고 있는데 어떻게 해야 하나요?","고통"))
sentence.append(("갑자기 우울해지고 살기가 어려워 졌습니다. 이런 고통속에서는 어떻게 살아내야하나요?","고통"))
sentence.append(("세상에 고통은 왜 존재하는 것인가요? 고통이 주는 의미는 무엇인가요?","고통"))
sentence.append(("하나님을 믿어도 고통이 면재가 되질 않습니다. 너무 힘들고 어려운데 이럴 땐 어떻게 해야 하나요?","고통"))
sentence.append(("마음의 고통으로 힘들어 하고 있습니다. 이 마음의 고통을 덜어내려면 어떻게 해야 하나요?","고통"))
sentence.append(("지금 육체적인 고통에 시달리고 있습니다. 허리가 너무 아파서 어딜 나가지를 못합니다. 이럴 땐 어떻게 해야하나요?","고통"))
sentence.append(("제 인생은 고통뿐인 인생입니다. 제 인생의 고통을 해결하려면 어떻게 해야하나요?","고통"))
sentence.append(("살면서 감당할 수 없는 고난에 마주했습니다. 이 고난을 어떻게 피해갈 수 있을까요?","고통"))
#건강(health)
sentence.append(("제가 허리건강이 너무 안좋습니다. 건강해지려면 어떻게 해야 하나요?","건강"))
sentence.append(("건강하게 지내고 싶습니다. 어떻게 하면 건강해질 수 있나요?","건강"))
sentence.append(("제가 장이 안좋아서 매일 속이 더부룩합니다. 몸이 건강해지려면 어떻게 해야하나요?","건강"))
sentence.append(("내 몸의 건강을 유지하는 방법이 있을까요?","건강"))
sentence.append(("환절기에 건강 관리하는 방법을 알려주세요.","건강"))
sentence.append(("제가 나이가 많은데 건강해지고 싶습니다. 건강해지려면 어떻게 해야하나요?","건강"))
sentence.append(("몸이 약한 것 같아서 건강 관리를 좀 하려고 합니다. 어떻게 하면 좋을까요?","건강"))
sentence.append(("여름에 건강하게 지내려면 어떻게 해야 하나요? 알려주세요","건강"))
sentence.append(("암 안걸리고 건강하게 살고 싶습니다. 건강해지려면 어떻게 해야 하나요?","건강"))
sentence.append(("병에 걸려서 고생중입니다. 어떻게 하면 병이 낫고 건강해 질 수 있나요?","건강"))
#연애(love)
sentence.append(("지금 만난 남자친구와 결혼해도 괜찮을까요?","연애"))
sentence.append(("연애하고 싶은데 어떤 사람을 만나야하나요? 궁금합니다.","연애"))
sentence.append(("연애한지 4년이 지났는데 한 번도 싸운적이 없습니다. 이 사람과 결혼해도 괜찮을까요?","연애"))
sentence.append(("결혼하고 싶은데 어떤 사람을 만나서 결혼해야하나요?","연애"))
sentence.append(("지금 좋아하는 사람이 있는데 고백해도 될까요? 이 사람과 결혼하고 싶어요.","연애"))
sentence.append(("제가 좋아하는 사람과 저를 좋아하는 사람 둘 중에 어떤 사람을 만나야 하나요?","연애"))
sentence.append(("오랜기간 만나서 정도 많이 들고 추억도 많이 쌓인 연인이랑 결혼해도 괜찮을까요?","연애"))
sentence.append(("제가 벌이가 좋지는 않은데 결혼하고 싶습니다. 결혼해도 괜찮을까요?","연애"))
sentence.append(("결혼 상대는 어떻게 결정해야하나요?","연애"))
sentence.append(("어떤 사람과 연애하고 결혼해야하나요? 좋은사람은 어떤 사람인가요?","연애"))
#게으름(lazy)
sentence.append(("어느 순간 나태함과 게으름으로 문제가 발생하고 있습니다.","게으름"))
sentence.append(("나태, 태만, 게으름을 고칠수있는 방법좀 알려주세요","게으름"))
sentence.append(("전 진짜로 게을러서 어렸을 때부터 집에서는 커녕 학원에서 2시간도 공부하지 못했습니다.","게으름"))
sentence.append(("점점 제가 나태해진것 같아요. 의욕이 없어졌죠. 의욕이 생기더라도 몇일 지나면 사그라졌어요 지금 벌써 3주 지났습니다","게으름"))
sentence.append(("대학생이 되니까 사람이 게으르고 나태해지는 걸 느낍니다. 어떻게 하면 사람이 좀 더 부지런해질 수 있을까요?","게으름"))
sentence.append(("게으름에서 벗어난 경험자분들의 조언이 필요합니다.","게으름"))
sentence.append(("제 자신이 너무 게을러서 싫습니다. 해야할 공부도 많고 읽을 책도 많은데 오히려 많아서인지 부담감 때문에 그냥 다 놓아버리고 싶어요.","게으름"))
sentence.append(("게으름과 나태함으로 귀찮음을 느끼고 아무것도 안하는 제가 참 한심할 따름입니다. 어떻게 하면 게으름과 나태함을 고칠 수 있을까요?","게으름"))
sentence.append(("저의 게으름과 모든걸 귀찮아하는 나태함을 치유할 방법이 없을까요","게으름"))
sentence.append(("매일 침대에서 일어나기가 싫습니다. 많이 게을러지고 나태해진 것 같습니다.","게으름"))
#겸손(modest)
#sentence.append(("겸손한 마음을 가지려면 어떻게해야되나요? 겸손하다의 뜻이 뭔가요?","겸손"))
#sentence.append(("겸손 해지고 싶어요. 아직은 가진게 넉넉하지 않고 앞서 내세울 만큼 잘난 구석도 없구요. 보잘것 없고  부족 하지만 이 한몸 겸손한 맘으로 하나님만을 바라보며 늘 감사한 마음으로 살고 싶어요.","겸손"))
#sentence.append(("어떻게하면 좀 더 현명한 겸손한 사람이 될수 있을까요? 어떻게하면 남의 의견과 분야를 존중할수 있을까요?","겸손"))
#sentence.append(("마음이 교만해질때 묵상할 수 있는 가장 좋은 말씀 좀 부탁합니다.","겸손"))
#sentence.append(("진정한 겸손이란 무엇인가요?","겸손"))
#sentence.append(("겸손은 말로 들으면 참 실천하기 좋은것 같아요 근데 막상하면 실천의지가 부족해서인지 너무 자만하는거같아요 겸손해지법좀 알려주세요","겸손"))
#sentence.append(("자만하지 않으려면 어떻게 해야하나요?  저는 자만해서 방심하다가 낭패를 자주 봅니다.","겸손"))
#sentence.append(("착한 척 하는 사람이 아니라,  겸손한 척 하는 사람이 아니라  정말로 뼛 속까지 겸손한 사람이 되고 싶어요.","겸손"))
#sentence.append(("교만하지 않고 마음이 겸손한 사람이 되고 싶은데 어떻게 해야 하나요?","겸손"))
#sentence.append(("다른 사람을 존중하는 겸손한 사람이 되고 싶습니다. 교만을 버리고 싶습니다.","겸손"))
#기도(pray)
sentence.append(("기도를 하는법은 어떻게 되나요?","기도"))
sentence.append(("제가 교회를 다니는데 저만 방언을 안해서요 제가 평소에 기도도 잘 안해서 일까요?","기도"))
sentence.append(("교회를 다닌지 조금 오래 되지만 아직도 기도 하는 법를 잘 몰라서요. 기도는 어떻게 해야 하나요?","기도"))
sentence.append(("기도를 하고 싶은데 어떤 내용으로 기도를 해야하나요? 기도하면 응답을 받을 수 있나요?","기도"))
sentence.append(("기도할 때 구체적으로 무엇을 기도해야하는지 잘 모르겠습니다. 무엇에 대해서 기도해야하나요?","기도"))
sentence.append(("마음이 너무 복잡해서 기도가 되지 않습니다. 이럴 땐 어떻게 해야 하나요?","기도"))
sentence.append(("기도가 너무 어렵게 느껴지는데 기도는 어떻게 하는 건가요?","기도"))
sentence.append(("누군가를 위해서 기도하려는데 어떻게 기도해야하나요?","기도"))
sentence.append(("기도하는 것이 익숙하지 않고 교회를 다니지 않아서 기도하는 방법을 모르는데, 기도는 어떻게 하는 건가요?","기도"))
sentence.append(("기도에 집중이 잘 안되고 기도하면서 무슨 말을 해야하는지 잘 모르겠어요. 기도하는 방법에 대해서 알려주세요.","기도"))
#걱정(fear)
sentence.append(("요즘 세상걱정에 잠을 못이루고 있습니다. 이런 저런 불안이 찾아오면서 너무 힘드네요.","걱정"))
sentence.append(("걱정이 너무 많아서 일이 손에 안잡힙니다. 틈만나면 이런 걱정 저런 걱정이 드는데 어떻게 하면 좋을까요?","걱정"))
sentence.append(("요즘들어서 쓸데없는 걱정을 많이 해서 힘듭니다. 너무 생각이 많습니다. 도대체 어떻게 해야 쓸데없는 생각들을 안할 수 있을까요?","걱정"))
sentence.append(("제가 돈이 없어서 생활걱정에 시달리고 있습니다. 생활비에 대한 걱정을 안하려면 어떻게 해야 할까요?","걱정"))
sentence.append(("평소에 쓸데없는 걱정이 너무 많아서 힘듭니다. 걱정을 안하고 싶은데 어떻게 해야 할까요?","걱정"))
sentence.append(("일어나지도 않을 일들에 대해서 걱정도 되고 불안함에 두려움을 느끼기도 합니다. 어떻게 하면 두려움을 없앨 수 있을까요?","걱정"))
sentence.append(("제가 평소에 걱정과 염려가 많아서 일어나지도 않을 일에 두려움을 많이 느끼는데 어떻게 하면 좋을까요?","걱정"))
sentence.append(("걱정과 염려 때문에 힘듭니다. 어떻게 하면 걱정과 염려를 안할 수 있나요?","걱정"))
sentence.append(("계속 혼자 생각하고 걱정하고 불안해하고 하는데 어떻게 하면 염려를 없애고 두려워 하지 않을 수 있나요?","걱정"))
sentence.append(("기독교에서는 미래에 대한 걱정, 근심, 불안, 두려움이 있을때 어떻게 하나요?","걱정"))
#죄(sin)
sentence.append(("자꾸 지었던 죄를 반복해서 짓게 됩니다. 어떻게 하면 죄를 안지을 수 있나요?","죄"))
sentence.append(("제 동생이 죄를 지었습니다. 계속 반복해서 죄를 짓는데 어떻게 하면 좋나요?","죄"))
sentence.append(("사회가 점점 악해지고 범죄가 넘쳐나고 있습니다. 이 사회는 어떻게 죄에서 빠져 나올 수 있나요?","죄"))
sentence.append(("죄를 짓고 싶지 않은데 계속해서 죄를 짓게 됩니다. 어떻게 하면 좋을까요? 죄를 지었을 때는 어떻게 해야 하나요?","죄"))
sentence.append(("형제가 죄를 범한 것을 어떻게 하면 좋을까요? 죄를 용서해 주어야 하나요?","죄"))
sentence.append(("자매가 자꾸 죄를 짓는데 어떻게 하면 좋을까요? 죄를 지은 대가를 치르게 해야 하나요?","죄"))
sentence.append(("죄에서 벗어나고 싶은데 쉽지가 않습니다. 어떻게 하면 죄에서 벗어날 수 있나요? 죄를 짓지 않으려면 어떻게 살아야 하나요?","죄"))
sentence.append(("이 사회와 국가가 죄에 빠져 있는데 어떻게 하면 좋나요? 죄에서 자유를 얻게 하려면 어떻게 해야 할까요?","죄"))
sentence.append(("죄를 너무 많이 지었는데 저는 어떻게 되는 건가요? 죄를 해결 받기 위해서는 어떻게 해야 하나요?","죄"))
sentence.append(("죄를 범한사람을 어떻게 하면 좋을까요? 죄를 용서해줘야 할까요? 아니면 엄벌에 처해야 할까요?","죄"))
#일(work)
sentence.append(("일하면서 너무 지치고 힘들어요. 일하면서 일과 휴식의 균형은 어떻게 맞춰야 하나요?","일"))
sentence.append(("요새 일이 너무 바빠지면서 정신이 하나도 없습니다. 일을 이렇게 바쁘게만 하는게 맞나요?","일"))
sentence.append(("요새 일이 많아지면서 신앙이 뒷전이 되어가고 있습니다. 일과 신앙의 균형을 어떻게 맞춰야 하나요?","일"))
sentence.append(("일도 열심히 하고 신앙 생활도 열심히 하고 싶습니다. 어떻게 해야 하나요?","일"))
sentence.append(("일은 열심히 하려고 하는데 일에 성과가 나타나지 않습니다. 어떻게 하면 일의 성과를 만들 수 있나요?","일"))
sentence.append(("이제 곧 취업을 해야 하는데 어떤 직장에 다니는게 좋을까요? 또 어떤 마음가짐으로 직장에 임해야 할까요?","일"))
sentence.append(("이제 직장을 구해야 하는데 어떤 일을 해야할 지 잘 모르겠습니다. 어떤 직장을 선택하면 좋을까요?","일"))
sentence.append(("직장에서 일을 하는데 성과가 안나와서 매일 욕먹습니다. 어떻게 하면 좋은 결과를 얻어낼 수 있을까요?","일"))
sentence.append(("매일 일에 치이다보니 쉴 틈이 없습니다. 어떻게 하면 일과 쉼의 균형을 맞추어 갈 수 있나요?","일"))
sentence.append(("일을 열심히 하려하면 자꾸 신앙생활을 소홀히 하게 됩니다. 어떻게 하면 일과 신앙의 균형을 잘 맞출 수 있나요?","일"))
#진리(truth)
sentence.append(("진리는 무엇인가요? 어떻게 하면 진리에 대해서 알게 되나요?","진리"))
sentence.append(("진리에 대해서 알고 싶은데 어떻게 하면 알 수 있나요?","진리"))
sentence.append(("인생의 진리는 무엇일까요? 정말로 궁금합니다.","진리"))
sentence.append(("도대체 진리는 무엇인가요? 진리에 대해서 알고 싶습니다.","진리"))
sentence.append(("인생의 진리는 어디에 있나요? 진리를 깨닫게 되려면 어떻게 해야 하나요?","진리"))
sentence.append(("진리는 무엇인가요? 진리에 대해서 궁금함이 생겼는데 꼭 알고 싶습니다.","진리"))
sentence.append(("인생의 진리는 어디에서 찾을 수 있나요? 구체적으로 알려주세요.","진리"))
sentence.append(("모든것의 참 진리는 도대체 무엇인가요? 진리가 이 세상에 존재하기는 한 것인가요?","진리"))
sentence.append(("진리에 대해서 알고 싶습니다. 진리란 무엇인가요?","진리"))
sentence.append(("다들 진리에 대해서 얘기하는데 도대체 참 진리는 무엇인가요? 인생의 진리는 존재하는 것인가요?","진리"))



sentence.append((user_input,"고민"))


for record in sentence:
    twitter = Twitter()
    tpos = twitter.pos(record[0])
    s_t = []
    for t in tpos:
        if t[1] in pos_in and len(t[0]) > 0:
            if False == False : s_t.append(t[0])
            else : s_t.append(t[0]+'/'+t[1])
            
    words = s_t
    tagged.append(gensim.models.doc2vec.TaggedDocument(words,[record[1]]))
    
    
    
model = gensim.models.doc2vec.Doc2Vec(vector_size=30, window=5, min_count=5, epochs=5)

model.build_vocab(tagged)

model.train(tagged, total_examples=model.corpus_count, epochs=model.epochs)
n = len(model.docvecs)
UrlScore = model.docvecs.most_similar("고민", topn=n)

print(UrlScore[0][0])
