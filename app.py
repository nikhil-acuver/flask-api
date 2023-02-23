from flask import Flask,jsonify, request

app= Flask(__name__)

fruits = [
    {
        'name':'mango',
        'price':100
    },
    {
        'name':'apple',
        'price':90
    },
    {
        'name':'grapes',
        'price':80
    }
]

@app.route('/')
def greet():
    return 'hello world'

#retriving all fruits
@app.route('/fruits')
def get_fruits():
    return jsonify({'fruits':fruits})


#retriving single fruit/Dynamic url
@app.route('/fruit/<string:name>')
def get_fruit(name):
    for fruit in fruits:
        if fruit['name'] == name:
            return jsonify({'fruit':fruit})
    return jsonify({'your fruit not found':'try other'})  

@app.get('/get_fruit')
def get_fruitbyquery():
    req_name = request.args.get('name')
    for fruit in fruits:
        if fruit['name'] == req_name:
            return fruit
    return jsonify({'your fruit not found':'try other'}) 

@app.put('/update_fruit')
def update_fruit():
    req_update= request.get_json()
    for fruit in fruits:
        if fruit['name'] == req_update['name']:
            fruit['price']=req_update['price']
            return {'message':'fruit updated'}
    return jsonify({'your fruit not found':'try other'}) 

@app.post('/add_fruit')
def add_fruit():
    request_add= request.get_json()
    fruits.append(request_add)
    return {'message':'fruit added'}

@app.delete('/delete_fruit')
def delete_fruit():
    req_name = request.args.get('name')
    for fruit in fruits:
        if fruit['name'] == req_name:
            fruits.remove(fruit)
            return {"successfully":"deleted"}
    return jsonify({'your fruit not found':'try other'}) 

      

if __name__==("__main__"):
    app.run(debug=True)
    