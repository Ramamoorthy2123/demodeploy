from fastapi import FastAPI;
from fastapi.params import Body;
from pydantic import BaseModel;


app = FastAPI();

@app.get('/')
def display():
    return {'data': 'FastAPI Tutorial'}

# @app.post('/createPost')
# def createPost():
#     return {'message': 'Post created successfully'}

# def check(Basemodel):
#     title : str
#     price : int

# my_post = [{
#     'title':'OnePlus 12R',
#     'price':"40000"
# },
# {
#     'title': 'Iphone 15',
#     'price': '87000'
# }
# ]



# @app.post('/createPost')
# def phones(payload :  dict = Body(...)):
#  print(payload)
#  return{"data": f'Title : {payload.title}, price : {payload.price}'}

# # @app.post('/create_post')
# # def check(post:my_post):
# #     print(post)
# #     raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f'post not found')
# #     return {"data": post}
