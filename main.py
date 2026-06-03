from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
   return {"message": "Hello FastAPI"}

@app.get("/users")
def get_users():
   return [
       {"id": 1, "name": "Bold"},
       {"id": 2, "name": "Saraa234"}
   ]



@app.post("/users")
def create_user():
  return {
      "message": "User created"
  }
