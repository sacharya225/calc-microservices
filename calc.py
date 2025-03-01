from fastapi import FastAPI
import uvicorn

app=FastAPI()

@app.get("/")
async def homepage():
    return  "Welcome to MathoMania!!"


#getcalc(a: float ,b: float)
@app.get("/calculate")
async def getcalc(a: float ,b: float):
    return {
            "a" : a,
            "b" : b,
            "greater" : a if (a>b) else b,
            "sum" : (a+b),
            "difference" : (a-b),
            "product" : (a*b), 
            "division" :(a/b)
            
          }
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=6200)
