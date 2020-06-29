#-*-coding: utf-8 -*-

import argparse
#import sys
#sys.path.append('/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages')

#import gensim
#from konlpy.tag import Twitter

# argparse
parser = argparse.ArgumentParser()

parser.add_argument('input', type=str, help="ex) '안녕하세요 ~~', 사용자로부터 고민 데이터를 입력받는다. -- 나중에 생각해주어야 하는 것은 어느정도 길이까지 입력이 가능한지 제한을 풀어주어야 한다.")


args = parser.parse_args()


user_input = args.input

print(user_input)
