# QAC SFIA2 Project

This application is a simple [Flask application](https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application), ready to be deployed, for your SFIA2 project.

The following information should be everything you need to complete the project.

## Brief

The application must:

- Be deployed to a **Seperate Virtual Machine using Docker**
- Be deployed in a **Docker Compose Network within a Load Balancer**
- Be controlled with a **CI/CD Pipeline using Jenkins**
- Make use of a **Managed Database solution**

## Application

The application is a Flask application running in **2 micro-services** (*frontend* and *backend*).  

The database directory is available should you: 
  - want to use a MySQL container for your database at any point, *or*
  - want to make use of the `Create.sql` file to **set up and pre-populate your database**.

The application works by:
1. The frontend service making a GET request to the backend service. 
2. The backend service using a database connection to query the database and return a result.
3. The frontend service serving up a simple HTML (`index.html`) to display the result.

### Database Connection

The database connection is handled in the `./backend/application/__init__.py` file.

A typical Database URI follows the form:

```
mysql+pymysql://[db-user]:[db-password]@[db-host]/[db-name]
```

An example of this would be:

```
mysql+pymysql://root:password@mysql:3306/orders
```

### Environment Variables

The application makes use of **2 environment variables**:

- `DATABASE_URI`: as described above
- `SECRET_KEY`: any *random string* will work here

### Running a Flask Application

Typically, to run a Flask application, you would:

1. Install the pip dependencies:

```
pip install -r requirements.txt
```

2. Run the application:

```
python3 app.py
```

![app-diagram](https://i.imgur.com/wnbDazy.png)


## Infrastructure

The **Minimum Viable Product** for this project should at least demonstrate the following infrastructure diagram:

![mvp-diagram](https://i.imgur.com/tW80MrE.png)

- Terraform to provision the following: 
  - VPC
  - IGW
  - Route Table
  - Subnet(s)
  - Security Group(s)
  - EC2(s)
  - RDS
  - Elastic Load Balancer

- Ansible to configure all EC2s automatically 
- Jenkins used to control the CI/CD 
- Docker VM used to deploy containers/application
- Elastic Load balancer used to balance EC2s for application

**Good luck!**
