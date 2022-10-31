<h1 align='center'> CRUD exercise with Python, FastAPI and MongoDB </h1>

<img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white"/> <img src="https://img.shields.io/badge/fastapi-109989?style=for-the-badge&logo=FASTAPI&logoColor=white"/> 

## Running the API

1. Clone the repository

```
https://github.com/naomyduarteg/CRUD_python_mongo.git
```
2. Create a virtual environment

```
python3 -m venv <name_of_venv>
```
3. Go to the virtual environment's directory and activate it

For Windows:
```
Scripts/activate
```
For Linux/Mac:
```
bin/activate
```
4. Install the requirements

```
pip install -r requirements.txt
```

6. Run the API with uvicorn

```
uvicorn main:app --reload
```

The message "Project connected to the MongoDB database!" muts appear if everything is right. From this point, one can use the Swagger documentation to test the API and MongoDB Compass to visualize the collections and documents. 
More information can be found at <a href="https://naomy-gomes.medium.com/crud-with-python-fastapi-and-mongodb-e830c6c538f4">my Medium article</a>.
