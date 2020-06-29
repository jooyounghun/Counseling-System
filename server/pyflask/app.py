#-*-coding: utf-8 -*-
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)
import json

import subprocess

#import mysql.connector



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/search')
def item_search():
    return render_template('search.html')

#Pain

@app.route('/gominsolve_pain')
def gominsolve_pain():
    return render_template('pain.html')

@app.route('/pain1')
def pain1():
    return render_template('pain1.html')

@app.route('/pain2')
def pain2():
    return render_template('pain2.html')

@app.route('/pain3')
def pain3():
    return render_template('pain3.html')

#Health

@app.route('/gominsolve_health')
def gominsolve_health():
    return render_template('health.html')

@app.route('/health1')
def health1():
    return render_template('health1.html')

@app.route('/health2')
def health2():
    return render_template('health2.html')

#Love

@app.route('/gominsolve_love')
def gominsolve_love():
    return render_template('love.html')

@app.route('/love1')
def love1():
    return render_template('love1.html')

#Lazy

@app.route('/gominsolve_lazy')
def gominsolve_lazy():
    return render_template('lazy.html')

@app.route('/lazy1')
def lazy1():
    return render_template('lazy1.html')

#Pray

@app.route('/gominsolve_pray')
def gominsolve_pray():
    return render_template('pray.html')

@app.route('/pray1')
def pray1():
    return render_template('pray1.html')

@app.route('/pray2')
def pray2():
    return render_template('pray2.html')

#Fear

@app.route('/gominsolve_fear')
def gominsolve_fear():
    return render_template('fear.html')

@app.route('/fear1')
def fear1():
    return render_template('fear1.html')

@app.route('/fear2')
def fear2():
    return render_template('fear2.html')

@app.route('/fear3')
def fear3():
    return render_template('fear3.html')

#Work

@app.route('/gominsolve_work')
def gominsolve_work():
    return render_template('work.html')

@app.route('/work1')
def work1():
    return render_template('work1.html')

@app.route('/work2')
def work2():
    return render_template('work2.html')

@app.route('/work3')
def work3():
    return render_template('work3.html')

@app.route('/work4')
def work4():
    return render_template('work4.html')

#Truth

@app.route('/gominsolve_truth')
def gominsolve_truth():
    return render_template('truth.html')

@app.route('/truth1')
def truth1():
    return render_template('truth1.html')

#Else

@app.route('/gominsolve_else')
def gominsolve_else():
    return render_template('info.html')



@app.route('/item_request', methods=['POST'])
def item_query():
    value1 = request.form['item_id']
    print(value1)
    result = subprocess.check_output ("python user_input.py '"+value1+"'", shell=True, encoding='utf-8')
    #test = os.system("python test.py '"+value1+"'")
    #del(user_input_cls)
    
    #print("user_input_cls 참조개수: ", sys.getrefcount(user_input_cls))
    
    top_score_item = result
    print(result)
    
    #for i in Score:
        #arr.append((i[0].encode('cp949'),i[1]))
        #arr.append(i[0].encode('cp949'))
    json_return = json.dumps(top_score_item,ensure_ascii = False)
#    json_return.status_code = 200
#    json_return.headers['Access-Control-Allow-Origin'] = '*'
    return jsonify(json_return)

if __name__ =='__main__':
    app.run(host='0.0.0.0',port=5000)
    
#db.close()

