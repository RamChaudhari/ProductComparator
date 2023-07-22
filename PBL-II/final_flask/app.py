from flask import Flask, jsonify
from flask import render_template
from flask import url_for,request,redirect,session
from icecream import ic
import test_chroma
import test_hnm
import test_amazon_elec
import test_flip_elec
import test_flip_fash
import test_amazon_fash
import test_ajio



app=Flask(__name__)
app.secret_key="jaee"



@app.route('/login', methods=["GET"])
def search():
    query = request.args.get('query')
    print(query)
    domain = request.args.get('type')

    results = {}
    storenames = []

    if "electronics" in domain.casefold():
        storenames = ["Croma", "Amazon", "Flipkart"]
        results["Croma"] = user_croma(query)
        results["Flipkart"] =  user_flip_ele(query)
        results["Amazon"] = user_amaz_ele(query)

    else:
        storenames = ["AJIO", "Amazon", "H&M"]
        results["AJIO"] = user_ajio(query)
        results["Amazon"] = user_amazon_fash(query)
        results["H&M"] = user_hnm(query)
        # results["Flipkart"] = user_flip_fash(query)

   
    response = jsonify({
         'storeNames' : storenames,
         'storeItems': results,
         'colors': [
             "#ff00000",
             "#ff00000",
             "#ff00000",
         ]
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

        
def user_hnm(search_query):
    results_hnm = test_hnm.search(search_query)
    return results_hnm

def user_ajio(search_query):

    results_ajio=test_ajio.search(search_query)
    return results_ajio

def user_flip_fash(search_query):
     results_flip_fash=test_flip_fash.flipFashion(search_query)
     return results_flip_fash

def user_amazon_fash(search_query):
     results_amazon_fash=test_amazon_fash.search(search_query)
     return results_amazon_fash

def user_croma(search_query):
     results_chroma=test_chroma.search(search_query)
     return results_chroma

def user_amaz_ele(search_query):
     results_amazon_ele=test_amazon_elec.search(search_query)
     return results_amazon_ele

def user_flip_ele(search_query):
     results_flip_ele=test_flip_elec.flipElect(search_query)
     return results_flip_ele

if(__name__=='__main__'):
    app.run(debug=True,port=5500)
    