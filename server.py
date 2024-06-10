import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "True"
from app.main import app


if __name__ == "__main__":
    app.run()
