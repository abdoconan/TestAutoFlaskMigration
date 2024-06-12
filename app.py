from src import create_app
from src.models.user import User




app =  create_app()

if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=8000)