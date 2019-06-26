from flask import Flask, render_template, request, url_for
import requests
import time
from bs4 import BeautifulSoup
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/output")
def output():
    kw = request.args.get('name','')
    top_kw = kw.replace(' ','%20')
    after_kw = kw.replace(' ','+')
    
    top_url ='https://fril.jp/s?query=%20' + top_kw +'&transaction=soldout'
    top_response = requests.get(top_url)
    top_response.encoding = top_response.apparent_encoding
    bs = BeautifulSoup(top_response.text, 'html.parser')
    price_tag = bs.findAll('span',{'itemprop':'price'})


    price_date = []
    
    for price in price_tag :
        price_text = price.text.replace(',', '')
        price_date.append(price_text)
        
    num = 2
    while num <= 5 :
        time.sleep(3)
        after_url = 'https://fril.jp/s?order=desc&page=' + str(num) +'&query=+' +  after_kw +  '&sort=relevance&transaction=soldout'
        after_response = requests.get(after_url)
        after_response.encoding = after_response.apparent_encoding
        bs2 = BeautifulSoup(after_response.text, 'html.parser')
        price_tag2 = bs2.findAll('span',{'itemprop':'price'})
        for price in price_tag2 :
            price_text2 = price.text.replace(',', '')
            price_date.append(price_text2)
        num += 1
        
        
    price_num = [int(s) for s in price_date]    
    ave = sum(price_num) / len(price_num)
    
    
    e = []

    for f in price_num :
        if f <= 9999 :
            e.append(9999)
        elif f <= 19999 :
            e.append(19999)
        elif f <= 29999 :
            e.append(29999)
        elif f <= 39999 :
            e.append(39999)
        elif f <= 49999 : 
            e.append(49999)
        elif f <= 59999 : 
            e.append(59999)
        elif f <= 69999 : 
            e.append(69999)
        elif f <= 79999 : 
            e.append(79999)
        elif f <= 89999 : 
            e.append(89999)
        elif f <= 99999 : 
            e.append(99999)  
        else :
            e.append(100000)
    
    price_range_box = []


    w=e.count(9999)
    price_range_box.append(w)

    n=e.count(19999)
    price_range_box.append(n)

    aa=e.count(29999)
    price_range_box.append(aa)

    cc=e.count(39999)
    price_range_box.append(cc)


    zz=e.count(49999)
    price_range_box.append(zz)

    ff=e.count(59999)
    price_range_box.append(ff)


    gg=e.count(69999)
    price_range_box.append(gg)

    ee=e.count(79999)
    price_range_box.append(ee)

    tt=e.count(89999)
    price_range_box.append(tt)

    kk=e.count(99999)
    price_range_box.append(kk)

    pp=e.count(100000)
    price_range_box.append(pp)


    lll = price_range_box[0]
    aaa= price_range_box[1]
    bbb= price_range_box[2]
    ccc= price_range_box[3]
    eee= price_range_box[4]
    ddd= price_range_box[5]
    fff= price_range_box[6]
    ggg= price_range_box[7]
    hhh= price_range_box[8]
    iii= price_range_box[9]
    jjj= price_range_box[10]
    



    
    
        
    return render_template('output.html',name0=kw,name=round(ave),name1=max(price_num),
    name2=min(price_num),price_name=lll,price_name1=aaa,price_name2=bbb,price_name3=ccc
    ,price_name4=eee,price_name5=ddd,price_name6=fff,price_name7=ggg,price_name8=hhh
    ,price_name9=iii,price_name10=jjj)

app.run(host='0.0.0.0', debug=True)


@app.route('/output')

def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=7777)
